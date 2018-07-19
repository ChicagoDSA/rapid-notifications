from flask import Flask
from peewee import *

app = Flask(__name__)
app.config.from_object(__name__)

# TODO: This needs to be configurable per env
# TODO: make this pg if not local
db = SqliteDatabase("data.db")
