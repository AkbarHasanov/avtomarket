from flask import jsonify
from const import *
from bot.repository.car import get_car_by_id
from bot.repository import payme
from bot.models.payme import Payme


def check_perform_transaction(request):
    print(request)

    car = get_car_by_id(request['account']['order_id'])
    if car.tariff.amount != request['amount']:
        return jsonify({
            'error': {
                'code': PAYME_ERROR_INVALID_AMOUNT,
            }
        })

    return jsonify({
        'result': {
            'allow': True,
        },
    })


def create_transaction(request):
    payme_transaction = Payme()
    payme_transaction.transaction_id = request['id']
    payme_transaction.created_at_payme = request['time']
    payme_transaction.amount = request['amount']
    account = request['account']
    payme_transaction.order_id = account['order_id']
    payme_transaction.state = 1

    car = get_car_by_id(request['account']['order_id'])
    if car.tariff.amount != request['amount']:
        return jsonify({
            'error': {
                'code': PAYME_ERROR_INVALID_AMOUNT,
            },
        })

    payme_transaction = payme.create(payme_transaction)

    return jsonify({
        "result": {
            "create_time": payme_transaction.create_time,
            "transaction": payme_transaction.id,
            "state": 1
        }
    })


def perform_transaction(request):
    transaction_id = request['id']
    transaction = payme.perform(transaction_id)

    return jsonify({
        "result": {
            "transaction": transaction.id,
            "perform_time": transaction.perform_time,
            "state": 2
        }
    })


def cancel_transaction(request):
    transaction_id = request['id']
    transaction = payme.cancel(transaction_id)

    return jsonify({
        "result": {
            "transaction": transaction.id,
            "cancel_time": transaction.cancel_time,
            "state": -2
        }
    })


def check_transaction(request):
    transaction_id = request['id']
    transaction = payme.get(transaction_id)

    return jsonify({
        "result": {
            "create_time": transaction.create_time,
            "perform_time": transaction.perform_time,
            "cancel_time": transaction.cancel_time,
            "transaction": transaction.id,
            "state": transaction.state,
            "reason": transaction.reason,
        }
    })


def get_statement(request):
    from_time = request['from']
    to_time = request['to']
    transactions = payme.get_all(from_time, to_time)

    result = []
    for transaction in transactions:
        result.append({
            "id": transaction.transaction_id,
            "time": transaction.created_at_payme,
            "amount": transaction.amount,
            "account": {
                "order_id": transaction.order_id,
            },
            "create_time": transaction.create_time,
            "perform_time": transaction.perform_time,
            "cancel_time": transaction.cancel_time,
            "transaction": transaction.id,
            "state": transaction.state,
            "reason": transaction.reason,
        })

    return jsonify({
        "result": {
            "transactions": result
        }
    })
