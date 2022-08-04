from flask_restx import Resource, Namespace

from app.container import genre_dao, genre_service
from app.dao.genre import GenreDAO
from app.dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid: int):
        try:
            genre = genre_service.get_one(gid)
            return genre_schema.dump(genre), 200
        except Exception:
            return "", 404
