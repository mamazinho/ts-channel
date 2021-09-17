from src.daos.shipping_history_dao import ShippingHistoryDao
from datetime import datetime


class ShippingHistoryController():

    def create(self, product_post_id):
        order_history_update = {
            "product_post_id": product_post_id,
            "requested_at": datetime.now()
        }
        order_history_id = ShippingHistoryDao(order_history_update).create()
        return order_history_id

    def update(self, shipping_id):
        order_history_update = {
            "id": shipping_id,
            "responsed_at": datetime.now(),
        }
        ShippingHistoryDao(order_history_update).update()

    def read_all(self):
        shipping_history = ShippingHistoryDao().read_all()
        return shipping_history
