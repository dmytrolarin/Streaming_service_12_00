$(document).ready(function(){
    // Подія відправки форми
    $('#reviewForm').submit(function(event){
        // Запобігаємо стандартній поведінці форми, щоб форма не відправлялась (і сторінка не перезавантажувалась)
        event.preventDefault();
        // Формуємо AJAX запит для відправки форми        
        $.ajax({
            type: 'post',// Тип запиту на сервер
            data: $(this).serialize(),// Пердаємо дані полів форми у форматі пар ключ=значення
            success: function(response){
                console.log('Форма успішно надіслана');
            }
        })
    });
});