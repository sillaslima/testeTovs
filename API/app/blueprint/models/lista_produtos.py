from flask import Blueprint
lista_produto = Blueprint('/lista',__name__)
@lista_produto.route("/lista",methods=['GET','POST'])
def lista():
    return "lista produtos"
