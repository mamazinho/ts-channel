from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from config.settings import Settings

class MarketPlaceModel(Settings.Base):

    __tablename__ = 'marketplace'

    id = Column(Integer, primary_key=True)
    name = Column(String)


    def __str__(self):
        return f'{self.id} - {self.name}'
