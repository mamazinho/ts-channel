from .catalog_view import CatalogView
from .order_view import OrderView
from .shipping_view import ShippingView
from src.controllers.product_post_controller import ProductPostController

from datetime import datetime

class ChannelView():

    def __init__(self):
        self.catalog_view = CatalogView()
        self.order_view = OrderView()
        self.shipping_view = ShippingView()
        self.product_controller = ProductPostController()

    def simulate_buyer_buy_product(self, product_post_ids=[]):
        order = {
            'buyer': {
                'cpf': 12121234556,
                'email': 'teste@test.com',
                'cep': 12345678,
                'name': 'Teste',
                'number' : 11,
                'street' : 'rua do bobo 2',
                'district' : 'distrito 18',
                'city' : 'lugar nenhum 2',
                'state' : 'Oioioi 2',
            },
            'products': [],
            'shipping': ''
        }
        product = ProductModel(products)
        channel_products = [ self.product_controller.read_by_id(post_id) for post_id in product_post_ids ]
        for channel_product in channel_products:
            product = self.simulate_api_get_product_by_id(channel_product.product_catalog_id) ## retorna ID do produto
            
            products = {
                'product_catalog_id': channel_product.product_catalog_id,
                'seller_id': channel_product.seller_id,
                'quantity': 5,
                'price': product.price,
                'width': 5, # product.width
                'lenth': 5, # product.lenth
                'height': 5, # product.height
                'weight': 5, # product.weight
                'volume': 5,
            }
            order['products'].append(products)

        shipping_price = self.simulate_buyer_get_shipping(order['buyer']['cep'], order['products'], product_post_ids[0])
        order['shipping'] = shipping_price
        channel_order_history = self.order_view.create_order_history(order, product_post_ids[0])
        print('GERADA ORDEM: ', channel_order_history)

    def simulate_api_get_catalog_by_product_catalog_id(catalog_product_id):
        catalog = Catalog()
        catalog.id = 2

    def simulate_api_get_product_by_id(self, product_id):
        product = ProductModel()
        product.id = 1
        product.width = 200
        product.lenth = 100
        product.height = 80
        product.weight = 180
        if product_id == product.id:
            return product
        return "NotFound 404"


    def simulate_buyer_get_shipping(self, cep, products, product_post_id):
        inputs = {
            'cep': cep if cep else 12345678,
            'product_post_id': product_post_id if product_post_id else 1
        }
        shipping_price = self.shipping_view.get_ship(inputs['cep'], products, inputs['product_post_id'])
        print('FRETE: ', shipping_price)
        return shipping_price

    def simulate_buyer_get_order_status(self, channel_order_history):
        order = self.order_view.get_order_status(channel_order_history)
        print('STATUS DA ORDEM: ', order['status'])

