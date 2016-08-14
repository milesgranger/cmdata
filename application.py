import os

from flask import Flask
from flask_admin import Admin
from flask_debugtoolbar import DebugToolbarExtension
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CsrfProtect
from settings import ROOT_DIR, DEBUG, DATABASE, SECRET_KEY, STATIC_DIR
from flask_login import LoginManager


app = Flask(__name__, root_path=ROOT_DIR)


###################
### APP CONFIGS ###
###################
app.config['DEBUG'] = DEBUG
app.config['SECRET_KEY'] = SECRET_KEY
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

from flask_admin.contrib.fileadmin import FileAdmin
# The middle arg is the what is appended to the file name relative to STATIC_DIR
# ie. ../static/images/pic.jpg --> localhost:5000/static/images/pic.jpg
# and not localhost:5000/images/pic.jpg
admin.add_view(FileAdmin(STATIC_DIR, '/static/', name='Static Files'))

from apps.site.models import CMS, User
from apps.site.admin_views import CMSView, UserAreaView
admin.add_view(CMSView(CMS, name='Place Holders'))
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

