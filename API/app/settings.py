import os
import pdb
#pdb.set_trace()
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media_files')
DEBUG=True
USE_RELOADER=True
#SQLALCHEMY_DATABASE_URI = 'sqlite://produtos.db'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///database/test.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:////database/test.db'
PORT = 5555
HOST = "127.0.0.1"
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
