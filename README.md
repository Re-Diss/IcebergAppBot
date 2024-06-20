# IcebergAppBot Clicker

[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/IcebergAppBot?start=referral_896333795)
#### Join my [Telegram channel](https://t.me/scriptron). I will be posting news about new bots and scripts there.
## Important Notes

> 🇪🇳 README на русском [тут](README-RU.md)

- **Python Version:** The software runs on Python 3.10. Using a different version may cause errors.
- DONT USE MAIN ACCOUNT BECAUSE THERE IS ALWAYS A CHANCE TO GET BANNED IN TELEGRAM


## Functionality
| Functional                                                     | Supported |
|----------------------------------------------------------------|:---------:|
| Multithreading                                                 |     ✅     |
| Binding a proxy to a session                                   |     ✅     |
| Auto-complete tasks; claim points every 6 hours, start mine    |     ✅     |
| Random sleep time between accounts, claim                      |     ✅     |
| Support pyrogram .session                                      |     ✅     |
| Get statistics for all accounts                                |     ✅     |

## Settings data/config.py
| Setting                      | Description                                                                                    |
|------------------------------|------------------------------------------------------------------------------------------------|
| **API_ID / API_HASH**        | Platform data from which to launch a Telegram session _(stock - Android)_                      |
| **DELAYS-ACCOUNT**           | Delay between connections to accounts (the more accounts, the longer the delay) _(eg [5, 15])_ |
| **DELAYS-BEFORE_CLAIM**      | delay before claim points _(eg [5, 15])_                                                       |
| **DELAYS-CHANGE_STATUS_TASK**| CHANGE_STATUS_TASK _(eg [10, 12])_                                                             |
| **PROXY_TYPE**               | Proxy type for telegram session _(eg 'socks5')_                                                |
| **WORKDIR**                  | directory with session _(eg "sessions/")_                                                      |

## Prerequisites
Before you begin, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) **version 3.10**

## Obtaining API Keys
1. Go to my.telegram.org and log in using your phone number.
2. Select "API development tools" and fill out the form to register a new application.
3. Record the API_ID and API_HASH provided after registering your application in the `data/config.py` file.

## Installation
You can download the repository by cloning it to your system and installing the necessary dependencies:
```shell
git clone https://github.com/Re-Diss/IcebergAppBot
cd IcebergAppBot
```


# Linux manual installation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
Next:
- In the terminal, press 3 to create a new session
- Enter the name of the session
- Enter a proxy if necessary. If not necessary, press Enter
- Enter the phone number
- Enter the confirmation code
- After successfully creating a session, we can add another one or press Enter to exit
- Run python3 main.py again
- Press 1 to start the bot
```

You can also use arguments for quick start, for example:
```shell
~/IcebergAppBot >>> python3 main.py --action (1/2)
# Or
~/IcebergAppBot >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Get statistics
# 3 - Create sessions
```

# Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
Next:
- In the terminal, press 3 to create a new session
- Enter the name of the session
- Enter a proxy if necessary. If not necessary, press Enter
- Enter the phone number
- Enter the confirmation code
- After successfully creating a session, we can add another one or press Enter to exit
- Run python main.py again
- Press 1 to start the bot
```

You can also use arguments for quick start, for example:
```shell
~/IcebergAppBot >>> python main.py --action (1/2)
# Or
~/IcebergAppBot >>> python main.py -a (1/2)

# 1 - Run clicker
# 2 - Get statistics
# 3 - Create sessions
```

## Notes
This bot does not need a .env file
All data after creating a session is saved in the sessions folder. In the accounts.json file, you can edit the proxies, insert new ones if the old ones do not work.
