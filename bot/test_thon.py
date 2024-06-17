import sys
import asyncio
from database_stuff import async_get_records

async def get_user_balance(user):
    ...
    info = await async_get_records(user, ...)
    ...
    return info['balance']

async def main(users):
    user_coroutines = []
    for user in users:
        user_coroutines.append(get_user_balance(user))

    balances = await asyncio.gather(*user_coroutines)
    return balances

async def test(suser):
    #suser = await client.get_entity('Sie0205')
    _last = None


    from datetime import date
    from telethon.tl.types import UserStatusOnline, UserStatusOffline

    if isinstance(suser.status, UserStatusOnline):
        _last = date(suser.status.expires.year, suser.status.expires.month, suser.status.expires.day)

    if isinstance(suser.status, UserStatusOffline):
        _last = date(suser.status.was_online.year, suser.status.was_online.month, suser.status.was_online.day)

    print(_last)
    return _last

if __name__ == '__main__':
    users = sys.argv[1:]
    loop = asyncio.get_event_loop()
    balances = loop.run_until_complete(main(users))
    print(balances)
    test(main(users))


