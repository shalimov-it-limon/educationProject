import pytest
from datetime import datetime

@pytest.fixture()
def some_data():
    return 42

def test_some_data(some_data):
    assert some_data == 42

print(some_data)

@pytest.fixture(autouse=True):
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print (f"\nТест шел: {end_time - start_time}")


@pytest.fixture(scope="class", autouse=True)
def session_fixture():
    print("\nclass fixture starts")


@pytest.fixture(scope="function", autouse=True)
def function_fixture():
    print("\nfunction fixture starts")


class TestClass23:

    def test_first(self):
        pass


def test_second(self):
    pass


@pytest.fixture()
def request_fixture(request):
    print(request.fixturename)
    print(request.scope)
    print(request.function.__name__)
    print(request.cls)
    print(request.module.__name__)
    print(request.fspath)
    if request.cls:
        return f"\n У теста {request.function.__name__} класс есть\n"
    else:
        return f"\n У теста {request.function.__name__} класса нет\n"


def test_request_1(request_fixture):
    print(request_fixture)


class TestClassRequest:

    def test_request_2(self, request_fixture):
        print(request_fixture)