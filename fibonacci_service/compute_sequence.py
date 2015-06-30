from fibonacci_service.config import config
from fibonacci_service.exceptions import InputParameterError


def compute_sequence(base_num):
    try:
        base = int(base_num)
        if base < 0 or base > config.max_int:
            raise InputParameterError('Please supply an integer between 0 and {}. Supplied {}'
                                      .format(config.max_int, base_num))

    except ValueError:
        raise InputParameterError('Number {} is not a valid integer.'.format(base_num))

    result = [0, 1]
    for i in range(2, base):
        result.append(result[i-1] + result[i-2])

    return result
