from apps.site.models import BusinessArea, User
from settings import DATABASE

tables = [
    BusinessArea,
    User,
]

def create_tables():
    print 'Building tables...'
    DATABASE.create_tables(models=tables,
                           safe=True)
    print 'Tables built for models.'