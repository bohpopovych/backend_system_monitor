from flask_restful import Resource
from .. import api

class Ar(Resource):
    def get(self):
        return {'task': 'Say "Hello, World!"'}

api.add_resource(Ar, '/')
