from checkio_referee import RefereeBase
from checkio_referee import covercodes, validators, representations


import settings_env
from tests import TESTS

Validator = validators.FloatEqualValidator

Validator.PRECISION = 1


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "distance"
    VALIDATOR = Validator
    ENV_COVERCODE = {
        "python_2": covercodes.py_unwrap_args,
        "python_3": covercodes.py_unwrap_args,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_3": representations.unwrap_arg_representation,
    }
