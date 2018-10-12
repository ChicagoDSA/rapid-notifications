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

def updateGroup(_id, name):
    q = Group.update({Group.name: name}).where(Group.id == _id)
    rows = q.execute()
    return rows

def deleteGroup(_id):
    q = Group.delete().where(Group.id == _id)
    return q.execute()

def getAllGroups():
    groups = []
    for group in Group.select():
        group = {"group_name": group.name, "group_id": group.id}
        groups.append(group)

    return groups

def addMember(number):
    member = Member(phone_number=number)
    member.save()
    return member.id

def updateMember(_id, number):
    q = Member.update({Member.phone_number: number}).where(Member.id == _id)
    rows = q.execute()
    return rows

def deleteMember(_id):
    q = Member.delete().where(Member.id == _id)
    return q.execute()

def getAllMembers():
    members = []
    for member in Member.select():
        member = {"number": member.phone_number, "member_id": member.id}
        members.append(member)

    return members

def addMemberToGroup(member_id, group_id):
    gms = GroupMemberShip(group = group_id, member = member_id)
    gms.save()
    return gms.id

def removeMemberFromGroup(member_id, group_id):
    gms = GroupMemberShip.delete().where(Group.id == group_id, Member.id == member_id)
    return gms.execute()

## example usage ##
# dummy_member = Member(phone_number="1234567890")
# dummy_member.save()
#
# dummy_group = Group(name="tech working group")
# dummy_group.save()
#
# dummy_membership = GroupMemberShip(group=dummy_group.id, member=dummy_member.id)
# dummy_membership.save()
