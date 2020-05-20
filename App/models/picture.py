from .basemodel import BaseModel
from App.ext import models


class Picture(BaseModel):

    houseid = models.Column(models.Integer)
    picture = models.Column(models.String)

    def __repr__(self):
        return str(self.houseid)+self.picture

    def __init__(self, houseid, picture):
        self.houseid = houseid
        self.picture = picture