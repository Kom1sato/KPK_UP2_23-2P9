from peewee import *

db = SqliteDatabase("campus.db")

class BaseModel(Model):
    class Meta:
        database = db

class Building(BaseModel):
    name = CharField(max_length=100)
    address = CharField(max_length=255)
    floors = IntegerField(constraints=[Check("floors > 0")])
    is_active = BooleanField(default=True)

    class Meta:
        indexes = (
            (("name", "address"), True),
        ) 

def initialize_database():
    db.connect()
    db.create_tables([Building], safe=True)
    db.close()

if __name__ == "__main__":
    initialize_database()
