# test_microblog
Тестовое задание по разработке анонимного микроблога

**Установка:**

* Выполните: `pip install -r requirements.txt`, чтобы установить необходимые зависимости в вашем окружении.

* Измените настройки подключения базы данных в файле settings.py в соответствии с вашими значениями:
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'test_microblog',
            'USER' : 'microblog_user',
            'PASSWORD' : 'password',
            'HOST' : '127.0.0.1',
            'PORT' : '5432',
        }
    }
    ```

* Выполните: `python manage.py migrate`, чтобы применить миграции.
