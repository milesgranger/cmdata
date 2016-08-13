
import peewee as pw
from settings import BaseModel
from marshmallow_peewee import ModelSchema
from flask_login import UserMixin


class User(BaseModel, UserMixin):

    pk = pw.PrimaryKeyField()
    username = pw.CharField(max_length=100)
    first_name = pw.CharField(max_length=150)
    last_name = pw.CharField(max_length=150)
    password = pw.CharField(max_length=100)
    image = pw.CharField(null=True, max_length=200)

    def is_active(self):
        '''Do checks here if needed to ensure user is still active on site'''
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_id(self):
        return self.pk

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username


class UserSchema(ModelSchema):
    '''Dumps instance models into json/dict'''
    class Meta:
        model = User


class BusinessArea(BaseModel):

    pk = pw.PrimaryKeyField()
    title = pw.CharField(max_length=255)
    introduction = pw.TextField()
    image = pw.CharField(max_length=255, null=True)


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class BusinessAreaSchema(ModelSchema):
    '''Dumps instance models into json/dict'''
    class Meta:
        model = BusinessArea



