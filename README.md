# FLASK REST SAMPLE PROJECT

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Handling db migrations](#handling-db-migrations)
* [To do](#to-do)

## General info
This project is based on [Building REST APIs with Flask](https://www.amazon.com/Building-REST-APIs-Flask-Services/dp/1484250214) written by Kunal Relan. <br>
Due to large number of inaccuracies in the above position, I decided to improve, correct and tweak the code so it could run smoothly with Python 3.8. <br>
One of the improvements introduced in this code is the addition of database migration mechanism with [Flask-Migrate](https://flask-sqlalchemy.palletsprojects.com/).<br>
Future improvements may appear in the future as I explore REST API possibilities within Flask framework :)

## Technologies
Project is created with:
* Python 3.8
* SQLAlchemy
* MySQL
* And packages specified in requirements.txt file

## Setup
To run this project:
* Clone it!
* Create and activate Python virtual enviroment within main directory (for example with ***virtualenv***)
* Run *pip install -r requirements.txt*
* Setup your database server, in this case MariaDB from [XAMPP](https://www.apachefriends.org/) was used for the sake of simplicity. However feel free to use your favourite db engine as long as it is supported by SQLAlchemy
* Setup SMTP email, for example [GMAIL](https://support.google.com/a/answer/176600?hl=pl)
* In ```src/``` directory create ```credentials.py``` file and fill it in accordance with the example below:
```
DB_USER = <db_user>
DB_PASSWORD = <db_password>
FLASK_SECRET_KEY = <secret_key>
FLASK_SECURITY_PASSWORD_SALT = <salt>
MAIL_USERNAME = <full_email>
MAIL_PASSWORD = <email_password>
```
* Modify ```config.py``` in ```api/config/``` according to the database and SMTP used
* Run ```$ python app.py``` or ```$ flask run``` to start Flask server
* Run ```$ flask db init``` to initialize database migration mechanism

## Handling db migrations
Every time the database models change run:
* ```$ flask db migrate```
* ```$ flask db upgrade```

## To do
* REST API documentation with ```Swagger```
* Unit Tests with ```pytest```
