# DataCenter Management System

Это руководство содержит инструкции по запуску и использованию проекта DataCenter Management System.

## Установка

Python3 должен быть уже установлен.
Для корректной работы скрипта, необходимо использовать все зависимости из файла `requirements.txt`
Запуск лучше производить используя виртуальное окружение `venv`.
1. Склонируйте репозиторий:

```bash
git clone https://github.com/GoNt1eRRR/django-orm-watching-storage.git
```

2. Для создания `venv` и использования скрипта выполните следующие шаги:

Создать виртуальное окружение
```
python -m venv <name venv>
```

Активировать
```
<name venv>\Scripts\activate
```

3. Установить все зависимости из `requirements.txt`
```
pip install -r requirements.txt
```

## Настройка

Создайте файл `.env` в корне проекта и заполните его данными о настройке проекта, например:

```
DATABASE_URL=postgres://USERNAME:PASSWORD@HOST:PORT/DATABASE_NAME
SECRET_KEY=REPLACE_ME
DEBUG=True
ALLOWED_HOSTS=[*]
```

## Запуск

Запустите сервер

```bash
python manage.py runserver
```

Теперь проект доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)
