from flask_restplus import Resource
from flask import request
from src.models.movie_model import MovieModel
from src.schemas.movie_schema import MovieSchema
import ast

movie_schema = MovieSchema()
movie_list_schema = MovieSchema(many=True)


class MovieResource(Resource):
    @staticmethod
    def get(movie_id):
        return {"movie": movie_schema.dump(MovieModel.get_one(movie_id))}, 200


class MoviesListResource(Resource):
    @staticmethod
    def get():
        query = dict(request.args)

        if query.get("filter"):
            filter_query = ast.literal_eval(query.get("filter"))
            if filter_query.get("movie_title"):
                return (
                    {
                        "movies": movie_list_schema.dump(
                            MovieModel.get_by_title(
                                title=filter_query.get("movie_title")
                            )
                        )
                    },
                    200,
                )
            elif filter_query:
                return (
                    {
                        "movies": movie_list_schema.dump(
                            MovieModel.get_by(query.get("page"), **filter_query)
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


class MoviesNamesResource(Resource):
    @staticmethod
    def get():
        return {"names": MovieModel.get_movies_names()}, 200
