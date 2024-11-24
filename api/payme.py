from flask import jsonify
from const import *
from bot.repository.car import get_car_by_id


def check_perform_transaction(request):
    print(request)

    car = get_car_by_id(request['account']['order_id'])
    if car.tariff.amount != request['amount']:
        return jsonify({
            'result': {
                'allow': PAYME_ERROR_INVALID_AMOUNT,
            },
        })

    return jsonify({
        'result': {
            'allow': True,
        },
    })


def create_transaction(request):
    pass


def perform_transaction(request):
    pass


def cancel_transaction(request):
    pass


def check_transaction(request):
    pass


def get_statement(request):
    pass



