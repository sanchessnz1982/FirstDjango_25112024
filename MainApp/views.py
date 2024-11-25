from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
# NAME = 'Ващенко Александр Сергеевич'

author = dict(FirstName='Александр', MiddleName='Сергеевич', LastName='Ващенко', Telephone='+79227026677',
              Email='sanchessnz@mail.ru')


def get_fullname() -> str:
    return f'{author["LastName"]} {author["FirstName"]} {author["MiddleName"]}'


def home(request: HttpRequest) -> HttpResponse:
    full_name = get_fullname()
    text = f"""
        <h1>"Изучаем django"</h1>
        <strong>Автор</strong>: <i>{full_name}</i>
        """
    return HttpResponse(text)


def about(request: HttpRequest) -> HttpResponse:
    text = f"""
          <br>
          Имя:<b>{author["FirstName"]}</b><br>
          Отчество:<b>{author['MiddleName']}</b><br>
          Фамилия:<b>{author["LastName"]}</b><br>
          Телефон:<b>{author["Telephone"]}</b><br>
          электронный адрес:<b>{author["Email"]}</b><br>
          </br> 
    """
    return HttpResponse(text)


items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def get_item(request: HttpRequest, id: int) -> HttpResponse:
    for item in items:
        if item['id'] == id:
            text = f'наименование:{item["name"]}, количество: {item["quantity"]}'
            break
        else:
            text = f'товар с id = {id} не найден!'
    return HttpResponse(text)


def get_items(request: HttpRequest) -> HttpResponse:
    text = ''
    for item in items:
        # s =s + f'<li> {item['name']} : {item['quantity']} </li>'
        # s = s + '<a href = ./item/'+ str(item['id']) +'><li>наименование: ' + item['name'] + ', количество: ' + str(item['quantity']) + '</li></a>'
        # href_text = f"<a href = ./item/{str(item['id'])}></a>"
        text = text + f"<a href = /item/{str(item['id'])}><li>наименование:{item['name']}, количество: {item['quantity']}</li></a>"
        # href_text = href_text + f"<a href = ./item/{str(item['id'])}>{text}</a>"
    return HttpResponse(f"<ol>{text}</ol>")
