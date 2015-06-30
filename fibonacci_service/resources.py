import json
from flask.ext.restful import Resource
from fibonacci_service import api
from fibonacci_service.compute_sequence import compute_sequence


class Fibonacci(Resource):

    def get(self, base_num):
        result = json.dumps(compute_sequence(base_num))
        return result


class HealthCheck(Resource):

    def get(self):
        return "All is healthy"


""" Register resources """

api.add_resource(Fibonacci, '/fibonacci/<base_num>')
api.add_resource(HealthCheck, '/is_it_healthy')
