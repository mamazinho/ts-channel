from config.database import Database
from src.models.product_post_model import productPostModel

from datetime import datetime

class ProductPostDao:

    def __init__(self, product_post:dict={}):
        self.product_post = product_post
    
    def create(self):
        with Database() as session:
            prod_post = productPostModel(
                marketplace_id = self.product_post["marketplace_id"],
                product_catalog_id = self.product_post["product_catalog_id"],
                seller_id = self.product_post["seller_id"],
                created_at = datetime.now(),
                seller_zip_code = self.product_post["seller_zip_code"]
            )
            session.add(prod_post)
            session.flush()
            session.commit()
            return prod_post.id

    def read_all(self):
        with Database() as session:
            result = session.query(productPostModel).filter_by(status=True).all()
            return result

    def read_by_id(self):
        with Database() as session:
            result = session.query(productPostModel).filter_by(id=self.product_post['id']).all()
            return result[0]

    def read_by_seller_id(self):
        with Database() as session:
            result = session.query(productPostModel).filter_by(seller_id=self.product_post['seller_id']).all()
            return result[0]

    def read_by_marketplace_id(self):
        with Database() as session:
            result = session.query(productPostModel).filter_by(marketplace_id=self.product_post['marketplace_id']).all()
            return result[0]

    def read_by_product_catalog_id(self):
        with Database() as session:
            result = session.query(productPostModel).filter_by(product_catalog_id=self.product_post['product_catalog_id']).all()
            return result[0]
    
    def read_by_multiple_fields(self):
        with Database() as session:
            result = session.query(productPostModel).filter_by(**self.product_post).all()
            return result[0]

    def update(self):
        if not 'id' in self.product_post or not self.product_post['id']:
            return self.create()
        with Database() as session:
            prod_post_update = session.query(productPostModel).filter_by(id=self.product_post['id'])
            prod_post_update.update({
                "id": self.product_post['id'],
                "marketplace_id": self.product_post["marketplace_id"] if self.product_post['marketplace_id'] else prod_post_update[0].marketplace_id,
                "product_catalog_id": self.product_post["product_catalog_id"] if self.product_post['product_catalog_id'] else prod_post_update[0].product_catalog_id,
                "seller_id": self.product_post["seller_id"] if self.product_post['seller_id'] else prod_post_update[0].seller_id,
                "status": self.product_post["status"] if self.product_post['status'] == False else prod_post_update[0].status,
                "seller_zip_code": self.product_post["seller_zip_code"] if self.product_post['seller_zip_code'] else prod_post_update[0].seller_zip_code
            })
            session.commit()