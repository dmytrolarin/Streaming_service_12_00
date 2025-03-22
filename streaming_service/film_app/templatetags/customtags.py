from django import template
from film_app.models import Film

# Створюємо об'єкт класу Library, що відповідає за реєстрацію тегів
register = template.Library()

# Реєструємо простий тег (тег, що просто повертає значення у шаблоні)
@register.simple_tag
def number_of_favorites(request):
    ''' 
    Функція, що відповідає за логіку тегу {% number_of_favorites %} у шаблонах.
    Функція повертає кількість улюблених фільмів.
    '''
    # Отримуємо Cookie по ключу 'favorites'
    favorites_from_cookie = request.COOKIES.get('favorites')
    # Перевіряємо, чи існують такі кукі
    if favorites_from_cookie:
        # Розділяємо pk улюблених фільмів, перетворючи рядок на список 
        list_cookies = favorites_from_cookie.split(' ')
        # Отримуємо довжину списку (кількість улюблених фільмів)
        number_of_favorites = len(list_cookies)
    else:
        # Інакше кіькість улюблених фільмів - 0
        number_of_favorites = 0
    # Значення, яке повртає тег
    return number_of_favorites

# Реєструємо inclusion-тег, який генерує частину html-коду
@register.inclusion_tag(filename = 'film_app/inclusion_tags/best_film.html')
# Створюємо функцію яка відповідає за логіку тегу {% best_film %}
def best_film():
    # Створюємо об'єкт, у який отримаємо фільм з pk 1
    film = Film.objects.get(pk = 1)
    # Повертаємо контекст для роботи у файлі best_film.html
    return {'film': film}

# Реєструємо inclusion-тег, який генерує частину html-коду. 
# Параметр takes_context довзволяє тегу отримати context з функції-відображення у агрумент "context"
@register.inclusion_tag(filename = 'film_app/inclusion_tags/list_films.html', takes_context= True)
# Створюємо функцію тегу 'list_films', яка приймає аргумент context та add_or_delete
def list_films(context, add_or_delete):
    # Словник, який будемо передавати у  list_films.html
    films_context = {'films': context["films"]}
    # Робимо перевірку, якщо треба відображати під фільмами кнопку "додати до улюбленного"
    if add_or_delete == "add":
        # Вказуємо відповідні параемтри для кнопки
        films_context["button_url"] = "add_to_favorite"
        films_context["button_text"] = "Додати до улюбленого"
        films_context["button_class"] = "add-to-favorite"
    else:
        # Вказуємо відповідні параемтри для кнопки, якщо треба відображати під фільмами кнопку "видалити зщ улюбленного"
        films_context["button_url"] = "add_to_favorite"
        films_context["button_text"] = "Видалити з улюбленого"
        films_context["button_class"] = "delete-from-favorite"
    # Передаємо параметри у list_films.html
    return films_context

