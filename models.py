from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Configura o Banco de Dados
engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


# Define as Classes baseadas na estrutura do banco de dados
class Pessoa(Base):
    __tablename__ = 'Pessoa'  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)  # index deixa a consulta mais rapida quando consultar pelo nome
    idade = Column(Integer)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def __repr__(self):
        return '<Pessoa {}, {} anos>'.format(self.nome, self.idade)


class Atividade(Base):
    __tablename__ = 'Atividade'

    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    pessoa_id = Column(Integer, ForeignKey('Pessoa.id'))
    pessoa = relationship('Pessoa')

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def __repr__(self):
        return '<Atividade {}>'.format(self.nome)


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    password = Column(String(20))

    def __repr__(self):
        return '<Usuario {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


# Cria o banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
