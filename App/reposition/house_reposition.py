from App.models.house import House, models


class HouseReposition:

    def select_by_id(self, id):
        house = House.query.filter_by(id=id).first()
        return house

    def select_by_owner(self, owner):
        house = House.query.filter_by(owner=owner).all()
        return house

    def select_by_city(self, city):
        house = House.query.filter_by(city=city, status=0)
        return house[0:10]

    def select_by_status(self, status):
        house = House.query.filter_by(status=status)
        return house

    def sub_add(self, id):
        house = House.query.filter_by(id=id).first()
        house.status = 1
        house.save()
        return

    def sub_finish(self, id):
        house = House.query.filter_by(id=id).first()
        house.status = 0
        house.save()
        return

    def sub_judge(self, id):
        house = House.query.filter_by(id=id).first()
        house.status = 2
        house.save()
        return

    def add_house(self,jingdu,weidu,name,province,city,type,guest,room,bed,toilet,introduction,price,owner):
        house = House(jingdu,weidu,name,province,city,type,guest,room,bed,toilet,introduction,price,owner)
        house.save()
        return

    def search(self,people,room,bed,min,max,city):
        house = House.query.filter(House.price >= min,House.price <= max,House.city == city,House.guest == people,House.room == room,House.bed == bed).all()
        return house

