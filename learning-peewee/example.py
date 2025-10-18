from database_model import People, Group, Note
from rich import print

deadduck = People(
    name='Dead Duck',
    birth_date=19700101,
    password='asdfyuio',
    email='dead_duck@duck.com'
)

try:
    deadduck.save()
    People.create(
        name='Bob Cuspe',
        birth_date=19890201,
        email='bob@cuspe.com',
        password='12308520948'
    )
except:
    ...

a = People.select().where(People.name == 'Bob Cuspe').get()

print(dir(a))