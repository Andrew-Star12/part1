from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
# Create your views here.
from django.views import generic

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,
                 'num_authors':num_authors,
                 'num_visits':num_visits,}
    )

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'  # Убедитесь, что шаблон существует
    context_object_name = 'book_list'  # Используемое имя для списка книг в шаблоне

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'  # Убедитесь, что шаблон существует
    context_object_name = 'book'  # Имя переменной, которая будет передана в шаблон

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'  # Шаблон для отображения списка авторов
    context_object_name = 'author_list'  # Имя переменной, которая будет использоваться в шаблоне

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'  # Шаблон для отображения информации об авторе
    context_object_name = 'author'  # Имя переменной, которая будет использоваться в шаблоне
