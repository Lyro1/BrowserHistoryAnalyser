import aiohttp
import asyncio
from src.Entities.History import History
from src.Entities.HistoryEntry import HistoryEntry
from src.config import Config


sem = asyncio.Semaphore(50)


async def __check_urlhaus(entry: HistoryEntry, service):
    try:
        async with aiohttp.ClientSession() as session:
            data = {'url': entry.url}
            async with session.post(url=service, data=data) as response:
                json = await response.json()
                entry.flagged.url_haus = json['query_status'] == 'ok' and json['url_status'] == 'online'
    except Exception as e:
        print("Unable to get url {} due to {}.".format(service + entry.url, e.__class__))


async def check_urlhaus(entry: HistoryEntry, service):
    async with sem:
        return await __check_urlhaus(entry, service)


async def check_reputation(entry):
    await asyncio.gather(check_urlhaus(entry, "https://urlhaus-api.abuse.ch/v1/url/"))


async def check_all_history(size):
    history = History(size)
    await asyncio.gather(*[check_reputation(entry) for entry in history.entries])
    flaggedEntries = [entry for entry in history.entries if entry.flagged]
    if len(flaggedEntries) == 0:
        print("No warning")
    else:
        [print(entry) for entry in flaggedEntries]


def main():
    config = Config()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(check_all_history(config.max_entries))
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()


if __name__ == '__main__':
    main()
