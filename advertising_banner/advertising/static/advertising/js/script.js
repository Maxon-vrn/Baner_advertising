ymaps.ready(init);
    function init(){
        // Создание карты.
        var myMap = new ymaps.Map("map", {
            // Координаты центра карты.
            // Порядок по умолчанию: «широта, долгота».
            // Чтобы не определять координаты центра карты вручную,
            // воспользуйтесь инструментом Определение координат.
            center: [51.660703, 39.199516], //площадь Ленина
            // Уровень масштабирования. Допустимые значения:
            // от 0 (весь мир) до 19.
            zoom: 12
            },{
            searchControlProvider: 'yandex#search'
            });


    // Создаем геообъект с типом геометрии "Точка".
        myGeoObject = new ymaps.GeoObject({
            // Описание геометрии.
            geometry: {
                type: "Point",
                coordinates: [55.8, 37.8]
            },
            // Свойства.
            properties: {
                // Контент метки.
                iconContent: 'Я тащусь',
                hintContent: 'Ну давай уже тащи'
            }
        }, {
            // Опции.
            // Иконка метки будет растягиваться под размер ее содержимого.
            preset: 'islands#blackStretchyIcon',
            // Метку можно перемещать.
            draggable: true
        }),
        myPieChart = new ymaps.Placemark([
            55.847, 37.6
        ], {
            // Данные для построения диаграммы.
            data: [
                {weight: 8, color: '#0E4779'},
                {weight: 6, color: '#1E98FF'},
                {weight: 4, color: '#82CDFF'}
            ],
            iconCaption: "Диаграмма"
        }, {
            // Зададим произвольный макет метки.
            iconLayout: 'default#pieChart',
            // Радиус диаграммы в пикселях.
            iconPieChartRadius: 30,
            // Радиус центральной части макета.
            iconPieChartCoreRadius: 10,
            // Стиль заливки центральной части.
            iconPieChartCoreFillStyle: '#ffffff',
            // Cтиль линий-разделителей секторов и внешней обводки диаграммы.
            iconPieChartStrokeStyle: '#ffffff',
            // Ширина линий-разделителей секторов и внешней обводки диаграммы.
            iconPieChartStrokeWidth: 3,
            // Максимальная ширина подписи метки.
            iconPieChartCaptionMaxWidth: 200
        });


        myMap.geoObjects
            .add(myGeoObject)
            .add(myPieChart)
            .add(new ymaps.Placemark([51.69353117741523,39.144399542327825], {
                balloonContent: '<strong>45 Стрелковой Дивизии 247е</strong>'
            }, {
                preset: 'islands#icon',
                iconColor: '#0095b6'
            }))
            .add(new ymaps.Placemark([51.720326899673985,39.179332386260995], {
                balloonContent: '<strong>Московский пр. 131</strong>'
            }, {
                preset: 'islands#icon',
                iconColor: '#0095b6'
            }))
            .add(new ymaps.Placemark([51.716809714640824,39.179686841278], {
                balloonContent: '<strong>Московский пр. 125</strong>'
            }, {
                preset: 'islands#icon',
                iconColor: '#0095b6'
            }))
            .add(new ymaps.Placemark([51.64077216844209,39.23628202645869], {
                balloonContent: '<strong>Ленински проспект 15</strong>'
            }, {
                preset: 'islands#icon',
                iconColor: '#0095b6'
            }))





    }