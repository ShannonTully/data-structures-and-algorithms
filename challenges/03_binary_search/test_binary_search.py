import binary_search
import pytest


def test_valid_binary_search():
    assert binary_search.binary_search([4, 8, 15, 16, 23, 42], 15) == 2
    assert binary_search.binary_search([4, 8, 15, 16, 23, 42], 4) == 0
    assert binary_search.binary_search([4, 8, 15, 16, 23, 42], 8) == 1
    assert binary_search.binary_search([4, 8, 15, 16, 23, 42], 16) == 3
    assert binary_search.binary_search([4, 8, 15, 16, 23, 42], 23) == 4
    assert binary_search.binary_search([4, 8, 15, 16, 23, 42], 42) == 5


def test_key_not_in_list():
    assert binary_search.binary_search([4, 8, 15, 16, 23, 42], 100) == 0 - 1


def test_key_string():
    with pytest.raises(TypeError) as err:
        binary_search.binary_search([4, 8, 15, 16, 23, 42], 'string')

    assert str(err.value) == 'Argument invalid. Must be int.'
