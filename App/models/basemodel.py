from App.ext import models


class BaseModel(models.Model):
    __abstract__ = True

    id = models.Column(models.Integer, primary_key=True, autoincrement=True)

    def save(self):
        try:
            models.session.add(self)
            models.session.commit()

            return True

        except Exception as e:
            print(e)

            return False

    def delete(self):
        try:
            models.session.delete(self)
            models.session.commit()

            return True

        except Exception as e:
            print(e)

            return False
