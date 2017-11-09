from flask import Blueprint
cadastro_produtos = Blueprint('produtos',__name__)
todos_produtos = Blueprint('/',__name__)

@cadastro_produtos.route("/produtos/cadastro", methods=['GET','POST'])
def cadastro_produto():
    return "cadastro de produtos"

@todos_produtos.route("/", methods=['GET','POST'])
def index():
    return "todos produtos"
