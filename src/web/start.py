from flask import Flask, render_template, request, redirect
import sys
import os
sys.path.append(os.getcwd())
from src.controllers.marketplace_controller import MarketPlaceController
from src.controllers.product_post_controller import ProductPostController
from src.controllers.shipping_history_controller import ShippingHistoryController
from src.controllers.order_history_controller import OrderHistoryController

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/marketplace')
def marketplace():
    marketplace = MarketPlaceController().read_all()
    return render_template('marketplace.html', data=marketplace)

@app.route("/order_history")
def orderhistory():
    order_hisotry = OrderHistoryController().read_all()
    return render_template('order_history.html', data=order_hisotry)

@app.route('/product_post')
def product():
    product_post = ProductPostController().read_all()
    return render_template('product_post.html', data=product_post)

@app.route('/shipping_history')
def shipping_history():
    shipping_history = ShippingHistoryController().read_all()
    return render_template('shipping_history.html', data=shipping_history)

app.run(debug=True)
