from App.models.people import People, models


class PeopleReposition:

    def delete_by_name(self, name):
        people = People.query.filter_by(name=name).first()
        people.delete()
        return 'delete success'

    def change_by_name(self, name):
        people = People.query.filter_by(name=name).first()
        people.name = 'changed_name'
        people.save()
        return 'change success'

    def create(self, name, age):
        people = People(name, age)
        people.save()
        return 'create success'

    def create_all(self, peoples):
        for everyone in peoples:
            people = People(everyone.name, everyone.age)
            peoples.append(people)
        models.session.add_all(peoples)
        models.session.commit()
        return "add_all success"


'''
Model.query.get(id)   BaseQuery  None
.first()  BaseQuery 404  放在最后
.all()   list   404  放在最后
.filter(模型.属性.__eq__(魔术方法 e.g.__lt__)(匹配值))  BaseQuery
       __str__输出的是这个对象数据的SQL
.filter(模型.属性 >/==/<（其实就是调用了魔术方法） 匹配值)
.filter(模型.属性.contains/in/startswith/endwith("匹配值"))
.filter_by()用在级联数据上 条件语法精准，字段=值 
.offset()跳过   .limit()限制 不区分顺序
.order_by()排序  必须先调用
.filter(and_()/or_()/not_(),...)
'''
