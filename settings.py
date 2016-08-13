import os
import logging
import json
from peewee import Model, SqliteDatabase

with open('settings.json', 'r') as myfile:
    json_settings = json.loads(myfile.read())

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

SECRET_KEY = json_settings["SECRET_KEY"]
DEBUG = json_settings["DEBUG"]

#######################
### DATABASE CONFIG ###
#######################
DB_URI = json_settings['DATABASE']
DATABASE = SqliteDatabase(DB_URI, threadlocals=True)

class BaseModel(Model):
    '''
    Base class for all other DB Models
    Basically defines which database to use
    '''
    class Meta:
        database = DATABASE


#######################
### PATHS #############
#######################
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT_DIR, 'static')
TEMPLATES_DIR = os.path.join(ROOT_DIR, 'templates')

