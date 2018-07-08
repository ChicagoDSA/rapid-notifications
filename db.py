from peewee import *

# TODO make this pg if not local
db = SqliteDatabase('rapid-notifications')

class BaseModel(Model):
    class Meta:
        database = db 

class Group(BaseModel):
    id = UUIDField()
    name = CharField(unique=True)

class Member(BaseModel):
    id = UUIDField()
    phone_number = CharField(unique=True)

db.connect()
db.create_tables([Group, Member])
