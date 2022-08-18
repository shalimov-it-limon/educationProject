import pytest
from conf import param_test


def strange_string_funk(str):
    if len(str) > 5:
        return str + "?"
    elif len(str) < 5:
        return str + '!'
    else:
        return str + '.'


def test_strange_string_funk(param_test):
    (input, expected_output) = param_test
    result = strange_string_funk(input)
    print('input: {0}, output: {1}, expected {2}'.format(input, result, expected_output))
    assert result == expected_output


def calc(x):
    return (10 ** x) + x
