import os
import json
from flask import Flask
from sgd.gdrive import GoogleDrive

app = Flask(__name__)
tokenFromVar=os.environ.get('TOKEN')
token = json.loads(tokenFromVar)
gdrive = GoogleDrive(token)

from sgd import routes
