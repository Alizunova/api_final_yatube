# **Финальный проект спринта: API для Yatube** 
***Здесь можно размещать свой контент.
Авторам — публиковать посты. 
Пользователям -подписываться на любимого автора и оставлять комментарии.***   
## Технологии
Python 3.9
Django 3.2
Django REST framework 3.12
## **Как запустить проект:**
+ Клонировать репозиторий и перейти в него в командной строке:
  - git clone
  - cd api_yatube
+ Cоздать и активировать виртуальное окружение:
  - python -m venv env
  - source env/bin/activate
+ Установить зависимости из файла requirements.txt:
  - python -m pip install --upgrade pip
  - pip install -r requirements.txt
+ Выполнить миграции:
  - python manage.py migrate
+ Запустить проект:
  - python manage.py runserver
## Примеры запросов к API:
+ Неавторизированный пользователь

<ins>Получить список всех публикаций.</ins>
GET /api/v1/posts/
<ins>При указании параметров limit и offset выдача производится постранично.</ins>
GET /api/v1/posts/?limit=5&offset=3
<ins>Получить публикацию по id.</ins>
GET api/v1/posts/{id}/
<ins>Получить все комментарии к публикации post_id.</ins>
GET api/v1/posts/{post_id}/comments/
<ins>Получить список групп.</ins>
GET api/v1/groups/
+ Авторизированный пользователь

<ins>Добавление публикации.</ins>
POST /api/v1/posts/
<ins>Обновление публикации по id.</ins>
POST /api/v1/posts/{id}/
<ins>Удаление публикации по id.</ins>
DELETE /api/v1/posts/{id}/
<ins>Подписка на пользователя переданного в теле запроса.</ins>
POST /api/v1/follow/
<ins>Получить список всех подписок на других пользователей.</ins>
     GET api/v1/follow/
## Автор
Лизунова Анна
