from src.daos.marketplace_dao import MarketPlaceDao

class MarketPlaceController:

    def create_marketplace(self, marketplace_name):
        if type(marketplace_name) == str:
            marketplace = {
                'name': marketplace_name,
            }
            marketplace_id = MarketPlaceDao(marketplace).create()
            return marketplace_id
        raise Exception("Valor Invalido")
        
    def read_all(self):
        products_posted = MarketPlaceDao().read_all()
        return products_posted

    def read_by_id(self, marketplace_id):
        marketplace = {
            'id': marketplace_id
        }
        products_posted = MarketPlaceDao(marketplace).read_by_id()
        return products_posted

    def read_by_name(self, marketplace_name):
        marketplace = {
            'name': marketplace_name
        }
        products_posted = MarketPlaceDao(marketplace).read_by_name()
        return products_posted