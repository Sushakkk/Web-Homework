from django.http import HttpResponse
from django.urls import reverse

def index(request):
    # Получение URL для списка всех багов и запросов на улучшение с помощью функции reverse
    bugs_url = reverse('quality_control:bugs')
    features_url = reverse('quality_control:features')

    # Создание строки HTML с заголовком и ссылками, используя полученные URL
    html = f"<h1>Система контроля качества</h1>" \
           f"<a href='{bugs_url}'>Список всех багов</a><br>" \
           f"<a href='{features_url}'>Запросы на улучшение</a>"

    # Возврат HTML-строки в виде HTTP-ответа
    return HttpResponse(html)

def bug_list(request):
    return HttpResponse("<h2>Список отчетов об ошибках</h2>")

def feature_list(request):
    return HttpResponse("<h2>Список запросов на улучшение</h2>")

def bug_detail(request, bug_id):
    # Формирование строки с деталями бага, используя переданный bug_id
    html = f"Детали бага {bug_id}"
    return HttpResponse(html)

def feature_detail(request, feature_id):
    # Формирование строки с деталями улучшения, используя переданный feature_id
    html = f"Детали улучшения {feature_id}"
    return HttpResponse(html)
