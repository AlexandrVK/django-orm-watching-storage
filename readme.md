# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.\
Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

### Как установить

Перед началом использования скрипта необходимо установить следующие переменные окружения:
- `SECRET_KEY`: секретный ключ для доступа к БД сайта
- `PORT`:  порт для доступа к БД сайта
- `NAME`:  имя пользователя для доступа к БД сайта
- `USER`:  логин для доступа к БД сайта
- `HOST`: адрес доступа к БД сайта
- `PASSWORD`:  пароль доступа к БД сайта
- `ALLOWED_HOSTS`: домен, где развёрнут сайт
- `DEBUG`:  Отключение/включение отладочного режима работы сайта - принимает значения `False/True`

Переменные окружения необходими прописать в файле `.env` 

Python3 должен быть уже установлен.\
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).