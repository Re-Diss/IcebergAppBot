import argparse

from utils.core import create_sessions, logger
from utils.telegram import Accounts
from utils.starter import start, stats
import asyncio
from itertools import zip_longest
from utils.core import get_all_lines
import os

start_text = """

+-------------------------------------+
|                                     |
|          IcebergAppBot              |
|                                     |
+-------------------------------------+
Select an action:

    1. Run claimer
    2. Get statistics
    3. Create sessions
"""


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', type=int, help='Action to perform')

    action = parser.parse_args().action

    if not action:
        print(start_text)

        while True:
            action = input("> ")

            if not action.isdigit():
                logger.warning("Action must be number")
            elif action not in ['1', '2', '3']:
                logger.warning("Action must be 1, 2 or 3")
            else:
                action = int(action)
                break

    # action = int(input("Select action:\n1. Start soft\n2. Get statistics\n3. Create sessions\n\n> "))

    if not os.path.exists('sessions'): os.mkdir('sessions')
    if not os.path.exists('sessions/accounts.json'):
        with open("sessions/accounts.json", 'w') as f:
            f.write("[]")

    if action == 3:
        await create_sessions()

    if action == 2:
        if not os.path.exists('statistics'): os.mkdir('statistics')
        await stats()

    if action == 1:
        accounts = await Accounts().get_accounts()

        tasks = []
        for thread, account in enumerate(accounts):
            session_name, phone_number, proxy = account.values()
            tasks.append(asyncio.create_task(start(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
