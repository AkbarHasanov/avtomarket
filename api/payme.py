from datetime import datetime
from flask import jsonify
from const import *
from bot.repository.car import get_car_by_id, update_status
from bot.repository import payme
from bot.models.payme import Payme
from bot.models.car import PaymentStatus
from bot.bot import bot
from bot.handlers.payment_handler import send_payment_success_message


def _check_perform_transaction(request):
    car = get_car_by_id(request['account']['order_id'])
    if car is None:
        return {
            'error': {
                'code': PAYME_ERROR_ORDER_NOT_FOUND,
                'message': "Order not found",
            }
        }
    if car.tariff.amount != request['amount']:
        return {
            'error': {
                'code': PAYME_ERROR_INVALID_AMOUNT,
                'message': 'Invalid amount',
            }
        }
    return {
        'result': {
            'allow': True,
        },
    }

def check_perform_transaction(request):
    return jsonify(_check_perform_transaction(request))

def check(transaction: Payme):
    if transaction.state != 1:
        return jsonify({
            'error': {
                'code': -31008,
                'message': 'State != 1'
            }
        })
    
    if datetime.now().timestamp() * 1000 - transaction.create_time >= 1000*3600:
        payme.cancel(transaction.id, 4, -1)

    return jsonify({
        "result": {
            "create_time": transaction.create_time,
            "transaction": transaction.transaction_id,
            "state": 1
        }
    })



def create_transaction(request):
    old_transaction = payme.get_by_transaction_id(request['id'])

    if old_transaction is not None:
        return check(old_transaction)
    
    response = _check_perform_transaction(request)

    if response.get('error') is not None:
        return jsonify(response)


    payme_transaction = Payme()
    payme_transaction.transaction_id = request['id']
    payme_transaction.created_at_payme = request['time']
    payme_transaction.amount = request['amount']
    account = request['account']
    payme_transaction.order_id = account['order_id']
    payme_transaction.state = 1

    car = get_car_by_id(request['account']['order_id'])
    if car is None:
        return jsonify({
            'error': {
                'code': PAYME_ERROR_ORDER_NOT_FOUND,
                'message': "Order not found",
            }
        })
    if car.tariff.amount != request['amount']:
        return jsonify({
            'error': {
                'code': PAYME_ERROR_INVALID_AMOUNT,
                'message': 'Invalid amount',
            },
        })

    payme_transaction = payme.create(payme_transaction)

    return jsonify({
        "result": {
            "create_time": payme_transaction.create_time,
            "transaction": payme_transaction.transaction_id,
            "state": 1
        }
    })


def perform_transaction(request):
    transaction_id = request['id']
    transaction = payme.get_by_transaction_id(transaction_id)
    if transaction is None:
        return jsonify({
            'error': {
                'code': PAYME_ERROR_TRANSACTION_NOT_FOUND,
                'message': 'Transaction not found'
            }
        })

    if transaction.state != 1:
        if transaction.state != 2:
            return jsonify({
                'error': {
                    'code': PAYME_ERROR_COULD_NOT_PERFORM,
                    'message': 'Transaction cancelled'
                }
            })
        return jsonify({
            "result": {
                "transaction": transaction.id,
                "perform_time": transaction.perform_time,
                "state": 2
            }
        })

    if datetime.now().timestamp() * 1000 - transaction.create_time > 1000 * 3600:
        payme.cancel(transaction_id, 4, -1)
        return jsonify({
            'error': {
                'code': PAYME_ERROR_COULD_NOT_PERFORM,
                'message': "Transaction expired",
            }
        })

    try:
        transaction = payme.perform(transaction_id)
        if transaction is None:
            raise ValueError("not found")
    except:
        return jsonify({
            'error': {
                'code': PAYME_ERROR_TRANSACTION_NOT_FOUND,
                'message': 'Transaction not found'
            }
        })
        

    car = get_car_by_id(transaction.order_id)
    if car is None:
        return jsonify({
            'error': {
                'code': PAYME_ERROR_ORDER_NOT_FOUND,
                'message': "Order not found",
            }
        })
    update_status(car, PaymentStatus.PAID)
    send_payment_success_message(bot, car)

    return jsonify({
        "result": {
            "transaction": transaction.id,
            "perform_time": transaction.perform_time,
            "state": 2
        }
    })


def cancel_transaction(request):
    transaction_id = request['id']
    try:
        transaction = payme.cancel(transaction_id)
        if transaction is None:
            raise ValueError('transaction error')
    except:
        return jsonify({
            'error': {
                'code': PAYME_ERROR_COULD_NOT_CANCEL,
                'message': "Could not cancel"
            }
        })

    return jsonify({
        "result": {
            "transaction": transaction.id,
            "cancel_time": transaction.cancel_time,
            "state": -2
        }
    })


def check_transaction(request):
    transaction_id = request['id']
    try:
        transaction = payme.get_by_transaction_id(transaction_id)
        if transaction is None:
            raise ValueError("transaction not found")
    except:
        return jsonify({
            'error': {
                'code': PAYME_ERROR_ORDER_NOT_FOUND,
                'message': "transaction not found",
            }
        })

    return jsonify({
        "result": {
            "create_time": transaction.create_time,
            "perform_time": transaction.perform_time,
            "cancel_time": transaction.cancel_time,
            "transaction": transaction.transaction_id,
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
