from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from views import index_blueprint

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/niarf/PycharmProjects/untitled1/todo.db'
app.register_blueprint(index_blueprint)
db = SQLAlchemy(app)
