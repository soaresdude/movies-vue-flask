from marshmallow import fields
from src.ma import ma
from src.models.movie_model import MovieModel


class MovieSchema(ma.ModelSchema):
    imdb_score = fields.Decimal()
    aspect_ratio = fields.Decimal()

    class Meta:
        model = MovieModel
        fields = (
            "id",
            "color",
            "director_name",
            "num_critic_for_reviews",
            "duration",
            "director_facebook_likes",
            "actor_3_facebook_likes",
            "actor_2_name",
            "actor_1_facebook_likes",
            "gross",
            "genres",
            "actor_1_name",
            "movie_title",
            "num_voted_users",
            "cast_total_facebook_likes",
            "actor_3_name",
            "facenumber_in_poster",
            "plot_keywords",
            "movie_imdb_link",
            "num_user_for_reviews",
            "language",
            "country",
            "content_rating",
            "budget",
            "title_year",
            "actor_2_facebook_likes",
            "movie_facebook_likes",
        )