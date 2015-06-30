import unittest
from fibonacci_service import app


class ResourceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_fibonacci_resource(self):
        response = self.app.get('/fibonacci/0',)
        self.assertEqual(response._status_code, 200)

        response = self.app.get('/fibonacci/5',)
        self.assertEqual(response._status_code, 200)

        response = self.app.get('/fibonacci/50000')
        self.assertEqual(response._status_code, 400)

        response = self.app.get('/fibonacci/-5')
        self.assertEqual(response._status_code, 400)

    def test_healthcheck_resource(self):
        response = self.app.get('/is_it_healthy',)
        self.assertEqual(response._status_code, 200)