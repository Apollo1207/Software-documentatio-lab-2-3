from database import init_db, session

from flask import Flask, render_template
from flask_restful import Api

from models import User, PaymentMethod
from resources.user import UserResource, UserListResource
from resources.payment_method import PaymentMethodResource, PaymentMethodListResource
from utils import write_from_csv_to_database, generate_csv_file

app = Flask(__name__)
api = Api(app)

api.add_resource(UserResource, '/user', '/user/<int:pk>')
api.add_resource(UserListResource, '/users')
api.add_resource(PaymentMethodResource, '/paymentMethod', '/paymentMethod/<int:pk>')
api.add_resource(PaymentMethodListResource, '/messages')


@app.route("/", methods=["GET"])
def get_all_data():
    users = [x.json() for x in User.get_all()]
    payment_methods = [x.json() for x in PaymentMethod.get_all()]
    return render_template("index.html", users=users, payment_methods=payment_methods)


if __name__ == '__main__':
    init_db()
    # generate_csv_file('data.csv')
    # write_from_csv_to_database('data.csv', ['User', 'PaymentMethod'], session=session)
    app.run()
