from peewee import (
    Model, SqliteDatabase, TextField, ForeignKeyField, DateTimeField, IntegerField
)
from datetime import datetime

db = SqliteDatabase('mydatabase.db')


class BaseModel(Model):
    
    class Meta:
        database = db


class People(BaseModel):
    name = TextField()
    email = TextField(unique=True)
    password = TextField()
    birth_date = IntegerField()


class Group(BaseModel):
    name = TextField()
    owner = ForeignKeyField(People, backref='groups')


class Note(BaseModel):
    owner = ForeignKeyField(People, backref='notes')
    group = ForeignKeyField(Group, backref='notes', null=True, default=None)
    title = TextField()
    note = TextField()
    created = DateTimeField(default=datetime.now())
    modified = DateTimeField()
    

# People.create_table()
db.create_tables([People, Group, Note])