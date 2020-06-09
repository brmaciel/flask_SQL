from models import Pessoa, Atividade, Usuario

# Insere dados na tabela pessoa
def insere_pessoa():
    pessoa = Pessoa(nome='Galeani', idade=25)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela pessoa
def consulta_pessoa():
    pessoas = Pessoa.query.all()
    print(pessoas)
    pessoa = Pessoa.query.filter_by(nome='Rafael').first()
    print(pessoa)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoa.query.filter_by(nome='Galeani').first()
    pessoa.idade = 21
    pessoa.save()

# Exclui dados na tabela pessoa
def deleta_pessoa():
    pessoa = Pessoa.query.filter_by(nome='Galeani').first()
    pessoa.delete()


def consulta_usuario():
    usuarios = Usuario.query.all()
    print(usuarios)

def insere_usuario(login, senha):
    usuario = Usuario(login=login, password=senha)
    usuario.save()


if __name__ == '__main__':
    # insere_pessoa()
    #altera_pessoa()
    # consulta_pessoa()
    # deleta_pessoa()
    # consulta_pessoa()
    #insere_usuario('rafael', '123')
    #insere_usuario('admin', 'admin')
    consulta_usuario()
