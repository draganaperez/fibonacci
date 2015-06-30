from flask import jsonify
from flask.ext.restful import Resource
from fibonacci_service import api
from fibonacci_service.exceptions import InputParameterError


class ComputeFibonacci(Resource):

    def get(self, base_num):
        try:
            base = int(base_num)
            if base < 0 or base > 1000:
                raise InputParameterError('Please supply an integer between 0 and 1000. Supplied {}'.format(base_num))
        except ValueError:
            raise InputParameterError('Number {} is not a valid integer.'.format(base_num))

        result = [0, 1]
        for i in range(2, base):
            result.append(result[i-1] + result[i-2])
        return jsonify({'result': result})


class HealthCheck(Resource):

    def get(self):
        return "All is healthy"


""" Register resources """

api.add_resource(ComputeFibonacci, '/fibonacci/<base_num>')
api.add_resource(HealthCheck, '/is_it_healthy')
