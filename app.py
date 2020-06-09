from flask import Flask
from flask_restful import Api
from PessoaRoute import PessoaRoute, auth
from Autentication import auth
from models import Usuario

app = Flask(__name__)
api = Api(app)


@auth.verify_password
def verification(login, password):
    # Verifica se a senha foi inserida corretamente
    if not (login and password):
        return False
    return Usuario.query.filter_by(login=login, password=password).first()


# USERS = {'rafael': '323', 'galeani': '321'}
# @auth.verify_password
# def verification(login, password):
#     # Verifica se a senha foi inserida corretamente
#     if not (login and password):
#         return False
#
#     return USERS.get(login) == password


# Rotas
api.add_resource(PessoaRoute, '/pessoa/<nome>', '/pessoa/')

if __name__ == '__main__':
    app.run(debug=True)
