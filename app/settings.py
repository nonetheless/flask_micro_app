import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI ="mysql://root:66166161@localhost:3306/demo?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
