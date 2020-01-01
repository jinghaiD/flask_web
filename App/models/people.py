from .basemodel import BaseModel
from App.ext import models


class People(BaseModel):

    name = models.Column(models.String(100))
    age = models.Column(models.Integer)

    def __repr__(self):
        return str(self.id)+self.name+str(self.age)

    def __init__(self, name, age):
        self.name = name
        self.age = age
