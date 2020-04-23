# -*- coding: utf-8 -*-

import braintree
from flask import render_template, Flask


app = Flask(__name__, static_folder=".", static_url_path="", template_folder="")


gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="",
        public_key="",
        private_key="",
    )
)


@app.route("/client_token", method=["GET"])
def client_token():
    token = gateway.client_token.generate()
    return render_template("charge.html", client_token=token)


@app.route("/checkout", methods=["POST"])
def create_purchase(request):
    print(request)
    nonce_from_the_client = request.form["payment_method_nonce"]
    result = gateway.transaction.sale(
        {
            "amount": "10.00",
            "payment_method_nonce": nonce_from_the_client,
            "device_data": "",
            "options": {"submit_for_settlement": True},
        }
    )
    return result
