import asyncio
from app.core.db import AsyncSessionLocal
from app.db.models import Question, Topic, User


async def seed_questions(user_id: int, topic_id: int):
    questions_data = [
        {"text": "Что такое переменная в Python и как её объявить?", "answer": "Переменная — это имя, ссылающееся на значение в памяти. Объявляется присваиванием: x = 10.", "difficulty": 1},
        {"text": "Чем отличается список (list) от кортежа (tuple)?", "answer": "Список изменяемый (mutable), кортеж — нет (immutable).", "difficulty": 2},
        {"text": "Что такое PEP8?", "answer": "Это набор правил оформления кода в Python.", "difficulty": 1},
        {"text": "Что такое тип данных dict?", "answer": "Словарь — структура данных для хранения пар ключ:значение.", "difficulty": 1},
        {"text": "Как работает оператор 'is' в Python?", "answer": "Он сравнивает идентичность объектов (находятся ли они по одному адресу в памяти).", "difficulty": 2},
        {"text": "Что делает функция range()?", "answer": "Создает последовательность чисел, обычно используется в циклах for.", "difficulty": 1},
        {"text": "Чем отличается оператор '==' от 'is'?", "answer": "'==' сравнивает значения, 'is' — идентичность объектов.", "difficulty": 2},
        {"text": "Что делает метод list.append()?", "answer": "Добавляет элемент в конец списка.", "difficulty": 1},
        {"text": "Что делает оператор *args и **kwargs в функциях?", "answer": "*args собирает позиционные аргументы, **kwargs — именованные.", "difficulty": 3},
        {"text": "Что такое list comprehension?", "answer": "Это краткий синтаксис для создания списка: [x*2 for x in range(5)].", "difficulty": 2},
        {"text": "Что делает конструкция try/except?", "answer": "Позволяет обрабатывать исключения, предотвращая падение программы.", "difficulty": 2},
        {"text": "Что делает оператор 'with'?", "answer": "Он управляет контекстом выполнения, автоматически закрывая ресурсы (например, файлы).", "difficulty": 3},
        {"text": "Что такое генератор (generator) в Python?", "answer": "Это функция, возвращающая итератор через 'yield', не хранящая все значения в памяти.", "difficulty": 3},
        {"text": "Что делает функция enumerate()?", "answer": "Возвращает пары (индекс, значение) при итерировании последовательности.", "difficulty": 1},
        {"text": "Что делает функция zip()?", "answer": "Объединяет несколько итерируемых объектов в кортежи.", "difficulty": 2},
        {"text": "Что такое декоратор в Python?", "answer": "Функция, которая принимает другую функцию и изменяет её поведение.", "difficulty": 4},
        {"text": "Как работает оператор 'global'?", "answer": "Позволяет функции изменять переменные, объявленные вне её области видимости.", "difficulty": 3},
        {"text": "Что такое модуль и пакет в Python?", "answer": "Модуль — это .py файл, пакет — директория с __init__.py, содержащая модули.", "difficulty": 2},
        {"text": "Что делает функция isinstance()?", "answer": "Проверяет, является ли объект экземпляром указанного класса или его наследников.", "difficulty": 1},
        {"text": "Чем отличаются shallow copy и deep copy?", "answer": "Shallow copy копирует только верхний уровень объекта, deep copy — полностью рекурсивно.", "difficulty": 4},
    ]

    async with AsyncSessionLocal() as session:
        user = await session.get(User, user_id)
        if not user:
            new_user = User(
                username="admin",
                email="admin@example.com",
                password_hash="",
            )
            new_user.set_password("admin123")
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            user_id = new_user.id

        topic = await session.get(Topic, topic_id)
        if not topic:
            topic = Topic(title="Основы Python", user_id=user_id)
            session.add(topic)
            await session.commit()
            await session.refresh(topic)
            topic_id = topic.id  # обновляем ID

        session.add_all([
            Question(
                text=q["text"],
                answer=q["answer"],
                difficulty=q["difficulty"],
                user_id=user_id,
                topic_id=topic_id,
            ) for q in questions_data
        ])
        await session.commit()

        print("✅ 20 вопросов успешно добавлены в базу данных!")


if __name__ == "__main__":
    asyncio.run(seed_questions(1, 1))
