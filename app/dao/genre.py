from app.dao.model.genre import Genre

class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        """ Возврат жанров по id """
        return self.session.query(Genre).filter(Genre.id == gid).one()

    def get_all(self):
        """ Возврат всех жанров """
        return self.session.query(Genre).all()
