from flask import request
from flask_restful import Resource
from models import Pessoa
from Autentication import auth

class PessoaRoute(Resource):
    @auth.login_required
    def get(self, nome=None):
        if nome is None:
            pessoas = Pessoa.query.all()
            response = [{'id': p.id,
                         'nome': p.nome,
                         'idade': p.idade} for p in pessoas]
            return response

        pessoa = Pessoa.query.filter_by(nome=nome).first()
        try:
            response = {
                "nome": pessoa.nome,
                "idade": pessoa.idade,
                "id": pessoa.id
            }
        except AttributeError:
            return {"message": "pessoa não encontrada"}

        return response

    def put(self, nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        body = request.json

        if "nome" in body:
            pessoa.nome = body['nome']
        if "idade" in body:
            pessoa.idade = body['idade']

        pessoa.save()
        response = {
            "nome": pessoa.nome,
            "idade": pessoa.idade,
            "id": pessoa.id
        }
        return response

    def delete(self, nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        response = {'mensagem': '{} excluido'.format(pessoa.nome)}
        pessoa.delete()
        return response

    def post(self, nome=None):
        if nome is not None:
            return {'message': 'endereço errado. Metodo não aceita parametros'}

        body = request.json
        pessoa = Pessoa(nome=body['nome'], idade=body['idade'])
        pessoa.save()
        response = {'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade}
        return response
