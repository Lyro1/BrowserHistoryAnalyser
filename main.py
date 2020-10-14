import browserhistory as bh
import aiohttp
import asyncio
import requests


async def get(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                resp = await response.read()
                print("Successfully got url {} with response of length {}.".format(url, len(resp)))
    except Exception as e:
        print("Unable to get url {} due to {}.".format(url, e.__class__))


def get_all_history():
    history = bh.get_browserhistory()
    entries = []
    for browser in history:
        entries += [entry[0] for entry in history[browser]]
    return entries


def check_urlhaus(current, response):
    if response.status_code == 404:
        return current + 1, None
    else:
        return current + 1, response.json()


async def check_all_history():
    history = get_all_history()
    if len(history) <= 0:
        print("No entry found.")
    current = 1
    foundDanger = 0

    ret = await asyncio.gather(*[get(url) for url in history])

    print("Results: " + str(foundDanger) + " dangerous URLs found.")


if __name__ == '__main__':


