from flask import jsonify
from flask.ext.restful import Resource
from fibonacci_service import api


class ComputeFibonacci(Resource):
    def get(self, base_num):
        result = [0, 1]
        for i in range(2, base_num):
            result.append(result[i-1] + result[i-2])
        return jsonify({'result': result[-1]})


class HealthCheck(Resource):
    def get(self):
        return "All is healthy"

api.add_resource(ComputeFibonacci, '/fibonacci/<int:base_num>')
api.add_resource(HealthCheck, '/is_it_healthy')
