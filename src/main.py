import logging
import os
from flask import Flask, current_app
from flask import send_from_directory
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from api.utils.database import db
from api.config.config import ProductionConfig, TestingConfig
from api.config.config import DevelopmentConfig
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


@app.route('/', methods=['GET'])
def index():
    return response_with(resp.SUCCESS_200, value={"test": "ok"})


@app.route('/avatar/<path:filename>', methods=['GET'])
def uploaded_file(filename):
    print(f"filename {filename}")
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    print(f"UPLOADS {uploads}")
    return send_from_directory(directory=uploads, filename=filename)
    # return response_with(resp.SUCCESS_200, value=send_from_directory(app.config['UPLOAD_FOLDER'], filename, _external=True))


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
migrate = Migrate(app, db)
# with app.app_context():
#     db.create_all()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", use_reloader=False)
