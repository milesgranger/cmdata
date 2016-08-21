
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


class CMS(BaseModel):

    pk = pw.PrimaryKeyField()
    page = pw.CharField(max_length=255,
                        null=False,
                        help_text='Relative path to url. ie. /about, or / for index page')

    place_holder = pw.CharField(max_length=50,
                                null=False,
                                help_text='Unique id relative to this/these element(s); NO SPACES!')
    place_holder_description = pw.CharField(null=True,
                                            max_length=255,
                                            help_text='Description for this placeholder (not shown on site)')

    glyphicon = pw.CharField(null=True, help_text='Bootstrap glyphicon class name if needed')

    title = pw.CharField(null=True, help_text='Any relevant title.')

    text = pw.TextField(null=True,
                        help_text='Raw text/html which will be displayed')
    image = pw.CharField(max_length=255,
                         null=True,
                         help_text='Optional picture')


    def __unicode__(self):
        return u'Page: {}, Placeholder: {}'.format(self.page, self.place_holder)

    def __str__(self):
        return u'Page: {}, Placeholder: {}'.format(self.page, self.place_holder)


class CMSSchema(ModelSchema):
    '''Dumps instance models into json/dict'''
    class Meta:
        model = CMS



