from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
#NAME = 'Ващенко Александр Сергеевич'

author = dict(FirstName='Александр', MiddleName='Сергеевич', LastName='Ващенко', Telephone='+79227026677',
              Email='sanchessnz@mail.ru')

def get_fullname()->str:
    return f'{author["LastName"]} {author["FirstName"]} {author["MiddleName"]}'


def home(request:HttpRequest)->HttpResponse:
    full_name = get_fullname()
    text = f"""
        <h1>"Изучаем django"</h1>
        <strong>Автор</strong>: <i>{full_name}</i>
        """
    return HttpResponse(text)

def about(request:HttpRequest)->HttpResponse:
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
