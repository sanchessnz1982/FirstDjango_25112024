#FirstDjango_25112024

## инструкция по развертыванию

1. python -m venv .env
2. source .env/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

## запуск ipython 
    pip install shell-plus,
    pip freeze > requer...txt
    pip install ipython
    
    python manage.py shell_plus --ipython

## выгрузить данные из бд
python manage.py dumpdata MainApp --indent 4 > ./fixtures/items.json
python manage.py dumpdata MainApp --indent 4 -o ./fixtures/items.json (win)

## загрузка данных в бд

python manage.py loaddata ./fixtures/items.json


## day 2 

1. PyCharm -> File -> Settings -> Language and Frameworks ->
    Template Language: Django