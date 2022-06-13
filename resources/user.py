from flask_restful import reqparse

from models import User
from resources.abstract_resource import AbstractResource, AbstractResourceList


class UserResource(AbstractResource):
    model = User
    parser = reqparse.RequestParser()
    parser.add_argument('phone_number', type=str, required=False)
    parser.add_argument('first_name', type=str, required=False)
    parser.add_argument('last_name', type=str, required=False)
    parser.add_argument('email', type=str, required=False)
    parser.add_argument('password', type=str, required=False)
    parser.add_argument('date_of_birth', type=str, required=False)
    parser.add_argument('address', type=str, required=False)


class UserListResource(AbstractResourceList):
    model = User



