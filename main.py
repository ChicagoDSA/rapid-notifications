from app import app
from models import *

import api

if __name__ == "__main__":
    Group.create_table(True)
    Member.create_table(True)
    app.run()

