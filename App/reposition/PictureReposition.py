from App.models.picture import Picture, models


class PictureReposition:

    def select_pics(self, houseid):
        pictures = Picture.query.filter_by(houseid=houseid).all()
        if len(pictures) >= 10:
            return pictures[0:10]
        else:
            return pictures