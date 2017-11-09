from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blueprint.produtos import cadastro_produtos, todos_produtos
from blueprint.models.lista_produtos import lista_produto

#from database.db import db
#from app.models import incluir_produto

db=SQLAlchemy()
def cria_app(config=None):
    app = Flask(__name__)
    if config:
        app.config.from_pyfile(config)

    db.init_app(app)
    #db.create_all()
    print(app.config)
    app.register_blueprint(cadastro_produtos)
    app.register_blueprint(todos_produtos)
    app.register_blueprint(lista_produto)
    return app