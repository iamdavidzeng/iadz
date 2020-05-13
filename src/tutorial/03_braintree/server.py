# -*- coding: utf-8 -*-

import os

import braintree
from flask import render_template, Flask, request, Response


"""
Braintree integration

Test card number: 4111111111111111
Test nonce: fake-valid-nonce
"""


app = Flask(__name__, static_folder=".", static_url_path="", template_folder="")

config = os.environ

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=config["BRAINTREE_MERCHANT_ID"],
        public_key=config["BRAINTREE_PUBLIC_KEY"],
        private_key=config["BRAINTREE_PRIVATE_KEY"],
    )
)


@app.route("/client_token", methods=["GET"])
def client_token():
    token = gateway.client_token.generate()
    return render_template("charge.html", client_token=token)


@app.route("/checkout", methods=["POST"])
def create_purchase():
    nonce_from_the_client = request.get_json()["payment_method_nonce"]
    result = gateway.transaction.sale(
        {
            "amount": "10.00",
            "payment_method_nonce": nonce_from_the_client,
            "options": {"submit_for_settlement": True},
        }
    )
    if result.is_success:
        print(result.transaction)
        return Response(str(result.transaction))
    else:
        print(result.errors.deep_errors)
        return Response(str(result.errors.deep_errors))


if __name__ == "__main__":
    app.run()
