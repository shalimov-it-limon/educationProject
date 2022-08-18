import pytest
from test_config import param_test


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


@pytest.mark.parametrize('x', [1, 2, 3, 4, 5, 6])
def test_no_1(x):
    print(calc(x))
