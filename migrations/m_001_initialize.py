from apps.site.models import CMS, User
from settings import DATABASE

models = [
    CMS,
    User,
]

def create_tables():
    print 'Building tables...'
    DATABASE.create_tables(models=models,
                           safe=True)
    print 'Tables built for models.'