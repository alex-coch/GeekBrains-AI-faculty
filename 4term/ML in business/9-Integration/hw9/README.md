# CardioSpike
Итоговый проект курса "Машинное обучение в бизнесе"

### Клонируем репозиторий и создаем образ
```
$ git clone git@github.com:alex-coch/GeekBrains-AI-faculty.git
$ cd "4term/ML in business/9-Integration/hw9/"
$ docker build -t task9/gb_docker_flask_example .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)
```
$ docker run -d -p 8180:8180 -p 8181:8181 task9/gb_docker_flask_example
```

### Переходим на localhost:8181


### Стек:

- ML: catboost, sklearn, pandas, numpy. 
- API: flask. 
Задача: Разработка детектора COVID-19 аномалий в ритме сердца.

### Формат передаваемых данных:
``{'id': [ id0, id1, ... ], 'x': [x0, x1, ...]}``, где
- id - идентификатор пациента
- x - измерения пульса R-R

### Преобразования данных:
- Сериализация в строку JSON - ``json.dumps``
- Кодирование в utf-8 - ``str.encode('utf-8')``

### Основные компоненты системы:
- ``EDA_and_learning_model/CardioSpike2.ipynb`` - EDA и создание модели.
- ``requirements.txt`` - необходимые компоненты для установки на сервер 
- ``app/run_server.py`` - запуск сервера на основе Flask
- ``pipeline.py`` - пайплайн предобработки и постобработки данных. 
- ``app/model/dill_clf_model.dill`` - реализованная модель
- ``app/data`` - примеры профилей пациентов
  - ``app/data/patient_1_non_anomaly.csv`` - предварительно отрицательный диагноз
  - ``app/data/patient_2_anomaly.csv`` - предварительно положительный диагноз
  - ``app/data/patient_3_anomaly.csv`` - предварительно положительный диагноз
- ``test_api/test_api.ipynb`` - тестирование внешнего API
  - ``test_api/data`` - данные для тестирования
