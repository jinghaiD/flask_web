from App.models.history import History, models


class HistoryReposition:

    def create(self, username, houseid):
        history = History.query.filter_by(username=username, houseid=houseid).first()
        if history is None:
            new_history = History(username, houseid)
            new_history.save()
        else:
            print(history)
            history.times += 1
            print(history)
            history.save()
        return


    def select_history(self, username):
        history = History.query.filter_by(username=username).all()
        return history
