# IcebergAppBot Clicker

[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/IcebergAppBot?start=referral_896333795)
#### Подписывайтесь на наш [телеграм канал](https://t.me/scriptron). Там будут новости о новый ботах
## Важно

- **Python Version:** Программное обеспечение работает на Python 3.10. Использование другой версии может привести к ошибкам.
- НЕ ИСПОЛЬЗУЙТЕ ОСНОВНОЙ АККАУНТ, ПОТОМУ ЧТО ВСЕГДА ЕСТЬ ШАНС ПОЛУЧИТЬ БАН В TELEGRAM


## Функционал
| Функционал                                                                    | Поддерживает |
|-------------------------------------------------------------------------------|:------------:|
| Многопоточность                                                               |      ✅       |
| Привязка прокси к сессии                                                      |      ✅       |
| Авто-исполнение заданий; получайте баллы каждые 6 часов, авто начало майнинга |      ✅       |
| Поддержка pyrogram .session                                                   |      ✅       |
| Получение статистики по аккаунтах                                             |      ✅       |

## Настройки файла data/config.py
| Настройки                      | Описание                                                                |
|------------------------------|-------------------------------------------------------------------------|
| **API_ID / API_HASH**        | Данные платформы, с которой запускать сессию Telegram _(сток - Android) |
| **DELAYS-ACCOUNT**           | Заддержка между подключением аккаунтов _(напр [5, 15])_                 |
| **DELAYS-BEFORE_CLAIM**      | Задержка перед клеймом _(напр [5, 15])_                                 |
| **DELAYS-CHANGE_STATUS_TASK**| Задержка между исполнением заданий _(напр [10, 12])_                    |
| **PROXY_TYPE**               | Тип прокси _(напр 'socks5')_                                            |
| **WORKDIR**                  | папка с сессиями _(eg "sessions/")_                                     |

## Предварительные условия
Прежде чем начать, убедитесь, что у вас установлено следующее:
- [Python](https://www.python.org/downloads/) **version 3.10**

## Получение API ключей
1. Перейдите на сайт [my.telegram.org](https://my.telegram.org) и войдите в систему, используя свой номер телефона.
2. Выберите **"API development tools"** и заполните форму для регистрации нового приложения.
3. Запишите `API_ID` и `API_HASH` в файле `.env`, предоставленные после регистрации вашего приложения.

## Установка
Вы можете скачать [**Репозиторий**](https://github.com/Re-Diss/IcebergAppBot) клонированием на вашу систему и установкой необходимых зависимостей:
```shell
git clone https://github.com/Re-Diss/IcebergAppBot.git
cd IcebergAppBot
```

# Linux
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Здесь вы обязательно должны указать ваши API_ID и API_HASH , остальное берется по умолчанию
python3 main.py
```

# Windows
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Указываете ваши API_ID и API_HASH, остальное берется по умолчанию
python main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/IcebergAppBot >>> python3 main.py --action (1/2)
# Или
~/IcebergAppBot >>> python3 main.py -a (1/2)

# 1 - Запускает кликер
# 2 - Получить статистику
# 3 - Создает сессию
