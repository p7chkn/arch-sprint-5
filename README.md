## Обучение собственной модели

Данные для обучения в папке /data

Команда для обучения:

```bash

rasa train

```

## Запуск проекта

Запустить фронтенд:

```bash

npm install
npm run build
npm run start

```

Запуск API rasa:

```bash

rasa run --enable-api --cors "*" --endpoints endpoints.yml --debug --log-file logs.txt

```


## Логи

Логи запуска API лежат [тут](logs.txt)
