from src.daos.marketplace_dao import MarketPlaceDao
from src.controllers.marketplace_controller import MarketPlaceController
from src.controllers.order_history_controller import OrderHistoryController
from src.controllers.product_post_controller import ProductPostController
from src.controllers.shipping_history_controller import ShippingHistoryController
from time import sleep


class Main:

    def __init__(self):
        self.product_controller = ProductPostController()
        self.marketplace_controller = MarketPlaceController()
        self.order_history_controller = OrderHistoryController()
        self.shipping_history_controller = ShippingHistoryController()
        print('--------MARKETPLACE--------')
        self.test_marketplace_create()
        sleep(2)
        self.test_marketplace_create_controller()
        sleep(2)
        self.test_marketplace_read_by_id_controller()
        sleep(2)
        print('--------PRODUCT POST--------')
        self.test_product_post_create()
        sleep(2)
        self.test_product_post_read_all()
        sleep(2)
        self.test_product_post_update()
        sleep(2)
        self.test_product_post_read_by_id()
        sleep(2)
        self.test_product_post_read_by_seller_id()
        sleep(2)
        self.test_product_post_read_by_marketplace_id()
        sleep(2)
        self.test_product_post_read_by_product_catalog_id()
        sleep(2)
        self.test_product_post_delete()
        sleep(2)
        self.test_product_post_read_by_multiple_fields()
        sleep(2)
        print('--------ORDER HISTORY--------')
        self.test_order_history_create_controller()
        sleep(2)
        self.test_order_history_read_all_controller()
        sleep(2)
        self.test_order_history_update_controller()
        sleep(2)
        self.test_order_history_read_by_id_controller()
        sleep(2)
        self.test_order_history_delete_controller()
        sleep(2)
        print('--------SHIPPING HISTORY--------')
        self.test_shipping_history()

    def test_marketplace_create(self):
        marketplace_created = MarketPlaceDao({}, True)
        print('MARKETPLACE CREATED', marketplace_created)

    def test_marketplace_create_controller(self):
        marketplace_created = self.marketplace_controller.create_marketplace('new marketplace')
        print('MARKETPLACE CREATED', marketplace_created)

    def test_marketplace_read_by_id_controller(self):
        marketplaces = self.marketplace_controller.read_by_id(1)
        print('MARKETPLACE READED BY ID', marketplaces)


    def test_product_post_create(self):
        product_posted = self.product_controller.create_product_post(1, 1, 1, 12345678)
        print('PRODUCT POSTED CREATED', product_posted)

    def test_product_post_read_all(self):
        products_posted = self.product_controller.read_all()
        print('PRODUCT READING ALL')
        [print(product) for product in products_posted]

    def test_product_post_update(self):
        self.product_controller.update_product_post(1, seller_zip_code=87654321)
        print('PRODUCT POSTED UPDATED', 1)

    def test_product_post_read_by_id(self):
        products_posted = self.product_controller.read_by_id(1)
        print('PRODUCT READING ID 1', products_posted)

    def test_product_post_read_by_seller_id(self):
        products_posted = self.product_controller.read_by_seller_id(1)
        print('PRODUCT READING SELLER_ID 1', products_posted)

    def test_product_post_read_by_marketplace_id(self):
        products_posted = self.product_controller.read_by_marketplace_id(1)
        print('PRODUCT READING MARKETPLACE 1', products_posted)
        
    def test_product_post_read_by_product_catalog_id(self):
        products_posted = self.product_controller.read_by_product_catalog_id(1)
        print('READING PRODUCT CATALOG 1', products_posted)

    def test_product_post_delete(self):
        self.product_controller.delete_product_post(1)
        print('PRODUCT POSTED DELETED', 1)

    def test_product_post_read_by_multiple_fields(self):
        conditions = {
            'product_catalog_id': 1,
            'seller_id': 1
        }
        products_posted = self.product_controller.read_by_multiple_fields(conditions)
        print('PRODUCT READING BY MULTIPLE CONDITIONALS', products_posted)


    def test_order_history_create_controller(self):
        order_history_created = self.order_history_controller.create(1)
        print('ORDER HISTORY CREATED', order_history_created)


    def test_order_history_read_all_controller(self):
        order_history_read_all = self.order_history_controller.read_all()
        print('ORDER HISTORY READ ALL')
        for item in order_history_read_all:
            print(item)

    def test_order_history_update_controller(self):
        test_update_order_history = {
            "id": 3,
            "product_post_id": 1
        }
        self.order_history_controller.update(
            test_update_order_history['id'], test_update_order_history['product_post_id'])
        print('ORDER HISTORY UPDATE', 3)

    def test_order_history_read_by_id_controller(self):
        order_history_read_by_id = self.order_history_controller.read_by_id(3)
        print('ORDER HISTORY READ BY ID', order_history_read_by_id)

    def test_order_history_delete_controller(self):
        self.order_history_controller.delete(3)
        print('ORDER HISTORY DELETE', 3)


    def test_shipping_history(self):
        shipping_history_created = self.shipping_history_controller.create(1)
        print('SHIPPING HISTORY CREATED', shipping_history_created)
        

Main()
