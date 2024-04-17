from django.http import HttpResponse  # Импорт класса HttpResponse из модуля django.http для возврата HTTP-ответов
from django.urls import reverse  # Импорт функции reverse из модуля django.urls для динамического получения URL

def index(request):
    # Получение URL для маршрута 'tasks:another_page' с помощью функции reverse
    another_page_url = reverse('tasks:another_page')
    quality_control_url = quality_control_url = reverse('quality_control:index')


    # Создание строки HTML, содержащей заголовок и ссылку на другую страницу
    html = f"<h1>Страница приложения tasks</h1>"\
      f"<a href='{another_page_url}'>Перейти на другую страницу</a><br>" \
      f"<a href='{quality_control_url}'>Система контроля качества</a>" \

    # Возврат HTML-строки в виде HTTP-ответа
    return HttpResponse(html)

def another_page(request):
    # Возврат текста в виде HTTP-ответа при обращении к другой странице
    return HttpResponse("Это другая страница приложения tasks.")
