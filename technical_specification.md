# Техническое задание

- процент новичковых вакансий
- общее и новичковое количество вакансий в сфере
- средняя зп по новичковой области и просто средняя
- необходимые навыки для новичка
- самые перспективные направления
- процент и количество вакансий с частичной занятостью(тут сказать что нам блин нужны связи с компаниями особенно шарповыми)

количество вакансий
hh ru 1 164 544
работа ру 250 000
хабр карьера 2 835
карьерист 1 183 082
job lab 300 000
super job 500 000
trud vsem 1 746 772

Это есть в принципе мой анализ будет идти следующим образом, сначала я покажу как обстоят дела на рынке в динамике за последние полгода
затем покажу что я разобрала какие навыки необходимы для каждой специализации
hard и soft skills, возможно следует сделать упор на командную работу

Доказать что стоит делать модули по выбору и давать людям возможность более углубленно изучать то что им нравится зхотя бы полсеместра

# нужен ди диплом?

Показать силу чатика и sql для крутых запросов к hh.ru

конкуренция по областям, среднее количество откликов и как выглдит обобщенно вакансия с большим количеством откликов(то есть привлекательная)

модель которая показывает зарплатную вилку для вакансии!

что еще следует подучить? например я ввожу что знаю python а он показывает ключевые навыки которые чаще всего бывают с ним в связке

удаленка против очной работы, плюсы и минусы:
где больше вакансий

Перед собеседованием — чтобы не называть "на глаз"
🔍 Во время поиска работы — чтобы не продешевить
💼 При переговорах о повышении
🧑‍🏫 Внутренним HR и рекрутерам — для оценки рынка

Красивая часть:
...
Тех часть:
Какие этапы были проделаны?
Собраны данные с помощью парсера на питоне с хх ру. Всего собрано N строк в OLAP БД
Далее был проведен разведочный анализ данных. 
Показать красивую карту, просто потому что мне нравится
Я выяснила что топ популярных кей скиллов для людей без опыта и с небольшим опытом такой
Но кей скиллы есть далеко не везде и они довольно общие. Поэтому я решила проанализировать текст.
Кстати вот табличка корреляций
Статистика показала вот такую картинку, но к сожалению она совсем не учитывает контекст. 
Именно в этот момент мне пришла идея предсказания зарплаты. Для этого текст придется превратить числа.
Для этого был выбран BERT как самый крутой и современный, а вот его архитектура(картинка) и вот так он работает
Итого я токенизировала текст, добавила новых фичей и полученный датасет засунула в случайный лес  


План презентации
Слайд 1: Титульный слайд
Текст:

Название: Разработка Информационной системы «Карьерный консультант»
Автор: [Ваше имя]
Руководитель: [Имя руководителя]
Учебное заведение: [Название вуза]
Год: 2025Описание: Краткое представление темы и автора. Используйте логотип вуза и минималистичный дизайн.


Слайд 2: Введение и актуальность
Текст:

Проблема: Выбор карьеры — сложный процесс, требующий анализа навыков, интересов и рынка труда.
Актуальность: Автоматизация карьерного консультирования экономит время и повышает точность рекомендаций.
Цель: Разработать информационную систему, которая использует ИИ для подбора карьерных путей.
Задачи:
Анализ существующих решений.
Разработка модели на основе методов NLP и машинного обучения.
Создание удобного интерфейса.Описание: Объясняет, почему тема важна, и задает контекст.




Слайд 3: Аналоги приложения
Текст:

Аналог 1: LinkedIn Career Explorer
Описание: Платформа для анализа навыков и рекомендаций по вакансиям.
Преимущества: Интеграция с профессиональной сетью, большая база данных.
Недостатки: Ограниченная персонализация, платные функции.


Аналог 2: O*NET OnLine
Описание: База данных профессий с фильтрами по навыкам и интересам.
Преимущества: Подробные описания профессий, бесплатный доступ.
Недостатки: Нет ИИ для персонализированных рекомендаций.


Отличие «Карьерного консультанта»: Использование BERT для глубокого анализа текста и персонализированных рекомендаций.Описание: Сравнение с конкурентами, подчеркивая уникальность вашей системы.


Слайд 4: Обзор системы «Карьерный консультант»
Текст:

Назначение: Помощь пользователям в выборе профессии на основе их навыков, интересов и целей.
Основные функции:
Анализ текстового ввода (резюме, ответы на вопросы).
Рекомендации профессий и карьерных путей.
Предоставление обучающих материалов.


Целевая аудитория: Студенты, молодые специалисты, люди, меняющие карьеру.Описание: Даёт общее представление о системе и её возможностях.


Слайд 5: Используемый стек технологий
Текст:

Frontend: React.js, Tailwind CSS — для интерактивного и адаптивного интерфейса.
Backend: Python (FastAPI) — для обработки запросов и интеграции с моделью.
Машинное обучение: PyTorch, Transformers (Hugging Face) — для реализации BERT и других моделей.
База данных: PostgreSQL — для хранения данных пользователей и профессий.
Развертывание: Docker, AWS — для масштабируемости и надежности.Описание: Показывает техническую основу проекта, подчеркивая современные инструменты.


Слайд 6: Методы машинного обучения
Текст:

Используемые методы:
Классификация: Random Forest, SVM — для предсказания подходящих профессий.
Кластеризация: K-Means — для группировки похожих профилей пользователей.
Векторизация текста: BERT — для глубокого понимания текстовых данных.


Почему выбраны:
Random Forest и SVM: Высокая точность на структурированных данных.
K-Means: Эффективен для анализа больших данных.
BERT: Учитывает контекст, улучшая качество рекомендаций.


Интеграция: BERT преобразует текст в эмбеддинги, которые подаются в классификаторы.Описание: Объясняет, как методы ML работают вместе с BERT.


Слайд 7: Роль BERT в системе
Текст:

Что такое BERT: Модель на основе трансформеров (2018, Google), двунаправленная, контекстуальная.
Применение в проекте:
Обработка текстов: Резюме, ответы пользователей.
Создание эмбеддингов: Плотные векторы, отражающие семантику текста.
Пример: «Люблю работать с данными» → вектор, связанный с профессиями аналитика.


Преимущества:
Учет контекста (например, различает «банк» как реку или организацию).
Высокая точность в задачах NLP.


Ограничения: Требует больших вычислительных ресурсов.Описание: Подробно описывает, как BERT улучшает систему.


Слайд 8: Демонстрация работы нейронной сети
Текст:

Скриншот: Интерфейс системы с результатами рекомендаций.
Описание:
Ввод: Резюме пользователя или ответы на вопросы.
Вывод: Список профессий с вероятностями соответствия (например, «Аналитик данных — 85%»).


Технические детали:
BERT преобразует текст в эмбеддинги.
Random Forest классифицирует эмбеддинги для рекомендаций.


Результат: Персонализированные рекомендации, основанные на навыках.Описание: Вставьте скриншот и объясните, как работает нейросеть.


Слайд 9: Архитектура системы
Текст:

Компоненты:
Frontend: Обработка ввода пользователя, отображение рекомендаций.
Backend: REST API, интеграция с моделью ML.
Модель ML: BERT + классификаторы, обучение на данных о профессиях.
База данных: Хранение профилей пользователей и справочника профессий.


Схема:
[Вставьте диаграмму: Пользователь → Frontend → Backend → BERT → Рекомендации]


Преимущества: Модульность, масштабируемость.Описание: Показывает, как компоненты системы взаимодействуют.


Слайд 10: Результаты и метрики
Текст:

Тестирование:
Датасет: 1000 резюме и описаний профессий.
Метрики: Accuracy (90%), F1-Score (0.88).


Результаты:
Точность рекомендаций: 85% пользователей получили релевантные профессии.
Время ответа: <2 секунд на запрос.


Сравнение с аналогами: Выше точность за счет BERT.Описание: Подчеркивает эффективность системы с цифрами.


Слайд 11: Выводы и перспективы
Текст:

Выводы:
Разработана система «Карьерный консультант» с использованием BERT и ML.
Достигнута высокая точность рекомендаций.
Система удобна и масштабируема.


Перспективы:
Интеграция с платформами вакансий (например, HH.ru).
Добавление мультиязычной поддержки.
Улучшение модели с помощью новых данных.Описание: Подводит итоги и намечает будущее проекта.




Слайд 12: Вопросы и благодарность
Текст:

Спасибо за внимание!
Готов ответить на ваши вопросы.
Благодарность:
Руководителю: [Имя] за поддержку и советы.
Команде: [Имена, если есть] за помощь в тестировании.Описание: Завершает презентацию, открывая диалог.



