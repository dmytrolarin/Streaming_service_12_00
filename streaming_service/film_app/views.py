from django.shortcuts import render, redirect
from .models import Film
from django.http import HttpRequest, HttpResponse
from .forms import ReviewForm


def render_all_films(request: HttpRequest):
    films = Film.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('all_films')
    else:
        form = ReviewForm()
    return render(request,"film_app/film.html", context={"films": films, 'form': form})

# Функція 'add_to_favorite' відповідає за додавання будь якого фільма в Улюблені в Улюблені
def add_to_favorite(request: HttpRequest, film_id: int):
    # Створили об'єкт відповіді
    response = HttpResponse()
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
        # Отримуємо кількість улюблених фільмів на основі довжини списку
        film_amount = len(set_cookies)

    # Якщо cookie-файли з запису не було отримано то
    else:
        # Встановлюємо cookie з назвою favorites із значенням film_id та вказуємо час життя 3600 секунд (1година)
        response.set_cookie("favorites", film_id, max_age=3600)  
        # Задаємо початкову кількість улюблених фільмів 
        film_amount = 1
    # У відповідь клієнту зберігаємо к-ть улюблених фільмів
    response["film_amount"] = film_amount
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

# Функція, що відповідає за видалення фільму з "улюблених" за id
def delete_from_favorite(request: HttpRequest, film_id: int):
    # Отримуємо рядок з COOKIES, що зберігає id улюблених фільмів
    films_id = request.COOKIES.get("favorites")
    # Розбиваємо рядок по пробілам, утіорюючи список
    films_list = films_id.split(" ")
    # Видаляємо зі списку відповідний id
    films_list.remove(str(film_id))
    # Конвертуємо список у рядок, розділяючи кожний id по пробілам
    films_id_updated = " ".join(films_list)
    # Формує об'єкт відповіді сервера
    response = HttpResponse()
    # Зберігаємо оновлені кукі
    response.set_cookie("favorites", films_id_updated, max_age=3600)
    # Отримуємо кількість улюблених фільмів на основі довжини списку
    film_amount = len(films_list)
    # У відповідь клієнту зберігаємо к-ть улюблених фільмів
    response["film_amount"] = film_amount
    # Повератємо об'єкт відопвіді
    return response



    