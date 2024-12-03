# Django Telegram Authentification

## Описание:
Web приложение на Django с аутентификацией через Telegram.
На данный ммент приложение доступно на https://djangotelegramauth.zapto.org/welcome/

## Для разработчиков:

### Пример файла с переменными среды:
".env.example" в корневой папке проекта:

### Линтер:
`black`

### Pre-commit:
Настроен pre-commit для проверки оформления кода.
Для проверки кода перед выполнением операции commit, выполнить команду:

```
pre-commit run --all-files
```

## Как запустить проект:

1) Клонировать проект.
```
git clone https://github.com:PentiukPavel/Django_Telegram_Auth.git
```

2) Создать Телеграм бот. Инструкция по созданию - https://core.telegram.org/bots#3-how-do-i-create-a-bot. Обязаьельно привяжите к боту доменное имя Вашего сайта.

3) Переименовать файл .env.example и изменить содержимое на актуальные данные.
```
mv .env.example .env
```

4) Создать виртуальное окружение:
```
py -3 -m venv venv
```

5) Активировать виртуальное окружение:
```
source venv/Scripts/activate
```

6) Установить зависимости из файла requirements_dev.txt:
```
pip install -r requirements_dev.txt
```

7) В папке с файлом manage.py (./src) выполнить следующие команды для миграций:
```
python manage.py migrate
```

8) Запустить проект:
```
python manage.py runserver
```

## Системные требования:
### Python==3.12

## Стек
### Django
