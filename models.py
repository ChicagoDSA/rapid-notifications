from peewee import *
from app import db


class BaseModel(Model):
    class Meta:
        database = db

class Group(BaseModel):
    id = UUIDField()
    name = CharField(unique=True)

class Member(BaseModel):
    id = UUIDField()
    phone_number = CharField(unique=True)

