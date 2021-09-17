from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from config.settings import Settings

class OrderHistoryModel(Settings.Base):

    __tablename__ = 'order_history'

    id = Column(Integer, primary_key=True)
    product_post_id = Column(Integer, ForeignKey('product_post.id'))
    status = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __str__(self):
        return f'{self.id} - {self.product_post_id} - {self.status} - {self.created_at} - {self.updated_at}'