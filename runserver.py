import os
from migrations.m_001_initialize import create_tables
from utils.create_data import create_data
from application import app
from settings import ROOT_DIR


if __name__ == '__main__':

    re_create_tables = True
    if re_create_tables:
        if os.path.exists(os.path.join(ROOT_DIR, 'dev.db')):
            os.remove(os.path.join(ROOT_DIR, 'dev.db'))
            print '\nRemoved dev.db\n'

        create_tables()
        create_data()

    app.run()