from django.shortcuts import render, redirect
from .models import Film
from django.http import HttpRequest


def render_all_films(request: HttpRequest):
    films = Film.objects.all()
    
    return render(request,"film_app/film.html", context={"films": films})

# Функція 'add_to_favorite' відповідає за додавання будь якого фільма в Улюблені в Улюблені
def add_to_favorite(request: HttpRequest, film_id: int):
    # Створили об'єкт відповіді, яка перенаправляє користувача на сторінку 'all_films'
    response = redirect("all_films")
    # Отримуємо значення cookie з ключем 'favorites'
    favorites_from_cookie = request.COOKIES.get("favorites")
    # Якщо були отримані cookie-файли з запиту:
    if favorites_from_cookie:
        # Поділимо наші cookie за пробілом та створимо список з id улюблених фільмів
        list_cookies = favorites_from_cookie.split(" ")
        # Додаємо в список id фільму,який треба додати в улюблені, та конвертуємо id у формат рядку
        list_cookies.append(str(film_id))
        # Видаляємо однакові id, за рахунок конвертування списку у тип даних set
        set_cookies = set(list_cookies)
        # Перетворюємо наш list в рядок для збереження в cookie
        string_cookies = " ".join(set_cookies)
        # Зберігаємо наші cookie файли за ключем favorites, встановлючи час життя 1 годину
        response.set_cookie("favorites", string_cookies, max_age=3600)
    # Якщо cookie-файли з запису не було отримано то
    else:
        # Встановлюємо cookie з назвою favorites із значенням film_id та вказуємо час життя 3600 секунд (1година)
        response.set_cookie("favorites", film_id, max_age=3600)
    # Повертаємо об'єкт response
    return response

# Функція, що відповідає за відображення сторінки з улюбленими фільмами
def render_favorite_films(request: HttpRequest):
    # Отримаємо кукі з id улюблених фільмів по ключу favorites
    films_ids = request.COOKIES.get("favorites")
    # Створюємо пустий context
    context = {
        "films": []
    }
    # Перевіряємо, чи існують куки
    if films_ids:
        # Ділимо films_ids по пробілам та перетворюємо films_id на список
        films_ids = films_ids.split(" ")
        # Фільтруємо фільми, в  id яких знаходиться у films_ids
        films = Film.objects.filter(id__in = films_ids)
        # Записуємо під ключем films відфільтровані фільми
        context["films"] = films
    # Формуємо відповідь
    return render(request, 'film_app/favorite_films.html', context= context)