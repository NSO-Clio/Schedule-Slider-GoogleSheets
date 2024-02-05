# Schedule-Slider-GoogleSheets

Веб заставка ввиде слайдера расписания

# Заказчик

Данная заставка была разработанна по заказу МАОУ Лицей №22 "Надежда Сибири" в Новосибирской области, город Новосибирск 2024 год.

<img style="width: 70%; height: 70%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/logo22.jpg">

# Подключение аккаунта и всей таблицы

- Вам понадобиться ключ разработчика google для вашей таблици с расписанием

- Ключ разработчика(json файл), который вы сохраните нужно переименовать как «TimeTable_serviceAcc»

- После чего в коде файла api.py где указан url в кавычки вставить свой, а именно ссылка на вашу таблицу

- После чего в переменных id_gid_one_sm и id_gid_two_sm укать id таблиц, которые сделаны для расписания классов. Id страници указан в ссылке после слова «gid» в данном примере id 0
<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo1701598302.jpeg">

```python
tw = TableWorker(
    url='YOUR_URL',
    id_gid_one_sm=[YOUR_ID],
    id_gid_two_sm=[YOUR_ID],
    id_gid_consult=[YOUR_ID],
    path_service_account='TimeTable_serviceAcc.json'
)
```

# Запуск приложения

После того как вы сделаете все пункты выше вам придётся скачать все библиотеки, которые используются в API, и запустить файл api.py. Через консоль, открыв её внутри рабочей папки и прописать

- Скачиваем библиотеки
```
pip install -r requirements.txt
```

- Запускаем API
```
python api.py
```

Потом в браузере перейти в по ссылке http://localhost:5000/ и включить полноэкранный режим.

Приложение запущено можно пользоваться

- пролистование происходит по таймеру в файле ``` templates/time_table_for_class.html ``` , по умолчанию стоит 27 секунд,
строки 239 - 254
```html
<script>
    $(document).ready(function () {
        $(".slider").slick({
            slidesToShow: 1,
            slidesToScroll: 2,
            infinite: true,
            centerMode: true,
            centerPadding: "50px",
            autoplay: true,
            autoplaySpeed: YOUR_TIME,
        });
        $(".slick-prev").text("");
        $(".slick-next").text("");
    });

</script>
```

- ежедневное происходит в файле ``` templates/time_table_for_class.html ``` , по умолчанию оно происходит в 00:03 🕥 ,
строки 256 - 274
```html
<script>
    function refreshAt(hours, minutes, seconds) {
    var now = new Date();
    var then = new Date();

    if(now.getHours() > hours ||
       (now.getHours() == hours && now.getMinutes() > minutes) ||
        now.getHours() == hours && now.getMinutes() == minutes && now.getSeconds() >= seconds) {
        then.setDate(now.getDate() + 1);
    }
    then.setHours(hours);
    then.setMinutes(minutes);
    then.setSeconds(seconds);

    var timeout = (then.getTime() - now.getTime());
    setTimeout(function() { window.location.reload(true); }, timeout);
}
refreshAt(YOUR_HOUR,YOUR_MINUT,0);
</script>
```

# Наши контакты

**Андреасян Егор Андреасович**:

> **BackEnd and FullStack Dev**

- Почта: egorandreasyan@yandex.ru
- Дополнительная почта: egorandreas28@gmail.com
- Телегремм: https://t.me/EgorAndrik
- Vk: https://vk.com/egor_andrik
- Github: https://github.com/EgorAndrik 

**Пясковский Александр Михайлович**:

> **FrontEnd and FullStack Dev**

- Почта: alexanderpyaskovsky@yandex.ru 
- Дополнительная почта: sashakedr@icloud.com 
- Телегремм: https://t.me/SAMURAI_KOVSKI
- Vk: https://vk.com/id457951126 
- Github: https://github.com/SAMURAI2035 
