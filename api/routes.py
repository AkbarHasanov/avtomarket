from flask import Blueprint, request, jsonify
from api import click, payme
from telebot import types
from config import WEBHOOK_PATH, PAYME_KEY
from bot.bot import bot

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/click/prepare', methods=['POST'])
def prepare():
    request_data = request.get_json()
    return click.prepare(request_data)


@api_blueprint.route('/click/complete', methods=['POST'])
def complete():
    request_data = request.get_json()
    return click.complete(request_data)


@api_blueprint.route('/payme/pay', methods=['POST'])
def payme_payment():
    if request.headers.get("Authorization") != f"Basic {PAYME_KEY}":
        return jsonify({
            'error': {
                'code': -32504,
                'message': "Unathorized",
            }
        }), 200

    request_data = request.get_json()

    method = request_data.get('method')

    if method == "CheckPerformTransaction":
        return payme.check_perform_transaction(request_data['params'])
    elif method == "CreateTransaction":
        return payme.create_transaction(request_data['params'])
    elif method == "PerformTransaction":
        return payme.perform_transaction(request_data['params'])
    elif method == "CancelTransaction":
        return payme.cancel_transaction(request_data['params'])
    elif method == "CheckTransaction":
        return payme.check_transaction(request_data['params'])
    elif method == "GetStatement":
        return payme.get_statement(request_data['params'])
    else:
        return "Method not supported"


@api_blueprint.route(WEBHOOK_PATH, methods=['POST'])
def webhook():
    """
    Telegram sends updates to this endpoint. The bot processes the updates.
    """
    json_data = request.get_json()
    if json_data:
        import logging
        update = types.Update.de_json(json_data)
        logging.error("update: ", update)
        bot.process_new_updates([update])
    return "", 200
