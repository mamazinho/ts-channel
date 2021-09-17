from config.database import Database
from src.models.shipping_history_model import shippingHistoryModel

from datetime import datetime

class ShippingHistoryDao:

    def __init__(self, shipping_history:dict={}):
        self.shipping_history = shipping_history
    
    def create(self):
        with Database() as session:
            martketplace = shippingHistoryModel(
                product_post_id = self.shipping_history["product_post_id"],
                requested_at = datetime.now()
            )
            session.add(martketplace)
            session.flush()
            session.commit()
            return martketplace.id

    def read_all(self):
        with Database() as session:
            result = session.query(shippingHistoryModel).all()
            return result

    def read_by_id(self):
        with Database() as session:
            result = session.query(shippingHistoryModel).filter_by(id=self.shipping_history['id']).all()
            return result[0]

    def update(self):
        if not 'id' in self.shipping_history or not self.shipping_history['id']:
            return self.create()
        with Database() as session:
            shipping_history_update = session.query(shippingHistoryModel).filter_by(id=self.shipping_history['id'])
            shipping_history_update.update({
                "id": self.shipping_history['id'],
                "responsed_at": self.shipping_history["responsed_at"] if self.shipping_history['responsed_at'] else shipping_history_update[0].responsed_at,
            })
            session.commit()