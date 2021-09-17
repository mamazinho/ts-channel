from src.daos.product_post_dao import ProductPostDao

from datetime import datetime

class ProductPostController:

    def create_product_post(self, marketplace_id, product_catalog_id, seller_id, seller_zip_code):
        product_post = {
            'marketplace_id': marketplace_id,
            'product_catalog_id': product_catalog_id,
            'seller_id': seller_id,
            'seller_zip_code': seller_zip_code
        }
        product_post_id = ProductPostDao(product_post).create()
        return product_post_id

    def update_product_post(self, product_post_id, marketplace_id=None, product_catalog_id=None, seller_id=None, seller_zip_code=None, status=True):
        product_post = {
            'id': product_post_id,
            'marketplace_id': marketplace_id,
            'product_catalog_id': product_catalog_id,
            'seller_id': seller_id,
            'seller_zip_code': seller_zip_code,
            'status': status
        }
        ProductPostDao(product_post).update()

    def delete_product_post(self, product_post_id):
        self.update_product_post(product_post_id, status=False)
        
    def read_all(self):
        products_posted = ProductPostDao().read_all()
        return products_posted

    def read_by_id(self, product_post_id):
        product_post = {
            'id': product_post_id
        }
        products_posted = ProductPostDao(product_post).read_by_id()
        return products_posted

    def read_by_seller_id(self, seller_id):
        product_post = {
            'seller_id': seller_id
        }
        products_posted = ProductPostDao(product_post).read_by_seller_id()
        return products_posted

    def read_by_marketplace_id(self, marketplace_id):
        product_post = {
            'marketplace_id': marketplace_id
        }
        products_posted = ProductPostDao(product_post).read_by_marketplace_id()
        return products_posted

    def read_by_product_catalog_id(self, product_catalog_id):
        product_post = {
            'product_catalog_id': product_catalog_id
        }
        products_posted = ProductPostDao(product_post).read_by_product_catalog_id()
        return products_posted
    
    def read_by_multiple_fields(self, fields):
        products_posted = ProductPostDao(fields).read_by_multiple_fields()
        return products_posted
