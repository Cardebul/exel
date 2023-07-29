### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Cardebul/exel.git
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
cd kp
```


Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Создать миграции:

```
python3 manage.py makemigrations
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
