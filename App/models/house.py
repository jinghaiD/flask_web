from .basemodel import BaseModel
from App.ext import models


class House(BaseModel):

    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    jingdu = models.Column(models.String)
    weidu = models.Column(models.String)
    name = models.Column(models.String)
    province = models.Column(models.String)
    city = models.Column(models.String)
    type = models.Column(models.String)
    guest = models.Column(models.Integer)
    room = models.Column(models.Integer)
    bed = models.Column(models.Integer)
    toilet = models.Column(models.Integer)
    introduction = models.Column(models.String(1000))
    price = models.Column(models.Integer)
    booktime = models.Column(models.Integer)
    owner = models.Column(models.String)
    status = models.Column(models.Integer)

    def __repr__(self):
        return str(self.id)+self.jingdu+self.weidu+self.name+self.province+self.city+self.type+str(self.guest)+str(self.room)+str(self.bed)+str(self.toilet)+str(self.price)+'/'+str(self.booktime)+'/'+str(self.status)

    def __init__(self,jingdu,weidu,name,province,city,type,guest,bed,room,toilet,introduction,price,owner):
        self.jingdu = jingdu
        self.weidu = weidu
        self.name = name
        self.province = province
        self.city = city
        self.type = type
        self.guest = guest
        self.room = room
        self.bed = bed
        self.toilet = toilet
        self.introduction = introduction
        self.price = price
        self.booktime = 0
        self.owner = owner
        self.status = 3