from .basemodel import BaseModel
from App.ext import models


class User(BaseModel):

    username = models.Column(models.String)
    password = models.Column(models.String)

    def __repr__(self):
        return str(self.id)+self.username+self.password

    def __init__(self, username, password):
        self.username = username
        self.password = password
