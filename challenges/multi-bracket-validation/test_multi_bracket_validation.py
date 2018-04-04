import multi_bracket_validation
import pytest


def test_basic():
    assert multi_bracket_validation.multi_bracket_validation('()') is True


def test_fail():
    assert multi_bracket_validation.multi_bracket_validation('(}') is False


def test_complex():
    assert multi_bracket_validation.multi_bracket_validation('[][Code][Fellows](())') is True
