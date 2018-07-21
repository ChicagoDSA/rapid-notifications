from schema import Schema, And, Use

group_schema = Schema({
    "group": And(str)
    })

member_schema = Schema({
    "number": And(str, Use(str), lambda s: len(s) == 12)
    })

members_schema = Schema({
    "numbers": [And(str, Use(str), lambda s: len(s) == 12)]
    })

message_schema = Schema({
    "groups": [And(Use(int), lambda n: n > 0)],
    "message": And(str)
    })
