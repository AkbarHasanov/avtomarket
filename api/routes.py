from flask import Blueprint, request
from api.click import click_prepare, complete
from api import payme

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/click/prepare', methods=['POST'])
def prepare():
    request_data = request.get_json()
    return click_prepare(request_data)


@api_blueprint.route('/click/complete', methods=['POST'])
def complete():
    request_data = request.get_json()
    return complete(request_data)


@api_blueprint.route('/payme/pay', methods=['POST'])
def payme_payment():
    request_data = request.get_json()

    method = request_data.get('method')

    if method == "CheckPerformTransaction":
        payme.check_perform_transaction(request_data['params'])
    elif method == "CreateTransaction":
        payme.create_transaction(request_data['params'])
    elif method == "PerformTransaction":
        payme.perform_transaction(request_data['params'])
    elif method == "CancelTransaction":
        payme.cancel_transaction(request_data['params'])
    elif method == "CheckTransaction":
        payme.check_transaction(request_data['params'])
    elif method == "GetStatement":
        payme.get_statement(request_data['params'])
