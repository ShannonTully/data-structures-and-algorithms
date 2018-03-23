import largest_product
import pytest


def test_largest_product_valid():
    assert largest_product.largest_product([[1, 2], [3, 4], [5, 6], [7, 8]]) == 56


def test_largest_product_empty_list():
    assert largest_product.largest_product([]) is False


def test_largest_product_not_array():
    with pytest.raises(TypeError) as err:
        largest_product.largest_product(1)

    assert str(err.value) == "object of type 'int' has no len()"
