// Якщо документ готовий (завантажився)
$(document).ready(function(){
    // Отримуємо усі кнокпи та застосвувємо функцію для кожної з них
    $('.manage-favorites-button').each(function(){
        // Звертаємося до поточної кнопки та задаємо подію натискання
        $(this).on('click', function(){
            // Створюємо AJAX-запит, щоб зробити запит на севрер без перезавантаження сторінки
            $.ajax({
                // url, на який треба зробити запит (беремо з атрибута value натиснутої кнопки)
                url: $(this).val(),
                // Тип запиту
                type: 'get',
                // Якщо запит надіслано та від сервера прийде відповідь про успіх 
                success: function(data, state, result){
                    // Отримуємо кількість улюблених фільмів з відповіді сервера
                    let amountFavouriteFilms = result.getResponseHeader("film_amount");
                    // Перезаписуємо кількість улюблених фільмів у HTML
                    $("#favorite-film-num").html(amountFavouriteFilms);
                }
            });
        });
    });
});