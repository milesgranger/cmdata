import os

from flask import Flask
from flask_admin import Admin
from flask_debugtoolbar import DebugToolbarExtension
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CsrfProtect
from settings import ROOT_DIR, DEBUG, DATABASE
from flask_login import LoginManager


app = Flask(__name__, root_path=ROOT_DIR)


###################
### APP CONFIGS ###
###################
app.config['DEBUG'] = DEBUG
app.config['SECRET_KEY'] = 'kAanV1owk^21dT23^$#@know./%*'
app.config['DEBUG_TB_PROFILER_ENABLED'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


###################
## BCRYPT & CSRF ##
###################
bcrypt = Bcrypt(app)
CsrfProtect(app)

###################
## DEBUG TOOLBAR ##
###################
toolbar = DebugToolbarExtension(app) if DEBUG else None


###################
##### LOGIN #######
###################
login_manager = LoginManager(app)
login_manager.login_view = 'apps.site.views.login'
login_manager.login_message = u'You must be logged in to view this page.'
login_manager.login_message_category = 'info'

# Login callback
@login_manager.user_loader
def load_user(user_id):
    try:
        return User.get(pk=user_id)
    except Exception as exc:
        return None


###################
##### ADMIN #######
###################
from apps.site.admin_views import FlaskAdminView
admin = Admin(app, name='C&M Data Solutions', index_view=FlaskAdminView(), template_mode='bootstrap3')

from apps.site.models import BusinessArea, User
from apps.site.admin_views import BusinessAreaView, UserAreaView
admin.add_view(BusinessAreaView(BusinessArea, name='Business Areas'))
admin.add_view(UserAreaView(User, name='Users'))


###################
##### ROUTES ######
###################
# /, /login, /logout, /register /about /contact
from apps.site.views import site_blueprint
app.register_blueprint(site_blueprint)


###################
#### App signals ##
###################
@app.before_request
def before_request():
    DATABASE.connect()


@app.teardown_request # Executes even if error occurred during request
def after_request(exc):
    if not DATABASE.is_closed():
        DATABASE.close()


@app.before_first_request
def create_tables():
    from settings import DB_URI
    from utils.create_data import create_data
    from migrations.m_001_initialize import create_tables
    re_create_tables = DEBUG
    if re_create_tables:
        if os.path.exists(os.path.join(ROOT_DIR, DB_URI)):
            os.remove(os.path.join(ROOT_DIR, DB_URI))
            print '\nRemoved {}\n'.format(DB_URI)
        create_tables()
        create_data()
    return True