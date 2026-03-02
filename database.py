from flask_login import UserMixin
from requests import Session
from sqlalchemy import create_engine, String, Integer, func, Column, DateTime, Numeric, Date
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash

# banco
engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/empresa_db')

db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


Base.query = db_session.query_property()
local_session = Session


class Funcionario(Base, UserMixin):
    __tablename__ = 'funcionarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(70), nullable=False)
    data_nascimento = Column(DateTime, nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    email = Column(String(120), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    cargo = Column(String(50), nullable=False)
    salario = Column(Numeric(10, 2), nullable=False)
    criado_em = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Funcionario(nome='{self.nome}', cargo='{self.cargo}')>"


    def set_password(self,password):
        self.senha = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.senha,password)

    def save(self, db_session):
        try:
            db_session.add(self)
            db_session.commit()
        except SQLAlchemyError:
            db_session.rollback()
            raise