import browserhistory as bh
import aiohttp
import asyncio

sem = asyncio.Semaphore(50)
MAX_HISTORY_ENTRIES = None

async def __get(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                print("Successfully got url {} with status codee {}.".format(url, response.status))
    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))


async def get(url):
    async with sem:
        return await __get(url)


def get_history(size):
    history = bh.get_browserhistory()
    entries = []
    for browser in history:
        if size is not None and len(entries) >= size:
            return entries
        entries += [entry[0] for entry in history[browser]]
    return entries


def check_urlhaus(response):
    return response.status == 404 or response.status == 405


async def check_all_history(size):
    history = get_history(size)
    if len(history) <= 0:
        print("No entry found.")

    await asyncio.gather(*[get("https://urlhaus-api.abuse.ch/v1/url/" + url) for url in history])


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(check_all_history(MAX_HISTORY_ENTRIES))
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
        

if __name__ == '__main__':
    main()

