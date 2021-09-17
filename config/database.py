from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config.settings import Settings


class Database:

    def __enter__(self):
        base = Settings.Base
        engine = Settings.Engine
        base.metadata.create_all(engine, checkfirst=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.close()