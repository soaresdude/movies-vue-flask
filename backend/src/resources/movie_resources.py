from flask_restplus import Resource
from flask import request
from src.models.movie_model import MovieModel
from src.schemas.movie_schema import MovieSchema
from src.api import api

movie_schema = MovieSchema()
movie_list_schema = MovieSchema(many=True)


class MovieResource(Resource):

    @staticmethod
    def get(**kwargs):
        return {'movie': movie_schema.dumo(MovieModel.get_by(**kwargs))}, 200


class MoviesListResource(Resource):

    @staticmethod
    @api.doc(params={'id': 'Movie ID'})
    def get():
        query = dict(request.args)
        if query.get('filter'):
            return {'movies': movie_list_schema.dump(
                MovieModel.get_by(query.get('page'),
                                  **query.get('filter')))},200
        return {'movies': movie_list_schema.dump(
            MovieModel.get_all(query.get('page')))}, 200
