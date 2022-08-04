from app.dao.model.director import Director

class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        """ Возврат директоров по id """
        return self.session.query(Director).get(did)

    def get_all(self):
        """ Возврат всех записей директоров """
        return self.session.query(Director).all()
