from src.db import db
from typing import List


class MovieModel(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color = db.Column(db.String(16))
    director_name = db.Column(db.String(32))
    num_critic_for_reviews = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    director_facebook_likes = db.Column(db.Integer)
    actor_3_facebook_likes = db.Column(db.Integer)
    actor_2_name = db.Column(db.String(28))
    actor_1_facebook_likes = db.Column(db.Integer)
    gross = db.Column(db.Integer)
    genres = db.Column(db.String(64), nullable=False)
    actor_1_name = db.Column(db.String(27))
    movie_title = db.Column(db.String(87), nullable=False)
    num_voted_users = db.Column(db.Integer, nullable=False)
    cast_total_facebook_likes = db.Column(db.Integer, nullable=False)
    actor_3_name = db.Column(db.String(29))
    facenumber_in_poster = db.Column(db.Integer)
    plot_keywords = db.Column(db.String(149))
    movie_imdb_link = db.Column(db.String(52), nullable=False)
    num_user_for_reviews = db.Column(db.Integer)
    language = db.Column(db.String(10))
    country = db.Column(db.String(20))
    content_rating = db.Column(db.String(9))
    budget = db.Column(db.BigInteger)
    title_year = db.Column(db.Integer)
    actor_2_facebook_likes = db.Column(db.Integer)
    imdb_score = db.Column(db.Numeric(3, 1), nullable=False)
    aspect_ratio = db.Column(db.Numeric(4, 2))
    movie_facebook_likes = db.Column(db.Integer, nullable=False)

    @classmethod
    def get_all(cls, page=1):
        return cls.query.paginate(page, 50, False).items

    @classmethod
    def get_by(cls, page=1, **kwargs) -> List['MovieModel']:
        print('query: ', kwargs)
        return cls.query.filter_by(**kwargs).paginate(page, 50, False).items

    @classmethod
    def get_one(cls, query) -> 'MovieModel':
        return cls.query.filter_by(query).first()

    def __repr__(self):
        return f'<Movie {self.movie_title}>'
