import time
import os
import glob

import pandas as pd

from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from application import bcrypt
from .models import CMS, CMSSchema, User
from .forms import LoginForm
from flask_login import login_required, login_user, logout_user
from settings import STATIC_DIR


site_blueprint = Blueprint(import_name='site_blueprint',
                           name=__name__,
                           static_folder='apps/site/static',
                           static_url_path='/static/site',
                           template_folder='apps/site/templates')


@site_blueprint.route('/')
def index():
    if request.args.get('json', None):
        jsonDumper = CMSSchema()
        areas = [jsonDumper.dump(area)[0] for area in CMS.select().where(CMS.page==u'/')]
        data = jsonify({'success': True, 'data': {'business_areas': areas}})
        return data
    else:
        return render_template('index.html')



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
