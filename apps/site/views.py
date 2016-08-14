import time
import os
import glob

import pandas as pd

from flask import Blueprint, render_template, redirect, url_for, request, flash
from application import bcrypt
from .models import CMS, User
from .forms import LoginForm
from flask_login import login_required, login_user, logout_user
from settings import STATIC_DIR


site_blueprint = Blueprint(name=__name__,
                           import_name='site_bluePrint',
                           static_folder='apps/site/static',
                           template_folder='apps/site/templates')


@site_blueprint.route('/')
def index():
    areas = [area for area in CMS.select().where(CMS.page==u'/').limit(5)]
    return render_template('index.html', areas=areas)


@site_blueprint.route('/pivot')
def pivot():
    pathToSampleData = os.path.join(STATIC_DIR, 'data', 'sample_data', '*.csv')
    data = glob.glob(pathToSampleData)
    if not data:
        return 'Sorry, there is not sample data available.'
    df = pd.read_csv(data[0])
    return render_template('pivottablejs.html',
                           data=df.to_dict('records'),
                           place_holders=[p for p in CMS.select().where(CMS.page==u'/pivot')])


@site_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(csrf_enabled=True)
    if form.validate_on_submit():
        try:
            user = User.get(username=form.username.data)
        except:
            flash('Username does not exist.', category='warning')
        else:
            if bcrypt.check_password_hash(user.password, password=form.password.data):
                login_user(user)
                return redirect(url_for('apps.site.views.index'))
            else:
                flash('Incorrect password', category='warning')
    return render_template('login.html', form=form)


@site_blueprint.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('apps.site.views.login'))
