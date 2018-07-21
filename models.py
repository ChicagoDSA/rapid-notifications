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


# TODO: this might make more sense to put in a different file
# helpers
def addGroup(name):
    group = Group(name=name)
    group.save()
    return group.id

def addMember(number):
    member = Member(phone_number=number)
    member.save()
    return member.id

def getAllGroups():
    groups = []
    for group in Group.select():
        group = {"group_name": group.name, "group_id": group.id}
        groups.append(group)

    return groups

def getAllMembers():
    members = []
    for member in Member.select():
        member = {"number": member.phone_number, "member_id": member.id}
        members.append(member)

    return members

## example usage ##
# dummy_member = Member(phone_number="1234567890")
# dummy_member.save()
#
# dummy_group = Group(name="tech working group")
# dummy_group.save()
#
# dummy_membership = GroupMemberShip(group=dummy_group.id, member=dummy_member.id)
# dummy_membership.save()
