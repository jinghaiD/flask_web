from .basemodel import BaseModel
from App.ext import models


class Sub(BaseModel):

    username = models.Column(models.String)
    houseid = models.Column(models.Integer)

    def __repr__(self):
        return str(self.houseid)+self.username

    def __init__(self, username, houseid):
        self.username = username
        self.houseid = houseid