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
    for i in range(3):
        item = CMS()
        item.page = u'/'
        item.place_holder = u'what_we_do'
        item.title = fake.text(25)
        item.text = fake.paragraph()
        item.save()

    ###############################
    ### Create business areas #####
    ###############################
    print 'Building dashboard intro placeholder...'
    item = CMS()
    item.page = u'/pivot'
    item.place_holder = u'dash_board_intro'
    item.place_holder_description = fake.text(25)
    item.text = fake.paragraph()
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