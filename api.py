import json
from flask import Flask
from flask import request

from app import app
from validator import group_schema, members_schema, message_schema

@app.route("/")
def hello():
    return "Hello World!"


"""
accepts: JSON data in format {group: "group name"}
returns: 200 with JSON in format {"group_id": 1}
"""
@app.route("/groups", methods=["POST"])
def group():
    group_req = request.json
    valid = group_schema.is_valid(group_req)
    if valid:
        return json.dumps({"group_id": 1})
    else:
        return "BAD DATA"

"""
accepts: JSON data in format {numbers: ["+11234567"]}
params:  group_id
returns: 200 with JSON in format {"status": "OK"}
"""
@app.route("/groups/<int:group_id>", methods=["POST"])
def member(group_id):
    member_req = request.json
    valid = members_schema.is_valid(member_req)
    if valid:
        return json.dumps({"status": "OK"})
    else:
        return "BAD DATA"

"""
accepts: JSON data in format {groups: [ids], message: "text"}
params:  group_id
returns: 200 with JSON in format {"status": "OK"}
"""
@app.route("/send", methods=["POST"])
def send():
    message_req = request.json
    valid = message_schema.is_valid(message_req)
    if valid:
        return json.dumps({"status": "OK"})
    else:
        return "BAD DATA"

