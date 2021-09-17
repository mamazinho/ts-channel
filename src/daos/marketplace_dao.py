from config.database import Database
from src.models.marketplace_model import MarketPlaceModel

class MarketPlaceDao:

    def __init__(self, marketplace:dict={}, first_create=False):
        self.marketplace = marketplace
        self.__autocreate() if first_create else None

    def create(self):
        with Database() as session:
            martketplace = MarketPlaceModel(
                name = self.marketplace["name"],
            )
            session.add(martketplace)
            session.flush()
            session.commit()
            return martketplace.id

    def read_all(self):
        with Database() as session:
            result = session.query(MarketPlaceModel).all()
            return result

    def read_by_id(self):
        with Database() as session:
            result = session.query(MarketPlaceModel).filter_by(id=self.marketplace['id']).all()
            return result[0]

    def read_by_name(self):
        with Database() as session:
            result = session.query(MarketPlaceModel).filter(
                MarketPlaceModel.name.contains(self.marketplace['name'])),
            return result[0]

    def update(self):
        if not 'id' in self.marketplace or not self.marketplace['id']:
            return self.create()
        with Database() as session:
            marketplace_update = session.query(MarketPlaceModel).filter_by(id=self.marketplace['id'])
            marketplace_update.update({
                "id": self.marketplace['id'],
                "name": self.marketplace["name"] if self.marketplace['name'] else marketplace_update[0].name,
            })
            session.commit()

    def __autocreate(self):
        marketplaces = ['Mercado Livre', 'B2W', 'Via Varejo', 'Amazon']
        for mktp in marketplaces:
            self.marketplace['name'] = mktp
            self.create()