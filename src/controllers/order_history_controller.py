from src.daos.order_history_dao import OrderHistoryDAO
from datetime import datetime


class OrderHistoryController():

    def create(self, product_post_id):
        new_order_history = {
            "product_post_id": product_post_id
        }
        order_history_id = OrderHistoryDAO(new_order_history).create()
        return order_history_id

    def read_all(self):
        list_order_history = OrderHistoryDAO().read_all()
        return list_order_history

    def read_by_id(self, order_history_id):
        order_history_id = {
            'id': order_history_id
        }
        order_history = OrderHistoryDAO(order_history_id).read_by_id()
        return order_history

    def delete(self, order_history_id):
        order_history = {
            "id": order_history_id
        }
        OrderHistoryDAO(order_history).delete()

    def update(self, order_history_id, product_post_id=None, status=None):
        order_history_update = {
            "id": order_history_id,
            "product_post_id": product_post_id,
            "status": status,
        }
        OrderHistoryDAO(order_history_update).update()
