from flask_restful import reqparse

from models import PaymentMethod
from resources.abstract_resource import AbstractResource, AbstractResourceList


class PaymentMethodResource(AbstractResource):
    model = PaymentMethod
    parser = reqparse.RequestParser()
    parser.add_argument('payment_system', type=str, required=False)
    parser.add_argument('card_number', type=str, required=False)
    parser.add_argument('expire_date', type=str, required=False)
    parser.add_argument('cvv', type=str, required=False)
    parser.add_argument('country', type=str, required=False)


class PaymentMethodListResource(AbstractResourceList):
    model = PaymentMethod
