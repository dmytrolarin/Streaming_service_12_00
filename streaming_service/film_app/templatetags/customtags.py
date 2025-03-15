from django import template

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