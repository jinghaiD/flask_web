from .basemodel import BaseModel
from App.ext import models


class History(BaseModel):

    username = models.Column(models.String)
    houseid = models.Column(models.Integer)
    times = models.Column(models.Integer)

    def __repr__(self):
        return str(self.houseid)+self.username+str(self.times)

    def __init__(self, username, houseid):
        self.houseid = houseid
        self.username = username
        self.times = 1