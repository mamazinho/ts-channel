from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class Settings:

    Engine = create_engine('postgresql+psycopg2://olist:olist123@localhost:5433/postgres', echo=False)
    Base = declarative_base()

# Banco + Driver :// User = "Nome do Usuario" Senha @localhost(Porta) = "Porta" / "Nome da Base de Dados"