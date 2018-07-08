# TODO make this pg if not local
database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database

class Group(BaseModel):
    id = UUIDField()
    name = CharField(unique=True)

class Member(BaseModel):
    id = UUIDField()
    phone_number = CharField(unique=True)

db.connect()
db.create_tables([Group, Member])
