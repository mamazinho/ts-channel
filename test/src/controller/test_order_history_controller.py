import os
import sys
from unittest import TestCase
from unittest.mock import patch, MagicMock
import pytest

sys.path.append(os.getcwd())

from src.controllers.order_history_controller import OrderHistoryController


class TestOrderHistoryController(TestCase):


    def setUp(self):
        self.order_history_controller = OrderHistoryController()
        self.ID_TEST=1


    def test_can_create_an_instance_of_OrderHistoryController_class(self):

        self.assertIsInstance(self.order_history_controller, OrderHistoryController)


    @patch('src.controllers.order_history_controller.OrderHistoryDAO.create')
    def test_create_order_history_method(
        self,
        create_mock
        ):

        create_mock.return_value = self.ID_TEST

        order_history_id = self.order_history_controller.create(
            self.ID_TEST
            )

        self.assertEqual(type(order_history_id), int)
        self.assertEqual(order_history_id, 1)


    @patch('src.controllers.order_history_controller.OrderHistoryDAO.read_all')
    def test_read_all_method(self, read_all_mock):

        products = MagicMock()

        read_all_mock.return_value = products

        order_historys = self.order_history_controller.read_all()

        self.assertEqual(order_historys, products)

    @patch('src.controllers.order_history_controller.OrderHistoryDAO.read_by_id')
    def test_read_by_id_method(
        self,
        read_by_id_mock
        ):


        order_history_model_mock = MagicMock()
        order_history_model_mock.id = 1

        read_by_id_mock.return_value = order_history_model_mock 

        products_posted = self.order_history_controller.read_by_id(
            order_history_id=1
        )

        self.assertEqual(products_posted, order_history_model_mock)


    @patch('src.controllers.order_history_controller.OrderHistoryDAO.delete')
    def test_delete_method(
        self,
        delete_mock
        ):

        self.order_history_controller.delete(self.ID_TEST)

        delete_mock.assert_called_once()
