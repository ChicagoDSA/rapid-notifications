import json
import peewee
from flask import Flask
from flask import request

import models
from app import app
from validator import group_schema, member_schema, members_schema, message_schema

@app.route("/")
def entry_point():
    return "NOT IMPLEMENTED", 501


"""
returns: 200 with JSON in format
{"status": "OK", "groups": [{"group_name": "", "group_id": 1}, ...]}
"""
@app.route("/groups", methods=["GET"])
def get_groups():
    groups = models.getAllGroups()
    return json.dumps({"status": "OK", "groups": groups})


"""
accepts: JSON data in format {group: "group name"}
returns: 200 with JSON in format {"status": "OK", "group_id": 1}
"""
@app.route("/groups", methods=["POST"])
def post_group():
    group_req = request.json
    valid = group_schema.is_valid(group_req)
    if valid:
        try:
            group_id = models.addGroup(group_req["group"])
            return json.dumps({"status": "OK", "group_id": group_id})
        except peewee.IntegrityError:
            return json.dumps({"status": "ERROR", "msg": "Name Already Used"}), 400
    else:
        return json.dumps({"status": "ERROR", "msg": "Data malformed"}), 400


"""
accepts: JSON data in format {ids: [1,2,3,...]}
returns: 200 with JSON in format
{"status": "OK"}
should delete groups from group
"""
@app.route("/groups", methods=["DELETE"])
def delete_group():
    return "NOT IMPLEMENTED", 501


"""
accepts: JSON data in format {group: "group name"}
returns: 200 with JSON in format {"status": "OK", "group_id": 1}
"""
@app.route("/groups/<int:group_id>", methods=["PUT"])
def update_group():
    return "NOT IMPLEMENTED", 501


"""
accepts: JSON data in format {ids: [1,2,3,...]}
params:  group_id
returns: 200 with JSON in format {"status": "OK"}
"""
@app.route("/groups/<int:group_id>", methods=["POST"])
def add_member_to_group(group_id):
    return "NOT IMPLEMENTED", 501


"""
accepts: JSON data in format {ids: [1,2,3,...]}
returns: 200 with JSON in format
{"status": "OK"}
should delete member from group
"""
@app.route("/groups/<int:group_id>", methods=["DELETE"])
def remove_member_from_group():
    return "NOT IMPLEMENTED", 501


"""
returns: 200 with JSON in format
{"status": "OK", "groups": [{"number": "", "member_id": 1}, ...]}
"""
@app.route("/members", methods=["GET"])
def get_members():
    members = models.getAllMembers()
    return json.dumps({"status": "OK", "members": members})


"""
accepts: JSON data in format {number: "+17735555555"}
returns: 200 with JSON in format {"status": "OK", "member_id": 1}
"""
@app.route("/members", methods=["POST"])
def post_member():
    member_req = request.json
    valid = member_schema.is_valid(member_req)
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
def update_member():
    return "NOT IMPLEMENTED", 501


"""
returns: 200 with JSON in format
{"status": "OK"}
"""
@app.route("/members/<int:member_id>", methods=["DELETE"])
def delete_member():
    return "NOT IMPLEMENTED", 501


"""
accepts: JSON data in format {groups: [ids], message: "text"}
params:  group_id
returns: 200 with JSON in format {"status": "OK"}
"""
@app.route("/send", methods=["POST"])
def send():
    return "NOT IMPLEMENTED", 501

