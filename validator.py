from schema import Schema, And, Use

group_schema = Schema({
    "group": And(str)
    })

members_schema = Schema({
    "numbers": [And(str, Use(str), lambda s: len(s) == 9)]
    })

message_schema = Schema({
    "groups": [And(Use(int), lambda n: n > 0)],
    "message": And(str)
    })
