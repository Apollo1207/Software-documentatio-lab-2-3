from flask_restful import Resource

from database import Session
from models import AbstractModel


class AbstractResource(Resource):
    __abstract__ = True
    model: AbstractModel.__class__ = None
    parser = None

    def get(self, pk):
        obj = self.model.get_by_pk(pk=pk)
        return (obj.json(), 200) if obj else ({'msg': 'item not found'}, 400)

    def post(self, pk=None):
        data = self.parser.parse_args()
        # import pdb
        # pdb.set_trace()
        item = self.model(**data)
        item.save()
        return item.json(), 201 if item else 500

    def put(self, pk):
        data = self.parser.parse_args()
        item = self.model.get_by_pk(pk=pk)
        item.save()
        if item:
            for k, v in data.items():
                if v and hasattr(item, k):
                    setattr(item, k, v)
        else:
            item = self.model(**data)
        item.save()
        return item.json(), 200

    def delete(self, pk):
        item = self.model.get_by_pk(pk=pk)
        if item:
            item.delete()
        return {'msg': 'deleted'}, 200


class AbstractResourceList(Resource):
    __abstract__ = True
    model: AbstractModel.__class__ = None

    def get(self):
        return {'objects': [obj.json() for obj in self.model.get_all()]}
