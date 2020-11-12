import aiohttp
import asyncio
from src.Entities.History import History

sem = asyncio.Semaphore(50)
MAX_HISTORY_ENTRIES = None


async def __get(entry, service, check_method):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=service + entry.url) as response:
                check_method(entry, response)
    except Exception as e:
        print("Unable to get url {} due to {}.".format(service + entry.url, e.__class__))


async def get(url, service, check_method):
    async with sem:
        return await __get(url, service, check_method)


def check_urlhaus(entry, response):
    entry.flagged = not (response.status == 404 or response.status == 405)


async def check_reputation(entry):
    await asyncio.gather(get(entry, "https://urlhaus-api.abuse.ch/v1/url/", check_urlhaus))


async def check_all_history(size):
    history = History(size)
    await asyncio.gather(*[check_reputation(entry) for entry in history.entries])
    flaggedEntries = [entry for entry in history.entries if entry.flagged]
    if len(flaggedEntries) == 0:
        print("No warning")
    else:
        [print(entry) for entry in flaggedEntries]


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(check_all_history(MAX_HISTORY_ENTRIES))
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()


if __name__ == '__main__':
    main()
