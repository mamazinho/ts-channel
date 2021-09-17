import os
import sys
from unittest import TestCase
from unittest.mock import patch, MagicMock
import pytest

sys.path.append(os.getcwd())

from src.controllers.marketplace_controller import MarketPlaceController
from src.models.marketplace_model import MarketPlaceModel



class TestMarketPlaceController(TestCase):


    def setUp(self):
        self.market_place_controller = MarketPlaceController()

    def test_can_create_an_instance_of_MarketPlaceController_class(self):

        self.assertIsInstance(self.market_place_controller, MarketPlaceController)

    def test_create_marketplace_method(self):
        
        name_of_marketplace = 'marketplace_name_test'


        market_place_id = self.market_place_controller.create_marketplace(
            name_of_marketplace
            )

        self.assertEqual(type(market_place_id), int)
        
    def test_create_marketplace_method_raise_exception(self):
        
        with pytest.raises(Exception) as ex:
            market_place_id = self.market_place_controller.create_marketplace(
                [123124]
                )

        self.assertIsInstance(ex.value, Exception)
        self.assertEqual(ex.value.args[0], "Valor Invalido")


    @patch('src.controllers.marketplace_controller.MarketPlaceDao.read_all')
    def test_read_all_method(self, read_all_mock):

        products = ['produtos teste']

        read_all_mock.return_value = products

        marketplaces = self.market_place_controller.read_all()

        self.assertEqual(marketplaces, products)

    @patch('src.controllers.marketplace_controller.MarketPlaceDao.read_by_id')
    def test_read_by_id_method(
        self,
        read_by_id_mock
        ):


        marketplace_model_mock = MagicMock()
        marketplace_model_mock.id = 1

        read_by_id_mock.return_value = marketplace_model_mock 

        products_posted = self.market_place_controller.read_by_id(
            marketplace_id=1
        )

        self.assertEqual(products_posted, marketplace_model_mock)

    @patch('src.controllers.marketplace_controller.MarketPlaceDao.read_by_name')
    def test_read_by_name_method(
        self,
        read_by_name_mock
        ):


        marketplace_model_mock = MagicMock()
        marketplace_model_mock.id = 1
        marketplace_model_mock.name = "markeplace_name_test"

        read_by_name_mock.return_value = marketplace_model_mock 
        

        products_posted = self.market_place_controller.read_by_name(
            marketplace_name="markeplace_name_test"
        )


        self.assertEqual(products_posted, marketplace_model_mock)