import sys
from app import cria_app
app = cria_app(config='settings.py')


app.run()
