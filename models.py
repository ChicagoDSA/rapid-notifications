from peewee import *
from app import db


class BaseModel(Model):
    class Meta:
        database = db

class Group(BaseModel):
    name = CharField(unique=True)

class Member(BaseModel):
    phone_number = CharField(unique=True)

class GroupMemberShip(BaseModel):
    group = ForeignKeyField(Group, backref='group')
    member = ForeignKeyField(Member, backref='member')
    class Meta:
        indexes = (
                # Specify a unique multi-column index on from/to-user.
                (('group', 'member'), True),
            )

## example usage ##
# dummy_member = Member(phone_number="1234567890")
# dummy_member.save()
#
# dummy_group = Group(name="tech working group")
# dummy_group.save()
#
# dummy_membership = GroupMemberShip(group=dummy_group.id, member=dummy_member.id)
# dummy_membership.save()
