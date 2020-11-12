# odoo_test

Здравствуйте!

Задание выполнил на 10й версии. Раньше её не пробовал, но теперь знаю что 10я у вас рабочая. 

Тестировал вручную.
Сложности возникали в связи с тем, что книга Даниэля Рейса по 10й версии пару раз заводила в тупик. Там буквально ошибки касательно применения orm/api.
Небольшие ошибки, но когда опыта около 0, такие ошибки в книге призванной провести по процессу работы с odoo "за руку" становятся критическими.
Больше пользы было от руководства ORM, и с форумов(odoo, stackoverflow).

Сначала выполнил задание на собственной, новой модели данных. С собственной простенькой формой представления.
Просто не знал что имеется базовая модель partner.

При тестировании обнаружил что в базовом классе models.Model create() является абсолютно отдельной функцией от write().
По моему не логично. Она же вносит значения полей в базу. Я бы на месте авторов в create создавал пустые поля, а затем использовал write для записи в них.
В итоге пришлось переопределять и create и write, что-бы задание выполнялось не только при создании объекта но и при изменении.

Перевел созданный addon на русский через программу poedit, проверил язык в интерфейсе.

Понял что в задании требуется именно наследовать модель данных от res.partner.
Наследовал под собственным именем.
На этом этапе возникли сложности с ручным тестированием. Унаследовалось много всего, причем многие поля обязательные. 
Пришлось наследовать и форму представления, взамен своей,
что-бы хоть посмотреть что там необходимо заполнять, помимо новых полей ИНН и КПП.
Заполнять там оказалось много. 
Да еще и с добавками от установленных стандартных модулей, которые res.partner наследуют с добавлением в исходник.
Но в общем справился и с этим.
 
