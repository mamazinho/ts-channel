from config.database import Database
from src.models.order_history_model import OrderHistoryModel
from datetime import datetime


class OrderHistoryDAO:

    def __init__(self, order_history: dict = {}):
        self.order_history = order_history

    def create(self):
        with Database() as session:
            order_history = OrderHistoryModel(
                product_post_id=self.order_history['product_post_id'],
                status=False,
                created_at=datetime.now(),
                updated_at=None
            )
            session.add(order_history)
            session.flush()
            session.commit()
            return order_history.id

    def read_all(self):
        with Database() as session:
            result = session.query(OrderHistoryModel).all()
            return result

    def read_by_id(self):
        with Database() as session:
            result = session.query(OrderHistoryModel).filter_by(
                id=self.order_history['id']).all()
            return result

    def update(self):
        if not 'id' in self.order_history or not self.order_history['id']:
            return self.create()
        with Database() as session:
            order_history_update = session.query(
                OrderHistoryModel).filter_by(id=self.order_history['id'])
            order_history_update.update({
                "id": self.order_history['id'],
                "product_post_id": self.order_history['product_post_id'] if self.order_history['product_post_id'] else order_history.product_post_id,
                "status": True if self.order_history['status'] == True else False,
                "updated_at": datetime.now(),
            })
            session.commit()

    def delete(self):
        with Database() as session:
            result = session.query(OrderHistoryModel).filter_by(
                id=self.order_history['id']).delete()
            session.commit()
