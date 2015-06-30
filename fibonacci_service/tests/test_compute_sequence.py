import unittest
from fibonacci_service.compute_sequence import compute_sequence
from fibonacci_service.exceptions import InputParameterError


class FibonacciSequenceTestCase(unittest.TestCase):

    def test_sequence(self):
        result = compute_sequence(0)
        self.assertEqual(result, [0, 1])

    def test_sequence_string_input(self):
        result = compute_sequence('1')
        self.assertEqual(result, [0, 1])

    def test_sequence_negative_number(self):
        self.assertRaises(InputParameterError, compute_sequence, -5)

    def test_sequence_big_number(self):
        self.assertRaises(InputParameterError, compute_sequence, 5000)

    def test_sequence_invalid_string(self):
        self.assertRaises(InputParameterError, compute_sequence, '55a')
