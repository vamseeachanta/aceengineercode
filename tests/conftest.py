import os

import pytest


@pytest.fixture
def get_dictionary():
    return {'a': 10, 'b': 12}
