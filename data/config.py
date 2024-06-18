# api id, hash
API_ID = 1488
API_HASH = 'abcde1488'

DELAYS = {
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
    'BEFORE_CLAIM': [5, 15],   # delay before claim points
    'CHANGE_STATUS_TASK': [10, 12],  # delay between change statuses of tasks delay between change statuses of tasks
}

# proxy type
PROXY_TYPE = "socks5"  # "socks4", "socks5" and "http" are supported

# title blacklist tasks (do not change)
BLACKLIST_TASKS = ['Invite 5 friends', 'Invite 10 friends', 'Invite 15 friends']

# session folder (do not change)
WORKDIR = "sessions/"

# timeout in seconds for checking accounts on valid
TIMEOUT = 30
