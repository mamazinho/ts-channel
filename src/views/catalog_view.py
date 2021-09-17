from src.controllers.product_post_controller import ProductPostController
from src.controllers.marketplace_controller import MarketPlaceController
from datetime import datetime


class CatalogView():

    def __init__(self):
        self.pp_controller = ProductPostController()
        self.marketplace_controller = MarketPlaceController()

    def __create_new_post_in_channels(self, catalog_product):
        seller = self.mock_seller_api_read_by_id(catalog_product['seller_id'])
        marketplaces = self.marketplace_controller.read_all()
        for marketplace in marketplaces:
            self.pp_controller.create_product_post(
                marketplace.id, 
                catalog_product['product_catalog_id'], 
                catalog_product['seller_id'], 
                seller['cep']
            )

    # Essa função é chamada pelo time de catalogo, passando o dicionario que esta no README para fazermos o post aqui
    def new_product_created_in_catalog(self, catalog_product):
        self.__create_new_post_in_channels(catalog_product)

    # Essa função é chamada pelo time de catalogo para atualizarmos o status de determinado produto
    def change_product_status_in_catalog(self, product_catalog_id, seller_id, status, marketplace=None):
        conditions = {
            'product_catalog_id': product_catalog_id,
            'seller_id': seller_id
        }
        if marketplace:
            conditions['marketplace_id'] = marketplace

        product_posted = self.pp_controller.read_by_multiple_fields(conditions)
        product_posted.status = status

    # Essa função é chamada por nós para recebermos todos os produtos do catalogo, passando a lista que esta no README para fazermos o post aqui
    def get_products_from_catalog(self):
        all_catalog = self.mock_catalog_api_read_all()
        for product in all_catalog:
            self.__create_new_post_in_channels(product)

    # Função que esta dentro da rota /seller/<id> la com seller, essa aqui só simula os valores que eles retornam
    def mock_seller_api_read_by_id(self, seller_id):
        mock = {
            'id': seller_id,
            'cep': 12345678,
        }
        return mock

    # Função que esta dentro da rota /catalogs/ la com catalogo, essa aqui só simula os valores que eles retornam
    def mock_catalog_api_read_all(self):
        mock = [
            {
                'product_catalog_id': 1,
                'seller_id': 1
            },
            {
                'product_catalog_id': 2,
                'seller_id': 2
            }
        ]
        return mock