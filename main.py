import logging
import os
from flask import Flask, send_from_directory
from flask_jwt_extended import JWTManager
from api.utils.database import db
from api.config.config import ProductionConfig, TestingConfig, DevelopmentConfig
from api.utils.responses import response_with
import api.utils.responses as resp
from api.utils.email import mail
from api.routes.authors import author_routes
from api.routes.books import book_routes
from api.routes.users import user_routes

app = Flask(__name__)

if os.environ.get('WORK_ENV') == 'PROD':
    app_config = ProductionConfig()
elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()

app.config.from_object(app_config)
# START GLOBAL HTTP CONF

app.register_blueprint(author_routes, url_prefix='/api/authors')
app.register_blueprint(book_routes, url_prefix='/api/books')
app.register_blueprint(user_routes, url_prefix='/api/users')

@app.route('/avatar/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.after_request
def add_header(response):
    return response


@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)


@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)


@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_404)


jwt = JWTManager(app)
mail.init_app(app)
db.init_app(app)
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", use_reloader=False)