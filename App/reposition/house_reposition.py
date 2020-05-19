from App.models.house import House, models


class HouseReposition:

    def find_first(self):
        house = House.query.first()
        return house

    def select_by_id(self, id):
        house = House.query.filter_by(id=id).first()
        return house