from src.controllers.order_history_controller import OrderHistoryController


class OrderView():

    def __init__(self):
        self.order_history_controller = OrderHistoryController()

    def create_order_history(self, order, product_post_id):
        order_history_id = self.order_history_controller.create(product_post_id)
        order['channel_order_id'] = order_history_id
        # Chama Order API enviado a order (quando realmente tiver rotas)
        response = self.mock_order_api_send_order(order)

        if response == 200:
            self.order_history_controller.update(order_history_id)

        return order_history_id

    def mock_order_api_send_order(self, order):
        if order:
            return 200
        return 404

    def get_order_status(self, order_history_id):
        # Chama Order API requisitando status de uma order (quando realmente tiver rotas)
        return self.mock_order_api_get_status(order_history_id)

    def mock_order_api_get_status(self, order_history_id):
        response = {
            "status": "Enviando"
        }
        return response
