# Book Shop API
Проект "book_shop" представляет собой API для интернет-магазина книг. С помощью этого API пользователи могут просматривать, добавлять, редактировать и удалять книги, а также управлять своими учетными записями.

## Установка и настройка

Для запуска проекта необходимо выполнить следующие шаги:
 
1. Склонировать репозиторий:
`git clone https://github.com/AzathothDK/book_shop.git`

2. Установить зависимости:
`pip install -r requirements.txt`

3. Настроить подключение к базе данных в файле "database.py"

4. Запустить командой
`python main.py`
## Структура проекта
Проект состоит из следующих файлов:

**app/crud/book.py**: модуль для работы с базой данных для книг.

**app/crud/user.py**: модуль для работы с базой данных для пользователей.

**app/routers/book.py**: модуль для маршрутизации запросов, связанных с книгами.

**app/routers/user.py**: модуль для маршрутизации запросов, связанных с пользователями.

**app/schemas/book.py**: модуль для определения схемы данных для книг.

**app/schemas/user.py**: модуль для определения схемы данных для пользователей.

**app/main.py**: основной файл приложения, который объединяет все модули и настраивает подключение к базе данных.

**app/database.py**: модуль для создания подключения к базе данных.

**app/models.py**: модуль для определения моделей данных для книг и пользователей.
## Использование API

API имеет следующие маршруты:

- **GET /books**: получение списка всех книг в базе данных.
- **GET /books/{id}**: получение информации о книге с указанным идентификатором.
- **POST /books**: добавление новой книги в базу данных.
- **PUT /books/{id}**: обновление информации о книге с указанным идентификатором.
- **DELETE /books/{id}**: удаление книги с указанным идентификатором из базы данных.
- **POST /users**: создание нового пользователя в базе данных.
- **GET /users/{id}**: получение информации о пользователе с указанным идентификатором.
- **PUT /users/{id}**: обновление информации о пользователе с указанным идентификатором.
- **DELETE /users/{id}**: удаление пользователя с указанным идентификатором из базы данных.
- **POST /token**: получение токена доступа для авторизации пользователя.
Для доступа к данным и выполнения запросов необходимо авторизоваться с помощью токена доступа, который можно получить, отправив запрос POST на маршрут "/token" с параметрами "username" и "password". Полученный токен нужно использовать в заголовке "Authorization" для выполнения запросов к остальным маршрутам.

## Примеры запросов
### Получение списка всех книг
```
GET /books HTTP/1.1
Host: example.com
Authorization: Bearer <access_token>
```
### Получение информации о книге
```
GET /books/1 HTTP/1.1
Host: example.com
Authorization: Bearer <access_token>
```
### Добавление новой книги
```
POST /books HTTP/1.1
Host: example.com
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "title": "New Book",
    "author": "John Doe",
    "description": "A new book.",
    "price": 9.99
}
```
### Обновление информации о книге
```
PUT /books/1 HTTP/1.1
Host: example.com
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "title": "Updated Book",
    "author": "Jane Doe",
    "description": "An updated book.",
    "price": 12.99
}
```
### Удаление книги
```
DELETE /books/1 HTTP/1.1
Host: example.com
Authorization: Bearer <access_token>
```
## Список желаний:
1. Добавление функционала поиска книг по автору, названию, описанию и тегам.
2. Возможность добавления тегов к книгам и поиска книг по тегам.
3. Реализация функции рекомендации книг на основе истории просмотров и покупок пользователя.
4. Добавление системы оценок книг, возможность просмотра рейтинга книг.
5. Реализация корзины для добавления книг перед покупкой.
6. Интеграция с сервисом оплаты для возможности проведения платежей за книги.
7. Возможность добавления отзывов и комментариев к книгам.
8. Реализация функционала подписки на новые книги и скидки.
9. Добавление функции сохранения книг в избранное.
10. Реализация мультиязычности приложения для привлечения максимального числа пользователей.

### Авторы
AzathothDK (https://github.com/AzathothDK)
