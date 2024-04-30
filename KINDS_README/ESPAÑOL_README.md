# Schedule-Slider-GoogleSheets

Slider de horario como una pantalla web

# Otros idiomas

- [Inglés](../KINDS_README/ENGLISH_README.md)
- [Español](../KINDS_README/ESPAÑOL_README.md)
- [Ruso](../README.md)

# Cliente

Esta pantalla fue desarrollada por encargo de la Escuela Secundaria №22 "Nadezhda Sibiri" en la región de Novosibirsk, ciudad de Novosibirsk en el año 2024.

<img style="width: 70%; height: 70%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/logo22.jpg">

# Conexión de la cuenta y la hoja completa

- Necesitará una clave de desarrollador de Google para su hoja de horarios.

- La clave de desarrollador (archivo json) que guarde debe ser renombrada como "TimeTable_serviceAcc".

- Luego, en el código del archivo api.py donde se especifica la URL entre comillas, inserte la suya, es decir, el enlace a su hoja.

- Luego, en las variables id_gid_one_sm e id_gid_two_sm, especifique los ID de las hojas que se crearon para los horarios de clases. El ID de la página se indica en el enlace después de la palabra "gid" en este ejemplo, el ID es 0.
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

# Ejecutar la aplicación

Después de completar los pasos anteriores, deberá descargar todas las bibliotecas utilizadas en la API y ejecutar el archivo api.py. A través de la consola, abriéndola dentro de la carpeta de trabajo y escribiendo

- Descargar bibliotecas
```
pip install -r requirements.txt
```

- Ejecutar la API
```
python api.py
```

Luego, vaya al navegador y acceda al enlace http://localhost:5000/ y active el modo de pantalla completa.

La aplicación está en funcionamiento y lista para ser utilizada.

- El desplazamiento se realiza mediante un temporizador en el archivo ``` templates/time_table_for_class.html ```, de forma predeterminada está configurado en 9 segundos,
líneas 239 - 254
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

- La actualización diaria se realiza en el archivo ``` templates/time_table_for_class.html ```, de forma predeterminada ocurre a las 00:03 🕥,
líneas 256 - 274
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

# Notas adicionales sobre la administración

- El horario de clases debe tener un estilo uniforme para la primera, segunda sesión y horarios de consulta.

Ejemplo:

- Primera sesión

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-25.jpg">

- Segunda sesión

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-24.jpg">

- Consultas

<img style="width: 80%; height: 80%;" src="https://github.com/NSO-OSKOM/Web-application-for-school-schedule/blob/main/forREADME/photo_2023-12-19_23-38-21.jpg">

Se puede ver un ejemplo de hoja de cálculo de Google en el siguiente enlace https://docs.google.com/spreadsheets/d/1ef__SA0CMETxDydDADxHaUU10-NLQmL6T16MOYVUznI/edit#gid=0

# Nuestros contactos

**Egor Andreasyan**:

> **Desarrollador BackEnd y FullStack**

- Correo electrónico: egorandreasyan@yandex.ru
- Correo electrónico adicional: egorandreas28@gmail.com
- Telegram: https://t.me/EgorAndrik
- Vk: https://vk.com/egor_andrik
- Github: https://github.com/EgorAndrik

**Alexander Pyaskovsky**:

> **Desarrollador FrontEnd y FullStack**

- Correo electrónico: alexanderpyaskovsky@yandex.ru
- Correo electrónico adicional: sashakedr@icloud.com
- Telegram: https://t.me/SAMURAI_KOVSKI
- Vk: https://vk.com/id457951126
- Github: https://github.com/SAMURAI2035
