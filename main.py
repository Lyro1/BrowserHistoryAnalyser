import browserhistory as bh
import aiohttp
import asyncio
import requests


async def get(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                print("Successfully got url {} with status codee {}.".format(url, response.status))
    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))


def get_all_history():
    history = bh.get_browserhistory()
    entries = []
    for browser in history:
        entries += [entry[0] for entry in history[browser]]
    return entries


def check_urlhaus(response):
    if response.status == 404:
        return True
    else:
        return False


async def check_all_history():
    history = get_all_history()
    if len(history) <= 0:
        print("No entry found.")
    foundDanger = 0

    await asyncio.gather(*[get("https://urlhaus-api.abuse.ch/v1/url/" + url) for url in history])


if __name__ == '__main__':
    asyncio.run(check_all_history())

