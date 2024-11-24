from flask import jsonify
import hashlib
import config
from bot.repository.car import get_car_by_id, update_status
from bot.models.click import Click
from bot.models.car import PaymentStatus
from bot.repository.click import create
from const import *


def prepare(request_data):
    click_transaction = Click()
    click_transaction.click_trans_id = request_data.get('click_trans_id')
    click_transaction.service_id = request_data.get('service_id')
    click_transaction.click_paydoc_id = request_data.get('click_paydoc_id')
    click_transaction.merchant_trans_id = request_data.get('merchant_trans_id')
    click_transaction.amount = request_data.get('amount')
    click_transaction.action = request_data.get('action')
    click_transaction.error = request_data.get('error')
    click_transaction.error_note = request_data.get('error_note')
    click_transaction.sign_time = request_data.get('sign_time')
    click_transaction.sign_string = request_data.get('sign_string')

    transaction_id = create(click_transaction)

    if click_transaction.error < 0:
        return jsonify({
            "click_trans_id": click_transaction.click_trans_id,
            "merchant_trans_id": click_transaction.merchant_trans_id,
            "merchant_prepare_id": transaction_id,
            "error": CLICK_TRANSACTION_CANCELLED,
            "error_note": click_transaction.error_note,
        })

    if validate_sign_string(click_transaction.sign_string, click_transaction.service_id, config.CLICK_SECRET_KEY,
                            click_transaction.merchant_trans_id, click_transaction.amount, click_transaction.action,
                            click_transaction.sign_time, click_transaction.sign_string):
        return jsonify({
            "click_trans_id": click_transaction.click_trans_id,
            "merchant_trans_id": click_transaction.merchant_trans_id,
            "merchant_prepare_id": transaction_id,
            "error": CLICK_INCORRECT_SIGN_CHECK,
            "error_note": "sign sting is incorrect",
        })

    car = get_car_by_id(click_transaction.merchant_trans_id)
    if car is None:
        return jsonify({
            "click_trans_id": click_transaction.click_trans_id,
            "merchant_trans_id": click_transaction.merchant_trans_id,
            "merchant_prepare_id": transaction_id,
            "error": CLICK_TRANSACTION_DOES_NOT_EXIST,
            "error_note": "already paid",
        })

    if car.payment_status == PaymentStatus.PAID:
        return jsonify({
            "click_trans_id": click_transaction.click_trans_id,
            "merchant_trans_id": click_transaction.merchant_trans_id,
            "merchant_prepare_id": transaction_id,
            "error": CLICK_ALREADY_PAID,
            "error_note": "already paid",
        })

    if car.tariff.amount != click_transaction.amount:
        return jsonify({
            "click_trans_id": click_transaction.click_trans_id,
            "merchant_trans_id": click_transaction.merchant_trans_id,
            "merchant_prepare_id": transaction_id,
            "error": CLICK_INCORRECT_AMOUNT,
            "error_note": "incorrect amount",
        })

    return jsonify({
        "click_trans_id": click_transaction.click_trans_id,
        "merchant_trans_id": click_transaction.merchant_trans_id,
        "merchant_prepare_id": transaction_id,
        "error": 0,
        "error_note": "",
    })


def complete(request_data):
    click_trans_id = request_data.get('click_trans_id')
    service_id = request_data.get('service_id')
    merchant_trans_id = request_data.get('merchant_trans_id')
    transaction_id = request_data.get('merchant_prepare_id')
    amount = request_data.get('amount')
    action = request_data.get('action')
    error = request_data.get('error')
    error_note = request_data.get('error_note')
    sign_time = request_data.get('sign_time')
    sign_string = request_data.get('sign_string')

    if error < 0:
        return jsonify({
            "click_trans_id": click_trans_id,
            "merchant_trans_id": merchant_trans_id,
            "merchant_confirm_id": transaction_id,
            "error": CLICK_TRANSACTION_CANCELLED,
            "error_note": error_note,
        })

    if validate_sign_string(sign_string, service_id, config.CLICK_SECRET_KEY,
                            merchant_trans_id, amount, action,
                            sign_time, sign_string):
        return jsonify({
            "click_trans_id": click_trans_id,
            "merchant_trans_id": merchant_trans_id,
            "merchant_confirm_id": transaction_id,
            "error": CLICK_INCORRECT_SIGN_CHECK,
            "error_note": "sign sting is incorrect",
        })

    car = get_car_by_id(merchant_trans_id)
    if car is None:
        return jsonify({
            "click_trans_id": click_trans_id,
            "merchant_trans_id": merchant_trans_id,
            "merchant_confirm_id": transaction_id,
            "error": CLICK_TRANSACTION_DOES_NOT_EXIST,
            "error_note": "transaction not found",
        })

    if car.payment_status == PaymentStatus.PAID:
        return jsonify({
            "click_trans_id": click_trans_id,
            "merchant_trans_id": merchant_trans_id,
            "merchant_confirm_id": transaction_id,
            "error": CLICK_ALREADY_PAID,
            "error_note": "already paid",
        })

    if car.tariff.amount != amount:
        return jsonify({
            "click_trans_id": click_trans_id,
            "merchant_trans_id": merchant_trans_id,
            "merchant_confirm_id": transaction_id,
            "error": CLICK_INCORRECT_AMOUNT,
            "error_note": "incorrect amount",
        })

    update_status(car, PaymentStatus.PAID)




    return jsonify({
        "click_trans_id": click_trans_id,
        "merchant_trans_id": merchant_trans_id,
        "merchant_confirm_id": transaction_id,
        "error": 0,
        "error_note": "",
    })


def validate_sign_string(click_trans_id, service_id, secret_key, merchant_trans_id, amount, action, sign_time,
                         received_sign_string):
    data_string = f"{click_trans_id}{service_id}{secret_key}{merchant_trans_id}{amount}{action}{sign_time}"
    generated_hash = hashlib.md5(data_string.encode('utf-8')).hexdigest()

    return generated_hash == received_sign_string
