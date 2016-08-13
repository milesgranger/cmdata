from apps.site.models import BusinessArea, User
from settings import DATABASE

models = [
    BusinessArea,
    User,
]

def create_tables():
    print 'Building tables...'
    DATABASE.create_tables(models=models,
                           safe=True)
    print 'Tables built for models.'