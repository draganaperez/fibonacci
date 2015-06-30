from fibonacci_service import app


class InputParameterError(Exception):
    def __init__(self, message=None):
        self.message = message


"""    Register custom exception handlers here """


@app.errorhandler(InputParameterError)
def special_exception_handler(error):
    return error.message, 400
