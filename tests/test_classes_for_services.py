# Импортируем фреймворк для тестирования кода
import pytest

# Импортируем классы объектов из файла classes_for_services.py
from src.from_api_integration.classes_for_services import HeadHunterAPI, SuperJobAPI


@pytest.fixture()
def hh_params_for_request():
    return HeadHunterAPI()


@pytest.fixture()
def sj_params_for_request():
    return SuperJobAPI()


@pytest.fixture()
def example_answers_yes():
    return 'да'


@pytest.fixture()
def example_answers_no():
    return 'нет'


@pytest.fixture()
def example_answers_any():
    return ''


@pytest.fixture()
def example_answers_no2():
    return 'нет'


@pytest.fixture()
def keyword_for_get_vacancies():
    return 'python'


@pytest.fixture()
def keyword_for_get_vacancies1():
    return 'сантехник'


@pytest.fixture()
def part_response_for_request_hh():
    return {'name': 'Backend разработчик', 'link': 'https://hh.ru/vacancy/108828750', 'city': 'Москва',
            'salary_from': 90000, 'salary_to': None, 'currency': 'RUR', 'experience': 'От 1 года до 3 лет',
            'busy': 'Полная занятость', 'schedule': 'Полный день',
            'requirements': 'Знание SQL. Опыт проектирования БД от 1 года. Опыт работы с какой либо СУБД (желательно '
                            'PostgreSQL). Навыки алгоритмизации. ',
            'duties': 'Анализ задач и проектирование под них БД. Разработка бизнес логики под требования компании '
                      '(имеется собственная платформа). Внедрение и поддержка новых...'}


@pytest.fixture()
def part_response_for_request_hh1():
    return {'name': 'Бармен в ресторан', 'link': 'https://hh.ru/vacancy/109468226', 'city': 'Алматы',
            'salary_from': 500000, 'salary_to': None, 'currency': 'KZT', 'experience': 'От 1 года до 3 лет',
            'busy': 'Полная занятость', 'schedule': 'Полный день',
            'requirements': 'Опыт работы от 2-х лет. Работоспособный (бережное отношение к ресторанному имуществу). '
                            'Пунктуальный. Желание развиваться и расти вместе с нами!',
            'duties': 'Приготовление напитков из барного меню ресторана. Разлив пива. Уход за барной стойкой.'}


@pytest.fixture()
def part_response_for_request_hh2():
    return {'name': 'Слесарь - сантехник', 'link': 'https://hh.ru/vacancy/109181768', 'city': 'Алматы',
            'salary_from': 250000, 'salary_to': None, 'currency': 'KZT', 'experience': 'Нет опыта',
            'busy': 'Полная занятость', 'schedule': 'Полный день', 'requirements': 'Знание города.',
            'duties': 'Мелкосрочный ремонт, связанный с ремонтом канализации, водопровода и отопления.'}


@pytest.fixture()
def part_response_for_request_sj():
    return {'name': 'Слесарь-сборщик ёмкостного оборудования',
            'link': 'https://elektrostal.superjob.ru/vakansii/slesar-sborschik-jomkostnogo-oborudovaniya-46272671.html',
            'city': 'Электросталь', 'salary_from': 2500, 'salary_to': 3500, 'currency': 'rub',
            'experience': 'От 3 лет', 'busy': 'Полный рабочий день', 'requirements': 'None', 'duties': 'None'}


@pytest.fixture()
def part_response_for_request_sj1():
    return {'name': 'Учитель информатики',
            'link': 'https://zheleznodorozhniy.superjob.ru/vakansii/uchitel-informatiki-36344427.html',
            'city': 'Железнодорожный', 'salary_from': 50000, 'salary_to': 0, 'currency': 'rub',
            'experience': 'Без опыта', 'busy': 'Полный рабочий день',
            'requirements': 'С 1 сентября 2024 года. \nОбязанности:\n• Осуществляет обучение и воспитание обучающихся '
                            'с учетом специфики преподаваемого предмета, проводит уроки и другие занятия в соответствии'
                            ' с расписанием.\n• В своей работе по предмету использует разнообразные приемы, методы и '
                            'средства обучения.\n• Реализует образовательные программы.\n• Подготовка обучающихся к '
                            'сдаче ГИА и участию в олимпиадах и конкурсах.\n• Ведение дополнительных занятий и '
                            'факультативов. \n• Программирование: Перволого/Логомиры, Scratch, Кумир, Паскаль/Дельфи, '
                            'C/C++, Python\nСАПР: Компас, AutoCAD CorelDRAW и др.\nВеб-дизайн и разработка: JavaScript,'
                            ' Adobe Photoshop, Flash.\nАдминистрирование: Windows, Linux\nУсловия:\n• Выплата '
                            'компенсации за аренду жилья (при отсутствии недвижимости в Московской области)\n• '
                            'Помощь в устройстве детей в дошкольные или школьные учреждения города.', 'duties': 'None'}


@pytest.fixture()
def part_response_for_request_sj2():
    return {'name': 'Слесарь-сантехник', 'link': 'https://ufa.superjob.ru/vakansii/slesar-santehnik-50095010.html',
            'city': 'Уфа', 'salary_from': 130000, 'salary_to': 130000, 'currency': 'rub', 'experience': 'От 1 года',
            'busy': 'Работа вахтовым методом',
            'requirements': 'Обязанности:\n• Разборка, ремонт и сборка сложных деталей и узлов санитарно-технических '
                            'систем центрального отопления, водоснабжения, канализации и водостоков\nДолжен знать:\n• '
                            'Устройство и способы ремонта различных санитарно-технических трубопроводных систем;\n• '
                            'Способы установления дефектных мест при испытании трубопроводов.\nУсловия:\n• Официальное'
                            ' трудоустройство согласно ТК РФ;\n• Вахтовый метод 60/60;\n• Стабильная заработная плата '
                            '2 раза в месяц;\n• Проживание в вахтовом поселке;\n• Оплата билетов;\n• '
                            'Выдача спецодежды', 'duties': 'None'}


def test_params(hh_params_for_request, sj_params_for_request, example_answers_yes, example_answers_no,
                example_answers_any, example_answers_no2):
    hh_params_for_request.params = example_answers_yes
    assert hh_params_for_request.params == {'text': '', 'per_page': 20}
    hh_params_for_request.params = example_answers_any
    assert hh_params_for_request.params == {'text': '', 'per_page': 20}
    hh_params_for_request.params = example_answers_no
    assert hh_params_for_request.params == {'text': '', 'per_page': 20, 'only_with_salary': True}
    hh_params_for_request.params = example_answers_no2
    assert hh_params_for_request.params == {'text': '', 'per_page': 20, 'only_with_salary': True}
    hh_params_for_request.params = example_answers_yes
    assert sj_params_for_request.params == {'keyword': '', 'count': 20}
    sj_params_for_request.params = example_answers_any
    assert sj_params_for_request.params == {'keyword': '', 'count': 20}
    sj_params_for_request.params = example_answers_no
    assert sj_params_for_request.params == {'keyword': '', 'count': 20, 'no_agreement': 1}
    sj_params_for_request.params = example_answers_no2
    assert sj_params_for_request.params == {'keyword': '', 'count': 20, 'no_agreement': 1}


def test_get_vacancies_hh(hh_params_for_request, part_response_for_request_hh, part_response_for_request_hh1,
                          part_response_for_request_hh2, keyword_for_get_vacancies, keyword_for_get_vacancies1,
                          example_answers_any):
    requests_hh = hh_params_for_request
    assert part_response_for_request_hh in requests_hh.get_vacancies(keyword_for_get_vacancies)
    assert part_response_for_request_hh1 in requests_hh.get_vacancies(example_answers_any)
    assert part_response_for_request_hh2 in requests_hh.get_vacancies(keyword_for_get_vacancies1)


def test_get_vacancies_sj(sj_params_for_request, part_response_for_request_sj, part_response_for_request_sj1,
                          part_response_for_request_sj2, keyword_for_get_vacancies, keyword_for_get_vacancies1,
                          example_answers_any):
    requests_sj = sj_params_for_request
    assert part_response_for_request_sj in requests_sj.get_vacancies(example_answers_any)
    assert part_response_for_request_sj1 in requests_sj.get_vacancies(keyword_for_get_vacancies)
    assert part_response_for_request_sj2 in requests_sj.get_vacancies(keyword_for_get_vacancies1)
