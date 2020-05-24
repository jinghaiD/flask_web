from App.models.sub import Sub, models


class SubReposition:

    def create(self, username, houseid):
        sub = Sub.query.filter_by(username=username, houseid=houseid).first()
        if sub is None:
            sub = Sub(username,houseid)
            sub.save()
        return

    def finish(self,username, houseid):
        sub = Sub.query.filter_by(username=username, houseid=houseid).first()
        sub.delete()
        return

    def select_sub(self, username):
        sub = Sub.query.filter_by(username=username).all()
        return sub