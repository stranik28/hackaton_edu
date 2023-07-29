import string

import requests
import random
import datetime

base_url = "http://localhost:9999"  # Replace with your API base URL


def create_university(name: int, photos: list[str], address: list[int], speciality: list[int], phone: str, description: str):
    payload = {
        "name": name,
        "photos": photos,
        "address": address,
        "speciality": speciality,
        "phone": phone,
        "description": description
    }
    response = requests.post(f"{base_url}/university", json=payload)
    return response.json()


def create_speciality(name: str, code: str, description: str, test: list[int], exam: list[int], budget_place: int, price: int, paid_place: int):
    payload = {
        "name": name,
        "code": code,
        "description": description,
        "test": test,
        "exam": exam,
        "budget_place": budget_place,
        "price": price,
        "paid_place": paid_place
    }
    response = requests.post(f"{base_url}/speciality", json=payload)
    return response.json()


def create_address(region: str, city: str, street: str, building: str):
    payload = {
        "region": region,
        "city": city,
        "street": street,
        "building": building
    }
    response = requests.post(f"{base_url}/address", json=payload)
    return response.json()


def create_user(username: str, ege: list[int], number_of_univers: int, snils: str):
    payload = {
        "username": username,
        "ege": ege,
        "number_of_univers": number_of_univers,
        "snils": snils
    }
    response = requests.post(f"{base_url}/user", json=payload)
    return response.json()


def create_ege(exam: int, score: int):
    payload = {
        "exam": exam,
        "Score": score
    }
    response = requests.post(f"{base_url}/ege", json=payload)
    return response.json()


def create_exam(name: str):
    payload = {
        "name": name
    }
    response = requests.post(f"{base_url}/exam", json=payload)
    return response.json()


def create_type_question(name: str):
    payload = {
        "name": name
    }
    response = requests.post(f"{base_url}/type_question", json=payload)
    return response.json()


def create_answer(body: str, correct: bool):
    payload = {
        "body": body,
        "correct": correct
    }
    response = requests.post(f"{base_url}/type_question", json=payload)
    return response.json()


def create_question(name: str, body: str, answer: list[int], type: int):
    payload = {
        "name": name,
        "body": body,
        "answer": answer,
        "type": type
    }
    response = requests.post(f"{base_url}/type_question", json=payload)
    return response.json()

ege_sets = [
    [1, 2, 9],
    [1, 2, 7],
    [1, 2, 3],
    [1, 2, 8],
    [1, 2, 5],
    [1, 2, 11],
    [1, 3, 4],
    [1, 2, 5, 7],
    [1, 2, 6, 7],
    [1, 2, 3, 9]
]


def gen_snils():
    res = ''.join(random.choice(string.digits) for _ in range(14))
    res = '-'.join(res[i:i + 4] for i in range(0, len(res), 4))
    res = res[:-3] + ' ' + res[-3 + 1:]

    return res


def gen_users(n):
    return [{
        "username": ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(6, 10))),
        "ege": ege_sets[random.randint(0, len(ege_sets) - 1)],
        "number_of_univers": random.randint(1, 3),
        "snils": gen_snils()
    } for i in range(n)]


def add_users(n):
    for user in gen_users(n):
        create_user(**user)
        
def add_universities():
    for university in universities:
        create_speciality(**university)
        
        
def add_specialities():
    for speciality in specialties:
        create_speciality(**speciality)


def add_adresses():
    for address in addresses:
        create_address(**address)


def add_exams():
    for exam_name in exam_names:
        create_exam(**exam_name)


def add_eges(n):
    ege_set = ege_sets[random.randint(0, len(ege_sets) - 1)]
    for i in range(n):
        create_ege(exam=ege_set[0], score=random.randint(0, 100))
        create_ege(exam=ege_set[1], score=random.randint(0, 100))
        create_ege(exam=ege_set[2], score=random.randint(0, 100))


if __name__ == "__main__":
    specialties = [
        {
            "name": "Математика",
            "code": "01.03.01",
            "description": "Программа подготовки математиков.",
            "test": [3, 5],
            "exam": [1, 2],
            "budget_place": 20,
            "price": 150000,
            "paid_place": 50
        },
        {
            "name": "Информатика и вычислительная техника",
            "code": "09.03.01",
            "description": "Обучение программированию и разработке информационных систем.",
            "test": [2, 4],
            "exam": [1, 2, 9],
            "budget_place": 25,
            "price": 180000,
            "paid_place": 60
        },
        {
            "name": "Экономика",
            "code": "38.03.01",
            "description": "Изучение экономических процессов и явлений.",
            "test": [1, 3],
            "exam": [1, 2, 7],
            "budget_place": 30,
            "price": 160000,
            "paid_place": 70
        },
        {
            "name": "Архитектура",
            "code": "07.03.01",
            "description": "Проектирование и создание архитектурных сооружений.",
            "test": [5, 2],
            "exam": [1, 2, 3],
            "budget_place": 15,
            "price": 160000,
            "paid_place": 35
        },
        {
            "name": "Лингвистика",
            "code": "45.03.01",
            "description": "Изучение языков и их структуры.",
            "test": [4, 1],
            "exam": [1, 2, 11],
            "budget_place": 20,
            "price": 150000,
            "paid_place": 45
        },
        {
            "name": "Геология",
            "code": "05.03.01",
            "description": "Изучение структуры и состава Земли.",
            "test": [3, 5],
            "exam": [1, 2, 8],
            "budget_place": 18,
            "price": 170000,
            "paid_place": 40
        },
        {
            "name": "Электроэнергетика и электротехника",
            "code": "13.03.01",
            "description": "Изучение систем электроснабжения и электротехнических устройств.",
            "test": [2, 4],
            "exam": [1, 2, 3, 9],
            "budget_place": 25,
            "price": 180000,
            "paid_place": 55
        },
        {
            "name": "Журналистика",
            "code": "42.03.02",
            "description": "Обучение журналистской деятельности и медиа.",
            "test": [5, 3],
            "exam": [1, 2, 7],
            "budget_place": 12,
            "price": 140000,
            "paid_place": 30
        },
        {
            "name": "Психология",
            "code": "37.03.01",
            "description": "Изучение человеческого поведения и психических процессов.",
            "test": [1, 2],
            "exam": [1, 2, 5, 7],
            "budget_place": 20,
            "price": 155000,
            "paid_place": 40
        },
        {
            "name": "Социология",
            "code": "39.03.01",
            "description": "Изучение общественных процессов и социальных явлений.",
            "test": [3, 4],
            "exam": [1, 2, 5, 7],
            "budget_place": 18,
            "price": 160000,
            "paid_place": 35
        },
        {
            "name": "Философия",
            "code": "47.03.01",
            "description": "Изучение основных философских течений и проблем.",
            "test": [2, 3],
            "exam": [1, 2, 7, 6],
            "budget_place": 15,
            "price": 145000,
            "paid_place": 30
        },
        {
            "name": "Биотехнология",
            "code": "05.04.02",
            "description": "Применение биологических процессов для получения новых продуктов.",
            "test": [4, 5],
            "exam": [1, 2, 5],
            "budget_place": 18,
            "price": 170000,
            "paid_place": 35
        },
        {
            "name": "Химия",
            "code": "04.03.01",
            "description": "Изучение химических процессов и веществ.",
            "test": [1, 2],
            "exam": [1, 3, 4],
            "budget_place": 22,
            "price": 160000,
            "paid_place": 40
        }
    ]

    addresses = [
        {
            "region": "Московская область",
            "city": "Москва",
            "street": "ул. Колмогорова",
            "building": "1"
        },
        {
            "region": "Ленинградская область",
            "city": "Санкт-Петербург",
            "street": "Университетская набережная",
            "building": "7"
        },
        {
            "region": "Новосибирская область",
            "city": "Новосибирск",
            "street": "ул. Пирогова",
            "building": "2"
        },
        {
            "region": "Республика Татарстан",
            "city": "Казань",
            "street": "ул. Кремлевская",
            "building": "18"
        },
        {
            "region": "Ленинградская область",
            "city": "Санкт-Петербург",
            "street": "Политехническая улица",
            "building": "29"
        }
    ]

    universities = [
        {
            "name": "Московский государственный университет",
            "photos": ["https://upload.wikimedia.org/wikipedia/commons/b/b1/%D0%9C%D0%93%D0%A3%2C_%D0%B2%D0%B8%D0%B4_%D1%81_%D0%B2%D0%BE%D0%B7%D0%B4%D1%83%D1%85%D0%B0.jpg",
                       "https://smapse.ru/storage/2019/08/z1-39.jpg"],
            "address": [1],
            "speciality": [1, 3, 7],
            "phone": "+7 (495) 939-10-00",
            "description": "Один из старейших и наиболее престижных вузов России."
        },
        {
            "name": "Санкт-Петербургский государственный университет",
            "photos": ["https://econ.spbu.ru/sites/default/files/den_vypusknika.png",
                       "https://changellenge.com/upload/resize_cache/iblock/ebe/1240_600_2/ebef6377d5ebde8ed76f93a555f5f14b.jpg"],
            "address": [2],
            "speciality": [2, 5, 8],
            "phone": "+7 (812) 328-32-91",
            "description": "Один из крупнейших классических университетов страны."
        },
        {
            "name": "Новосибирский государственный университет",
            "photos": ["https://studyinrussia.ru/upload/iblock/88d/88da0720506ca55eb1d23c6fa46f8e3a.jpg",
                       "https://ksonline.ru/wp-content/uploads/2019/10/Bezymyannyj-3.jpg"],
            "address": [3],
            "speciality": [3, 6, 9],
            "phone": "+7 (383) 363-30-13",
            "description": "Лидер в области естественных наук и математики."
        },
        {
            "name": "Казанский федеральный университет",
            "photos": ["https://media.kpfu.ru/sites/default/files/2021-10/IMG_2217_0.jpg",
                       "https://media.kpfu.ru/sites/default/files/2021-03/IMG_2784.jpg"],
            "address": [4],
            "speciality": [4, 7, 10],
            "phone": "+7 (843) 233-70-90",
            "description": "Один из крупнейших университетов России с богатой историей."
        },
        {
            "name": "Санкт-Петербургский политехнический университет",
            "photos": ["https://www.spbstu.ru/upload/medialibrary/37d/106.jpg",
                       "https://alfakom.uz/images/img/partners/spbstu_1.jpg"],
            "address": [5],
            "speciality": [5, 8, 13],
            "phone": "+7 (812) 552-99-24",
            "description": "Один из ведущих политехнических университетов России."
        }
    ]

    users = [
        {
            "username": "user1",
            "ege": [1, 2, 3],
            "number_of_univers": 4,
            "snils": "123-456-789 12"
        },
        {
            "username": "user2",
            "ege": [4, 5, 6],
            "number_of_univers": 3,
            "snils": "195-654-321 34"
        },
        {
            "username": "user3",
            "ege": [7, 8, 9],
            "number_of_univers": 2,
            "snils": "111-176-333 56"
        },
        {
            "username": "user4",
            "ege": [10, 11, 12],
            "number_of_univers": 5,
            "snils": "444-153-666 78"
        },
        {
            "username": "user5",
            "ege": [13, 14, 15],
            "number_of_univers": 3,
            "snils": "294-888-178 90"
        },
        {
            "username": "user889876",
            "ege": [16, 17, 18],
            "number_of_univers": 4,
            "snils": "123-294-789 12"
        },
        {
            "username": "user8",
            "ege": [19, 20, 21],
            "number_of_univers": 5,
            "snils": "987-654-928 34"
        },
        {
            "username": "uFAser3",
            "ege": [22, 23, 24],
            "number_of_univers": 2,
            "snils": "291-222-333 56"
        },
        {
            "username": "user99",
            "ege": [25, 26, 27],
            "number_of_univers": 5,
            "snils": "444-555-678 78"
        },
        {
            "username": "user10",
            "ege": [28, 29, 30],
            "number_of_univers": 3,
            "snils": "777-472-999 90"
        }
    ]

    exam_names = [
        "Русский язык",
        "Математика",
        "Физика",
        "Химия",
        "Биология",
        "История",
        "Обществознание",
        "География",
        "Информатика",
        "Литература",
        "Иностранный язык"
    ]

    add_exams()
    add_eges(100)
    add_users(100)

    add_specialities()
    add_adresses()
    add_universities()
