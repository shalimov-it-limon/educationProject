import sys
import pytest


@pytest.mark.skip(reason="Баг в продукте - <ссылка>")
def test_one():   # Это наш тест, который находит тот самый баг
    pass


@pytest.mark.skipif(sys.version_info < (3, 6), reason="Тест требует python версии 3.6 или выше")
def test_python36_and_greater():
    pass