import pytest

# 14.06.22.
@pytest.fixture
def fix():
    input_pet = {
        "id": 219,
        "category": {
            "id": 25,
            "name": "Vrapp"
        },
        "name": "BOOGY",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 14,
                "name": "string"
            }
        ],
        "status": "available"
    }

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}
    return input_pet, header
# ____________________
# Параметризация


@pytest.fixture(scope='function', params=[
    ('abcdefg', 'abcdefg?'),
    ('abc', 'abc!'),
    ('abcde', 'abcde.')
])
def param_test(request):
    return request.param
