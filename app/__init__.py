from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "m!3@4#n/k\h-0===4"
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:12345678@localhost/qlstk?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

admin = Admin(app=app, name="QUAN LY SO TIET KIEM", template_mode="bootstrap3")

login = LoginManager(app=app)