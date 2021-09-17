from src.controllers.shipping_history_controller import ShippingHistoryController
from datetime import datetime


class ShippingView():

    def __init__(self):
        self.shipping_history_controller = ShippingHistoryController()

    def get_ship(self, buyer_cep, products, product_post_id):
        shipping_id = self.shipping_history_controller.create(product_post_id)
        # Chama API de logistica para calculo de frete: /ship, quando realmente tiver rotas, o request deveria ser verificado
        # para fazer ou não o update da linha 15
        ship_infos = self.mock_logistic_api_calculate_ship(buyer_cep, products)
        if 'error' in ship_infos and ship_infos['error']:
            return ship_infos['error']
        else:
            self.shipping_history_controller.update(shipping_id)
            return ship_infos

    # Função que esta dentro da rota /ship la com logistica, essa aqui só simula os valores que eles retornam
    def mock_logistic_api_calculate_ship(self, buyer_cep, products):
        for prod in products:
            prod['frete'] = 10

        mock = {
            'endereco':'rua joao',
            'cep': buyer_cep,
            'products': products,
            'frete': 5
        }
        return mock
