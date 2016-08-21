import os
import glob
from settings import STATIC_DIR
from apps.site.models import CMS, User
from faker import Factory
from application import bcrypt

fake = Factory.create('en_US')

def create_data():

    ################################
    # Remove any pics in images/   #
    ################################
    print 'Removing images...'
    [os.remove(p) for p in glob.glob(os.path.join(STATIC_DIR, 'images/*'))]

    ###############################
    ### Create basic users    #####
    ###############################
    user = User()
    user.first_name = 'Miles'
    user.last_name = 'Granger'
    user.username = 'milesg'
    user.password = bcrypt.generate_password_hash('test')
    user.save()

    user = User()
    user.first_name = 'Chase'
    user.last_name = 'Stoeger'
    user.username = 'chases'
    user.password = bcrypt.generate_password_hash('password')
    user.save()

    ###############################
    ### Create business areas #####
    ###############################
    print 'Building Business Areas...'
    item = CMS()
    item.page = u'/'
    item.place_holder = u'business_area'
    item.place_holder_description = u'Raw html for business area detail description'
    item.title = u'Statistical Modeling & Prediction'
    item.text = u'Information about our statistical knowledge'
    item.glyphicon = u'glyphicon glyphicon-signal'
    item.save()

    item = CMS()
    item.page = u'/'
    item.place_holder = u'business_area'
    item.place_holder_description = u'Raw html for business area detail description'
    item.title = u'Data Management'
    item.text = u'Information about our data management'
    item.glyphicon = u'glyphicon glyphicon-hdd'
    item.save()

    item = CMS()
    item.page = u'/'
    item.place_holder = u'business_area'
    item.place_holder_description = u'Raw html for business area detail description'
    item.title = u'Custom Reporting'
    item.text = u'Information about our custom reporting'
    item.glyphicon = u'glyphicon glyphicon-list-alt'
    item.save()


    return True


def recreate_db():
    '''Recreats DB and also empties static/images/ via create_data above'''
    from settings import DB_URI, ROOT_DIR
    from migrations.m_001_initialize import create_tables

    if os.path.exists(os.path.join(ROOT_DIR, DB_URI)):
        os.remove(os.path.join(ROOT_DIR, DB_URI))
        print '\nRemoved {}\n'.format(DB_URI)
    create_tables()
    create_data()
    return True