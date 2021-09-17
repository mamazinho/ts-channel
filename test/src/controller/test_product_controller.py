import os
import sys
from unittest import TestCase
from unittest.mock import patch, MagicMock
import pytest

sys.path.append(os.getcwd())


from src.controllers.product_post_controller import ProductPostController



class TestProductPostController(TestCase):


    def setUp(self):
        self.product_post_controller = ProductPostController()
        self.ID_TEST=1

    @patch('src.controllers.product_post_controller.ProductPostDao.create')
    def test_create_product_post_method(
        self,
        create_mock,
    ):

        product_posted = MagicMock()
        product_posted.marketplace_id = self.ID_TEST
        product_posted.product_catalog_id = 2
        product_posted.seller_id = 3
        product_posted.seller_zip_code = 4

        product_model = self.product_post_controller.create_product_post(1,2,3,4)

        create_mock.return_value = product_posted


        self.assertAlmostEqual(product_model.marketplace_id, 1)



