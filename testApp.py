from unittest.mock import MagicMock
import requests
from app import search

RequestsMock = requests()
RequestsMock.args.get = MagicMock(return_value'victor')


this.assert(RequestsMock)