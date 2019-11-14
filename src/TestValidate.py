from unittest.mock import MagicMock
from Validate import Validator
from flask import request


RequestsMock = request
RequestsMock.headers.items = MagicMock(return_value=[['Authorization', 'token']])

ValidatorMock = Validator(RequestsMock)
this.Validate

ValidatorMock.