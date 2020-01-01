from App.models.basemodel import models


def drop_all():
    models.drop_all()
    return "drop_all success"


def create_all():
    models.create_all()
    return "create_all success"
