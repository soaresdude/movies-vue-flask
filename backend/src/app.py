import os
from flask import Flask
from flask_cors import CORS
from src.resources.movie_resources import MovieResource, MoviesListResource
from src.db import db
from src.api import api
from src.ma import ma
from config import config_by_name

app = Flask(__name__)
app.config.from_object(config_by_name[os.getenv('FLASK_ENV', 'development')])

CORS(app)
db.init_app(app)
with app.app_context():
    db.create_all()
api.init_app(app)
ma.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


api.add_resource(MovieResource,
                 '/movie/<int:id>',
                 endpoint='movie_endpoint')

api.add_resource(MoviesListResource, '/movies', endpoint='movies_endpoint')
