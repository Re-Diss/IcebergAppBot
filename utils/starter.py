import random
from utils.iceberg import IcebergBot
from data import config
from utils.core import logger
import datetime
import pandas as pd
from utils.telegram import Accounts
import asyncio


async def start(thread: int, session_name: str, phone_number: str, proxy: [str, None]):
    iceberg = IcebergBot(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)
    account = session_name + '.session'

    if await iceberg.login():
        while True:
            start_time, stop_time = await iceberg.get_farming()

            # tasks = await iceberg.get_tasks()
            # for task in tasks:
            #     if task['description'] in config.BLACKLIST_TASKS:
            #         continue
            #     if task['status'] == 'new':
            #         await iceberg.change_status(task['id'], 'in_work')
            #         await iceberg.change_status(task['id'], 'ready_collect')
            #         await iceberg.change_status(task['id'], 'collected')
            #     elif task['status'] == 'in_work':
            #         await iceberg.change_status(task['id'], 'ready_collect')
            #         await iceberg.change_status(task['id'], 'collected')
            #     elif task['status'] == 'ready_collect':
            #         await iceberg.change_status(task['id'], 'collected')
            #     else:
            #         continue
            #     logger.success(f'Thread {thread} | {account} | Completed task «{task["description"]}»')
            #     await asyncio.sleep(1)

            if start_time is None and stop_time is None:
                await iceberg.start_farming()
                logger.success(f"Thread {thread} | {account} | Start farming!")

            elif iceberg.current_time() > stop_time:
                status, amount = await iceberg.claim_points()
                if status:
                    logger.success(f"Thread {thread} | {account} | Claimed {amount} points!")
                else:
                    logger.error(f"Thread {thread} | {account} | Can't claim points; response status: {status}")
                await asyncio.sleep(2)

                await iceberg.start_farming()
                logger.success(f"Thread {thread} | {account} | Start farming!")

            else:
                sleep_time = stop_time - iceberg.current_time() + random.randint(*config.DELAYS['BEFORE_CLAIM'])
                logger.info(f"Thread {thread} | {account} | Sleep {sleep_time} seconds...")
                await asyncio.sleep(sleep_time)

            await asyncio.sleep(2)

    else:
        await iceberg.logout()


async def stats():
    accounts = await Accounts().get_accounts()

    tasks = []
    for thread, account in enumerate(accounts):
        session_name, phone_number, proxy = account.values()
        tasks.append(asyncio.create_task(IcebergBot(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy).stats()))

    data = await asyncio.gather(*tasks)

    path = f"statistics/statistics_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv"
    columns = ['Phone number', 'Name', 'Balance', 'Referrals', 'Referral link', 'Proxy (login:password@ip:port)']

    df = pd.DataFrame(data, columns=columns)
    df.to_csv(path, index=False, encoding='utf-8-sig')

    logger.success(f"Saved statistics to {path}")
