from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from config.settings import Settings

class productPostModel(Settings.Base):

    __tablename__ = 'product_post'

    id = Column(Integer, primary_key=True)
    marketplace_id = Column(Integer, ForeignKey('marketplace.id'))
    product_catalog_id = Column(Integer)        # Future foreign key with catalog
    seller_id = Column(Integer)         # Future foreign key with seller
    status = Column(Boolean, default=True)
    created_at = Column(DateTime)
    seller_zip_code = Column(Integer)

    def __str__(self):
        return f'{self.id} - {self.marketplace_id} - {self.product_catalog_id} - {self.seller_id} - {self.status} - {self.created_at} - {self.seller_zip_code}'