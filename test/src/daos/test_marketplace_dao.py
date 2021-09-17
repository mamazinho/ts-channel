import os
import sys
import pytest

sys.path.append(os.getcwd())

from unittest.mock import patch, call, MagicMock
from unittest import TestCase
from src.daos.marketplace_dao import MarketPlaceDao
from src.models.marketplace_model import MarketPlaceModel


class TestMarketPlaceDao(TestCase):
    def setUp(self):
        # configuração
        self.market_place_dao = MarketPlaceDao

    def test_create_instance_of_MarketPlaceDao_class(self):
        self.assertIsInstance(self.market_place_dao(), MarketPlaceDao)

    @patch('src.daos.marketplace_dao.MarketPlaceDao.create')
    def test_create_and_save_marketplace_in_database(self, create_mock):
        # marketplace_model_mock = MagicMock()
        # marketplace_model_mock.id = 1
        # ação
        create_mock.return_value = 1
        market_place_id = self.market_place_dao.create()
        # assertiva
        self.assertEqual(type(market_place_id), int)

    @patch('src.daos.marketplace_dao.MarketPlaceDao.read_all')
    def test_read_all_method(self, read_all_mock):
        marketplace = ['marketplace teste']
        read_all_mock.return_value = marketplace
        marketplaces = self.market_place_dao.read_all()
        self.assertEqual(marketplaces, marketplace)

    @patch('src.daos.marketplace_dao.MarketPlaceDao.read_by_id')
    def test_read_by_id(self, read_by_id_mock):
        marketplace_model_mock = MagicMock()
        marketplace_model_mock.id = 1
        read_by_id_mock.return_value = 1
        market_place_id = self.market_place_dao.read_by_id()
        self.assertEqual(type(market_place_id), int)

    # @patch('src.daos.marketplace_dao.Database')
    # def test_read_by_name(
    #     self,
    #     database_mock,
    # ):

    #     markeplace_model = {"name": "markeplace_name_test"}
        
    #     markeplace_model_mock = MagicMock()
    #     markeplace_model_mock.return_value = [markeplace_model]


    #     filter_mock = MagicMock()
    #     filter_mock.return_value = markeplace_model_mock

    #     query_mock = MagicMock()

    #     database_instance_mock = MagicMock()
    #     database_instance_mock.query = query_mock
    #     database_instance_mock.query.return_value.filter = filter_mock

    #     database_instance_mock.__enter__.return_value = database_instance_mock

    #     database_mock.return_value = database_instance_mock

    #     market_place_dao = MarketPlaceDao(markeplace_model)

    #     market_place_dao = market_place_dao.read_by_name()

    #     self.assertEqual(market_place_dao, 1)


    @patch('src.daos.marketplace_dao.Database')
    def test_update_marketplace(self, database_mock):
        market_place = self.market_place_dao(
            {'id': 1, 'name': 'teste_marketplace'})
        market_place_update = market_place.update()
        database_mock.assert_has_calls(
            [call(),
             call().__enter__(),
             call().__enter__().query(MarketPlaceModel),
             call().__enter__().query().filter_by(id=1),
             call().__enter__().query().filter_by().update(
                 {'id': 1, 'name': 'teste_marketplace'}),
             call().__enter__().commit(),
             call().__exit__(None, None, None)])
