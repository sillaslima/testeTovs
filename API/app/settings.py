import os
import pdb
#pdb.set_trace()
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media_files')
DEBUG=True
USE_RELOADER=True
SQLALCHEMY_DATABASE_URI = 'sqlite://produtos.db'