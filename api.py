import json
import peewee
from flask import Flask
from flask import request

import models
import validator as val
from app import app

@app.route("/")
def entry_point():
    return "NOT IMPLEMENTED", 501


"""
returns: 200 with JSON in format
{"status": "OK", "groups": [{"group_name": "", "group_id": 1}, ...]}
"""
@app.route("/groups", methods=["GET"])
def get_groups():
    try:
        groups = models.getAllGroups()
        return json.dumps({"status": "OK", "groups": groups})
    except:
        return json.dumps({"status": "ERROR", "msg": "Unknown Error"}), 500

"""
accepts: JSON data in format {group: "group name"}
returns: 200 with JSON in format {"status": "OK", "group_id": 1}
"""
@app.route("/groups", methods=["POST"])
def post_group():
    group_req = request.json
    valid = val.group_schema.is_valid(group_req)
    if valid:
        try:
            group_id = models.addGroup(group_req["group"])
            return json.dumps({"status": "OK", "group_id": group_id})
        except peewee.IntegrityError:
            return json.dumps({"status": "ERROR", "msg": "Name Already Used"}), 400
    else:
        return json.dumps({"status": "ERROR", "msg": "Data malformed"}), 400


"""
accepts: JSON data in format {group: "group name"}
returns: 200 with JSON in format {"status": "OK", "group_id": 1}
"""
@app.route("/groups/<int:group_id>", methods=["PUT"])
def update_group(group_id):
    group_req = request.json
    valid = val.group_schema.is_valid(group_req)
    if valid:
        try:
            rows = models.updateGroup(group_id, group_req["group"])
            return json.dumps({"status": "OK", "updated": rows})
        except:
            return json.dumps({"status": "ERROR", "msg": "Unknown Error"}), 500
    else:
        return json.dumps({"status": "ERROR", "msg": "Data malformed"}), 400


"""
returns: 200 with JSON in format
{"status": "OK"}
should delete a group
"""
@app.route("/groups/<int:group_id>", methods=["DELETE"])
def delete_group(group_id):
    try:
        del_res = models.deleteGroup(group_id)
        return json.dumps({"status": "OK"})
    except:
        return json.dumps({"status": "ERROR", "msg": "Unknown Error"}), 500


"""
accepts: JSON data in format {"member_id": 1}
params:  group_id
returns: 200 with JSON in format {"status": "OK", "membership_id": 1}
"""
@app.route("/groups/<int:group_id>", methods=["POST"])
def add_member_to_group(group_id):
    membership_req = request.json
    valid = val.membership_schema.is_valid(membership)
    try:
        membership_id = models.deleteGroup(group_id, membership_req["membership_id"])
        return json.dumps({"status": "OK", "membership_id": membership_id})
    except:
        return json.dumps({"status": "ERROR", "msg": "Unknown Error"}), 500

"""
returns: 200 with JSON in format
{"status": "OK", "groups": [{"group_name": "", "group_id": 1}, ...]}
"""
@app.route("/groups/<int:group_id>", methods=["GET"])
def get_group_members(group_id):
    return "NOT IMPLEMENTED", 501


"""
returns: 200 with JSON in format
{"status": "OK"}
should delete member from group
"""
@app.route("/groups/<int:group_id>/<int:member_id>", methods=["DELETE"])
def remove_member_from_group(group_id, member_id):
    try:
        del_res = models.removeMemberFromGroup(member_id, group_id)
        return json.dumps({"status": "OK"})
    except:
        return json.dumps({"status": "ERROR", "msg": "Unknown Error"}), 500


"""
returns: 200 with JSON in format
{"status": "OK", "groups": [{"number": "", "member_id": 1}, ...]}
"""
@app.route("/members", methods=["GET"])
def get_members():
    try:
        members = models.getAllMembers()
        return json.dumps({"status": "OK", "members": members})
    except:
        return json.dumps({"status": "ERROR", "msg": "Unknown Error"}), 500


"""
accepts: JSON data in format {number: "+17735555555"}
returns: 200 with JSON in format {"status": "OK", "member_id": 1}
"""
@app.route("/members", methods=["POST"])
def post_member():
    member_req = request.json
    valid = val.member_schema.is_valid(member_req)
    if valid:
        try:
            member_id = models.addMember(member_req["number"])
            return json.dumps({"status": "OK", "member_id": member_id})
        except peewee.IntegrityError:
            return json.dumps({"status": "ERROR", "msg": "Number Already Used"}), 400
    else:
        return json.dumps({"status": "ERROR", "msg": "Data malformed"}), 400


"""
accepts: JSON data in format {number: "number"}
returns: 200 with JSON in format {"status": "OK"}
"""
@app.route("/members/<int:member_id>", methods=["PUT"])
def update_member(member_id):
    member_req = request.json
    valid = val.member_schema.is_valid(member_req)
    if valid:
        try:
            rows = models.updateMember(member_id, member_req["number"])
            return json.dumps({"status": "OK", "updated": rows})
        except:
            return json.dumps({"status": "ERROR", "msg": "Unknown Error"}), 500
    else:
        return json.dumps({"status": "ERROR", "msg": "Data malformed"}), 400


"""
returns: 200 with JSON in format
{"status": "OK"}
"""
@app.route("/members/<int:member_id>", methods=["DELETE"])
def delete_member(member_id):
    try:
        del_res = models.deleteMember(member_id)
        return json.dumps({"status": "OK"})
    except:
        return json.dumps({"status": "ERROR", "msg": "Unknown Error"}), 500


"""
accepts: JSON data in format {groups: [ids], message: "text"}
params:  group_id
returns: 200 with JSON in format {"status": "OK"}
"""
@app.route("/send", methods=["POST"])
def send():
    return "NOT IMPLEMENTED", 501

