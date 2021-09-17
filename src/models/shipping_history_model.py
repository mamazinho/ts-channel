from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from config.settings import Settings

class shippingHistoryModel(Settings.Base):

    __tablename__ = 'shipping_history'

    id = Column(Integer, primary_key=True)
    product_post_id = Column(Integer, ForeignKey('product_post.id'))
    requested_at = Column(DateTime)
    responsed_at = Column(DateTime)

    def __str__(self):
        return f'{self.id} - {self.product_post_id} - {self.requested_at} - {self.responsed_at}'