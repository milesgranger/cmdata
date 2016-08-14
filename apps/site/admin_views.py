import glob
import os
import flask_admin

from flask import url_for, redirect
from flask_admin import form, expose
from flask_admin.contrib.peewee import ModelView
from flask_login import current_user
from jinja2 import Markup
from settings import STATIC_DIR
from application import bcrypt


class FlaskAdminView(flask_admin.AdminIndexView):
    '''
    Defines New class for admin view which checks for authorized users
    to access the /admin url
    '''
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('apps.site.views.index'))
        return super(FlaskAdminView, self).index()


class UserAreaView(ModelView):
    '''Admin view for business area'''
    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return ''
        return Markup('<img src="%s">' % url_for('static',
                                                 filename=form.thumbgen_filename(model.image)))

    def _password_formatter(view, context, model, name):
        return '*******'

    def is_accessible(self):
        return True if current_user.is_authenticated else False

    def inaccessible_callback(self, name, **kwargs):
        from flask import redirect, url_for, flash, request
        flash('Sorry, you do not have the permissions to view that page.')
        return redirect(url_for('apps.site.views.index', next=request.url))

    def after_model_delete(self, model):
        '''Used to remove profile images'''
        print 'Removing Business Area photo: {}'.format(model.image)
        f = os.path.splitext(model.image)[0]
        [os.remove(p) for p in glob.glob(os.path.join(STATIC_DIR, f + '*'))]
        return True

    def on_model_change(self, form, model, is_created):
        '''Has the plaintext password'''
        model.password = bcrypt.generate_password_hash(model.password)


    column_formatters = {
        'image': _list_thumbnail,
        'password': _password_formatter

    }

    column_exclude_list = ['password']
    form_excluded_columns = column_exclude_list

    form_extra_fields = {
        'image': form.ImageUploadField(label='Image',
                                       relative_path='images/',
                                       base_path=STATIC_DIR,
                                       thumbnail_size=(150, 150, True)
                                       )
    }



class CMSView(ModelView):
    '''Admin view for business area'''
    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return ''
        return Markup('<img src="%s">' % url_for('static',
                                                 filename=form.thumbgen_filename(model.image)))

    def is_accessible(self):
        return True if current_user.is_authenticated else False

    def inaccessible_callback(self, name, **kwargs):
        from flask import redirect, url_for, flash, request
        flash('Sorry, you do not have the permissions to view that page.')
        return redirect(url_for('apps.site.views.index', next=request.url))

    def after_model_delete(self, model):
        '''Used to remove profile images'''
        print 'Removing Business Area photo: {}'.format(model.image)
        f = os.path.splitext(model.image)[0]
        [os.remove(p) for p in glob.glob(os.path.join(STATIC_DIR, f + '*'))]
        return True


    column_formatters = {
        'image': _list_thumbnail
    }

    form_extra_fields = {
        'image': form.ImageUploadField(label='Image',
                                       relative_path='images/',
                                       base_path=STATIC_DIR,
                                       thumbnail_size=(150, 150, True)
                                       )
    }