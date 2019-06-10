from flask_restplus import Resource
from flask import request
from src.models.movie_model import MovieModel
from src.schemas.movie_schema import MovieSchema
from src.api import api

movie_schema = MovieSchema()
movie_list_schema = MovieSchema(many=True)


class MovieResource(Resource):
    @staticmethod
    @api.doc(params={"id": "Movie Id"})
    def get(movie_id):
        return {"movie": movie_schema.dump(MovieModel.get_one(movie_id))}, 200


class MoviesListResource(Resource):
    @staticmethod
    def get():
        query = dict(request.args)
        if query.get("filter"):
            return (
                {
                    "movies": movie_list_schema.dump(
                        MovieModel.get_by(query.get("page"), **query.get("filter"))
                    )
                },
                200,
            )
        return (
            {
                "movies": movie_list_schema.dump(
                    MovieModel.get_all(query.get("page", 1))
                )
            },
            200,
        )
