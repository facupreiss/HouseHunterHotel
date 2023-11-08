import os


class Config:
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.abspath(
      'basededatos/mi_bd.db')


class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
