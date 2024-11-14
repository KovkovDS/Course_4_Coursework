# Импортируем фреймворк для тестирования кода
import pytest

# Импортируем тестируемую функцию из файла auxiliary_func.py
from src.func.auxiliary_func import end_word_question


@pytest.fixture
def test_count_services_1():
    return len(['HeadHunter', 'Superjob'])


@pytest.fixture
def test_count_services_2():
    return len(['HeadHunter1', 'Superjob1', 'HeadHunter2', 'HeadHunter3', 'Superjob2', 'Superjob3'])


@pytest.fixture
def test_count_services_3():
    return len(['HeadHunter'])


def test_end_word_question(test_count_services_1, test_count_services_2, test_count_services_3):
    assert end_word_question(test_count_services_1) == 'сайтов'
    assert end_word_question(test_count_services_2) == 'сайтов'
    assert end_word_question(test_count_services_3) == 'сайта'
