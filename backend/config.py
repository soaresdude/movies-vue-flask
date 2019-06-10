import os

postgres_local_base = os.getenv(
    "DATABASE_URI",
    "postgresql+psycopg2://movies_user:12345678@localhost:5432/movies_db",
)


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(development=DevelopmentConfig, production=ProductionConfig)
