# Сервис Yacut

###*Автор - Кирилл Резник*

## Описание

**Yacut** - это сервис укорачивания ссылок, который ассоциирует 
длинную ссылку с короткой. Короткую ссылку можно "привязать" к
длинной двумя путями - либо придумать и ввести ее самому, либо
сгенерировать автоматически при помощи сервиса.

Короткая ссылка позволяет переходить по исходному адресу.

Данный проект также поддерживает взаимодействие по API

(полная спецификация API доступна в репозитории - файл openapi.yml)


## В проекте использовались следующие технологии:
- [Python](https://www.python.org/);
- [Flask](https://pypi.org/project/Flask/);
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/);

## Установка проекта
1. Склонируйте репозиторий:
```
git clone git@github.com:Invictus-7/yacut.git
```
2. Активируйте venv и установите зависимости:
```
python -m venv venv
venv/scripts/activate
pip install -r requirements.txt
```
3. Создайте в корневой директории файл .env со следующим константами:
```
FLASK_APP=yacut
FLASK_ENV=development или production
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=<ваш_секретный_ключ>
```
4. Теперь проект можно запускать.

## Управление проектом:
Для локального запуска выполните команду:
```
flask run
```
Сервис будет запущен и доступен по следующим адресам:
- http://localhost/ - главная страница сервиса;

    * Если не заполнить поле для короткой ссылки, она будет сгенерирована автоматически.
    * Короткая ссылка должна быть не длиннее 16 символов (цифры и латинские буквы в любом регистре).

##Работа с API

- http://localhost/api/id/ - эндпоинт для POST-запросов;

    * Схема POST-запроса:
        ```json
        {
        "url": "string",
        "custom_id": "string"
        }
        ```
      (string - необязательное поле)
    
    * Схема ответа на POST-запрос:
        ```json
        {
        "url": "string",
        "short_link": "string"
        }
        ```

- http://localhost/api/id/short_id/ - эндпоинт для GET-запросов.
    
    В данном эндпоинте вместо <short_id>  нужно прописать полученную ранее короткую ссылку.

    * Схема ответа на GET-запрос:
        ```json
        {
        "url": "string"
        }
        ```

    
