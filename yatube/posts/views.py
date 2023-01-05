# posts/views.py
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком постов
def posts_list(request):
    return HttpResponse('Список постов')


# Страница с информацией об группах постов;
# view-функция принимает параметр pk из path()
def group_posts(request, slug):
    return HttpResponse(f'группы постов {slug}')