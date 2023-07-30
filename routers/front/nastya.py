from fastapi import APIRouter

router = APIRouter(prefix="/moc", tags=["moc"])


@router.get("/creditCardsData")
async def all_address():
    return [
        {
            "imageSrc": "https://rcbc.ru/wp-content/uploads/2021/09/i-20-1024x669.webp",
            "title": "Сбербанк (потребительский кредит)",
            "description": "120 000 на 2 года по 5000 в месяц",
        },
        {
            "imageSrc": "https://the-golden-calf.com/upload/iblock/18d/v7u12ed9yh303zh0dvv38l71crljrm3d.jpg",
            "title": "Альфа (кредитная карта)",
            "description": "90 дней без процентов, потом платеж по 4900",
        },
        {
            "imageSrc": "https://filearchive.cnews.ru/img/book/2021/12/28/pasted-image-0.png",
            "title": "Тинькоф (рассрочка)",
            "description": "Плати равными долями 11 000 в месяц, переплата за год 10%",
        }
    ]


@router.get("/cards_1")
async def all_address():
    return [
        {
            "image": "http://ulpravda.ru/pictures/news/big/119060_big.jpg",
            "number": 1234,
            "title": "Образование и педагогика",
            "link": "/education"
        },
        {
            "image": "https://kartinki.pibig.info/uploads/posts/2023-04/1681142386_kartinki-pibig-info-p-kartinki-dlya-nauchnoi-prezentatsii-arti-68.jpg",
            "number": 567,
            "title": "Медицина и здравоохранение",
            "link": "/medicine"
        },
        {
            "image": "https://inring.ru/images/detailed/4/3849144.jpg",
            "number": 890,
            "title": "Инженерия и технологии",
            "link": "/engineering"
        }
    ]


@router.get("/specialities_1")
async def all_address():
    return [
        {
            "image": "http://ulpravda.ru/pictures/news/big/119060_big.jpg",
            "number": 1234,
            "title": "Инноватика",
            "link": "/education"
        },
        {
            "image": "https://kartinki.pibig.info/uploads/posts/2023-04/1681142386_kartinki-pibig-info-p-kartinki-dlya-nauchnoi-prezentatsii-arti-68.jpg",
            "number": 567,
            "title": "Дизайн",
            "link": "/medicine"
        },
        {
            "image": "https://inring.ru/images/detailed/4/3849144.jpg",
            "number": 890,
            "title": "Химия",
            "link": "/engineering"
        }
    ]


@router.get("/universities_1")
async def all_address():
    return [
        {
            "image": "https://static.rustore.ru/apk/1816534207/content/ICON/d289ec11-2dde-4b64-92df-88dd36f4457b.jpg",
            "number": "Краснодар",
            "title": "Кубанский государственный университет",
            "link": "/education"
        },
        {
            "image": "https://education-in-russia.com/static/universities_logo/b/c/7/bc7fc029ed003308733e87ace210db0b.jpeg",
            "number": "Краснодар",
            "title": "Кубанский государственный технологический университет",
            "link": "/medicine"
        },
        {
            "image": "https://sun6-22.userapi.com/s/v1/ig2/pr-eZOfQq0Uv7NKdiCFoHrTtG_9pNOmKawEURtmqSrqyqdFrSSlOsVnSvnsKCmoFuwr47XF2MNTvnrOWlU9H2xJ6.jpg?size=1250x1251&quality=95&crop=0,0,1250,1251&ava=1",
            "number": "Сочи",
            "title": "Сириус",
            "link": "/engineering"
        }
    ]


@router.get("/specialities_2")
async def all_address():
    return [
        {
            "image": "http://ulpravda.ru/pictures/news/big/119060_big.jpg",
            "number": 1234,
            "title": "Инноватика",
            "link": "/education"
        },
        {
            "image": "https://kartinki.pibig.info/uploads/posts/2023-04/1681142386_kartinki-pibig-info-p-kartinki-dlya-nauchnoi-prezentatsii-arti-68.jpg",
            "number": 567,
            "title": "Дизайн",
            "link": "/medicine"
        },
        {
            "image": "https://inring.ru/images/detailed/4/3849144.jpg",
            "number": 890,
            "title": "Химия",
            "link": "/engineering"
        }
    ]


@router.get("/specialities_3")
async def all_address():
    return [
        {
            "image": "http://ulpravda.ru/pictures/news/big/119060_big.jpg",
            "number": 1234,
            "title": "Инноватика",
            "link": "/education"
        },
        {
            "image": "https://kartinki.pibig.info/uploads/posts/2023-04/1681142386_kartinki-pibig-info-p-kartinki-dlya-nauchnoi-prezentatsii-arti-68.jpg",
            "number": 567,
            "title": "Дизайн",
            "link": "/medicine"
        },
        {
            "image": "https://inring.ru/images/detailed/4/3849144.jpg",
            "number": 890,
            "title": "Химия",
            "link": "/engineering"
        }
    ]


@router.get("/universities_2")
async def all_address():
    return [
        {
            "image": "https://static.rustore.ru/apk/1816534207/content/ICON/d289ec11-2dde-4b64-92df-88dd36f4457b.jpg",
            "number": "Краснодар",
            "title": "Кубанский государственный университет",
            "link": "/education"
        },
        {
            "image": "https://education-in-russia.com/static/universities_logo/b/c/7/bc7fc029ed003308733e87ace210db0b.jpeg",
            "number": "Краснодар",
            "title": "Кубанский государственный технологический университет",
            "link": "/medicine"
        },
        {
            "image": "https://sun6-22.userapi.com/s/v1/ig2/pr-eZOfQq0Uv7NKdiCFoHrTtG_9pNOmKawEURtmqSrqyqdFrSSlOsVnSvnsKCmoFuwr47XF2MNTvnrOWlU9H2xJ6.jpg?size=1250x1251&quality=95&crop=0,0,1250,1251&ava=1",
            "number": "Сочи",
            "title": "Сириус",
            "link": "/engineering"
        }

    ]


@router.get("/cards_2")
async def all_address():
    return [
        {
            "image": "https://static.rustore.ru/apk/1816534207/content/ICON/d289ec11-2dde-4b64-92df-88dd36f4457b.jpg",
            "number": "Краснодар",
            "title": "Кубанский государственный университет",
            "link": "/education"
        },
        {
            "image": "https://education-in-russia.com/static/universities_logo/b/c/7/bc7fc029ed003308733e87ace210db0b.jpeg",
            "number": "Краснодар",
            "title": "Кубанский государственный технологический университет",
            "link": "/medicine"
        },
        {
            "image": "https://sun6-22.userapi.com/s/v1/ig2/pr-eZOfQq0Uv7NKdiCFoHrTtG_9pNOmKawEURtmqSrqyqdFrSSlOsVnSvnsKCmoFuwr47XF2MNTvnrOWlU9H2xJ6.jpg?size=1250x1251&quality=95&crop=0,0,1250,1251&ava=1",
            "number": "Сочи",
            "title": "Сириус",
            "link": "/engineering"
        }
    ]


@router.get("/newsData")
async def all_address():
    return [
        {
            "id": 1,
            "title": "Важное объявление",
            "date": "2023-07-28",
            "content": "Зачислены первые студенты в вузы...",
        },
        {
            "id": 2,
            "title": "Новая программа стипендий",
            "date": "2023-07-25",
            "content": "Для многодетных семей будет...",
        },
    ]


@router.get("/admissionDates")
async def all_address():
    return [
        {
            id: 1,
            "title": "Крайний срок подачи заявлений",
            "date": "2023-08-15",
        },
        {
            id: 2,
            "title": "День ориентации",
            "date": "2023-09-01",
        },
    ]


@router.get("/questions_1")
async def all_address():
    return [
        {
            "question": "Какой вид искусства вам нравится больше всего?",
            "options": ["Живопись", "Музыка", "Театр", "Литература", "Танцы"],
        },
        {
            "question": "Какое мероприятие вы предпочитаете?",
            "options": ["Концерт", "Выставка", "Премьера спектакля", "Книжный вечер", "Танцевальный бал"],
        },
        {
            "question": "Какие путешествия вам более интересны?",
            "options": ["Городские туры", "Походы в горы", "Поездки на море", "Путешествия за границу",
                        "Путешествия по стране"],
        },
    ]


@router.get("/subjects_1")
async def all_address():
    return [
        {
            "subject": "Искусство и культура",
            "description": "Изучение искусства, истории и культуры различных народов и эпох. Работа в музеях, галереях и культурных учреждениях.",
            "image": "art.jpg",
        },
        {
            "subject": "Музыка и пение",
            "description": "Изучение музыкальной теории, игры на инструментах и пения. Карьера музыканта, певца или музыкального продюсера.",
            "image": "music.jpg",
        },
        {
            "subject": "Театр и актерское искусство",
            "description": "Обучение актерскому мастерству и театральному искусству. Работа на театральной сцене или в киноиндустрии.",
            "image": "theater.jpg",
        },
        {
            "subject": "Литература и писательство",
            "description": "Изучение литературных произведений и техник писательского мастерства. Карьера писателя, редактора или литературного критика.",
            "image": "literature.jpg",
        },
        {
            "subject": "Танцы и хореография",
            "description": "Обучение хореографии и танцевальному искусству. Работа танцора, хореографа или инструктора по танцам.",
            "image": "dance.jpg",
        },
    ]


@router.get("/subjects_2")
async def all_address():
    return [
        ["Русский язык", "Математика", "Иностранный язык"],
        ["Биология", "География", "Химия"],
        ["Обществознание", "Информатика", "Литература"],
        ["Физика"],
    ]


@router.get("/")
async def all_address():
    return []


@router.get("/specialities_4")
async def all_address():
    return [
        {
            "title": "Инноватика",
            "requiredSubjects": ["Математика", "Иностранный язык", "Информатика"],
            "minimumScore": 150,
            "image": "http://ulpravda.ru/pictures/news/big/119060_big.jpg"
        },
        {
            "title": "Системный анализ и управление",
            "requiredSubjects": ["Математика", "Иностранный язык", "Информатика"],
            "minimumScore": 150,
            "image": "http://ulpravda.ru/pictures/news/big/119060_big.jpg"
        },
        {
            "title": "Electrical Engineering",
            "requiredSubjects": ["Математика", "Физика"],
            "minimumScore": 140,
        },
        {
            "title": "Medicine",
            "requiredSubjects": ["Биология", "Химия"],
            "minimumScore": 180,
        },
    ]


@router.get("/careerDirections")
async def all_address():
    return [
        {
            "direction": "Точные науки",
            "description":
                "Точные науки — это научные дисциплины, основанные на строгой логике и математических методах. Они занимаются изучением количественных закономерностей и развивают аналитическое мышление. Сюда входят математика и физика, которые являются основой для многих технологий и научных исследований.",
            "specialties": ["Инноватика", "Физика", "Математика"],
        },
        {
            "direction": "Естественные науки",
            "description":
                "Естественные науки изучают природные явления и процессы, которые происходят в живой и неживой природе. Они помогают понять законы природы, функционирование организмов и экосистем, а также разрабатывать новые лекарства и технологии. В эту область входят химия и биология.",
            "specialties": ["Химик", "Биолог"],
        },
        {
            "direction": "Информатика",
            "description":
                "Информатика — это наука о методах и процессах обработки информации с помощью компьютеров. Она занимается разработкой программного обеспечения, искусственным интеллектом, базами данных и другими технологиями. Информатика имеет множество применений в различных сферах жизни и бизнеса.",
            "specialties": ["Информатика"],
        },
        {
            "direction": "Гуманитарные науки",
            "description":
                "Гуманитарные науки изучают человека, его культуру, историю и общество. Они помогают понять различные аспекты человеческой деятельности, искусства, языка и общественных отношений. Гуманитарные науки играют важную роль в формировании культурного наследия и понимании нашего прошлого и настоящего.",
            "specialties": ["Литература", "История", "Иностранные языки"],
        },
    ]
