# -*- coding: utf-8 -*-
import json
from decimal import Decimal

from behave import given, when, then


@given("Payments service is running")
def step_impl1(context):
    pass


@when("I send a healthcheck request to payments-service")
def step_impl2(context):
    response = context.rpc.payments.health_check()
    context.health_check_response = response


@then("I should get successful response")
def step_impl3(context):
    assert context.health_check_response["ok"]


@given("There is one transaction")
def step_impl4(context):
    if context.table:
        transaction_info = [row.as_dict() for row in context.table][0]
    elif context.text:
        transaction_info = json.loads(context.text)
    else:
        pass

    filters = [
        {
            "field": "transaction_record_id",
            "value": transaction_info["transaction_record_id"],
        }
    ]

    transactions = context.rpc.payments.list_simple_transactions(filters)

    if transactions:
        pass
    else:
        context.rpc.payments.create_simple_transaction(transaction_info)


@when("I get the transaction by transaction_record_id {transaction_record_id}")
def step_impl5(context, transaction_record_id):
    filters = [
        {
            "field": "transaction_record_id",
            "value": transaction_record_id,
        }
    ]

    transactions = context.rpc.payments.list_simple_transactions(filters)
    if transactions:
        context.transaction = transactions[0]


@then("I should the right transaction")
def step_impl6(context):
    transaction_info = json.loads(context.text)

    context.transaction.pop("id")
    context.transaction.update({"amount": Decimal(context.transaction["amount"])})

    assert transaction_info == context.transaction
