# Schedule-Slider-GoogleSheets

Web screensaver in the form of a schedule slider

# Other Languages

- [English](../KINDS_README/ENGLISH_README.md)
- [Español](../KINDS_README/ESPAÑOL_README.md)
- [Русский](../README.md)

# Customer

This screensaver was developed to order by the Municipal Autonomous Educational Institution Lyceum No. 22 "Nadezhda Sibiri" in the Novosibirsk region, city of Novosibirsk 2024.

<img style="width: 70%; height: 70%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/logo22.jpg">

# Connecting an account and the entire table

- You will need a Google developer key for your schedule table

- The developer key (json file) that you save needs to be renamed as "TimeTable_serviceAcc"

- After that, in the code of the api.py file where the url is specified in quotes, insert your own, namely the link to your table

- After that, in the variables id_gid_one_sm and id_gid_two_sm, specify the ids of the tables made for class schedules. The page id is specified in the link after the word "gid" in this example id 0
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

# Running the application

After you complete all the above steps, you will need to download all the libraries used in the API and run the api.py file. Through the console, opening it inside the working folder and typing

- Download libraries
```
pip install -r requirements.txt
```

- Launch the API
```
python api.py
```

Then in the browser go to the link http://localhost:5000/ and switch to full screen mode.

The application is running and can be used

- scrolling happens on a timer in the file `templates/time_table_for_class.html`, by default it is set to 9 seconds,
lines 239 - 254
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

- daily refresh happens in the file `templates/time_table_for_class.html`, by default it happens at 00:03 🕥,
lines 256 - 274
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

# Additional notes on administration

- The schedule for classes should be of the same style for the first, second shifts, and consultation schedules

Example:

- First shift

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-25.jpg">

- Second shift

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-24.jpg">

- Consultations

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-21.jpg">

You can view an example Google spreadsheet at the following link: https://docs.google.com/spreadsheets/d/1ef__SA0CMETxDydDADxHaUU10-NLQmL6T16MOYVUznI/edit#gid=0

# Our contacts

**Andreyasyan Egor Andreyasovich**:

> **BackEnd and FullStack Dev**

- Email: egorandreasyan@yandex.ru
- Additional email: egorandreas28@gmail.com
- Telegram: https://t.me/EgorAndrik
- Vk: https://vk.com/egor_andrik
- Github: https://github.com/EgorAndrik

**Pyaskovsky Alexander Mikhailovich**:

> **FrontEnd and FullStack Dev**

- Email: alexanderpyaskovsky@yandex.ru
- Additional email: sashakedr@icloud.com
- Telegram: https://t.me/SAMURAI_KOVSKI
- Vk: https://vk.com/id457951126
- Github: https://github.com/SAMURAI2035
