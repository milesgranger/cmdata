from application import app
from utils.create_data import recreate_db

if __name__ == '__main__':
    recreate_db()
    app.run()