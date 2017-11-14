from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from blueprint.produtos import cadastro_produtos, todos_produtos
from blueprint.models.lista_produtos import lista_produto

from models.database import db


def cria_app(config=None):
    app = Flask(__name__)
    if config:
        app.config.from_pyfile(config)

    #db.create_all()
    #from models import db
    db.init_app(app)
    from incluir_produto import User
    #db.create_all()


    #with app.app_context():
    #    db.create_all()


    app.register_blueprint(cadastro_produtos)
    app.register_blueprint(todos_produtos)
    app.register_blueprint(lista_produto)
    return app
#if __name__ == "__main__":
