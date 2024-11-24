from flask import Blueprint, request
from api import click, payme

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
