import aiohttp
import asyncio
from src.Entities.History import History
from src.Entities.HistoryEntry import HistoryEntry
from src.Entities.HistoryEntryFlags import HistoryEntryFlags
from src.config import Config

config = Config()
sem = asyncio.Semaphore(config.max_threads)
flaggedEntries = []


async def __check_urlhaus(entry: HistoryEntry, url):
    try:
        async with aiohttp.ClientSession() as session:
            data = {'url': entry.url}
            async with session.post(url=url, data=data) as response:
                json = await response.json()
                entry.flagged.url_haus = json['query_status'] == 'ok'
    except Exception as e:
        print("Unable to get url {} due to the following error: {}.".format(url, str(e)))


async def check_urlhaus(entry: HistoryEntry):
    async with sem:
        return await __check_urlhaus(entry, "https://urlhaus-api.abuse.ch/v1/url/")


async def __check_virus_total(entry: HistoryEntry, url):
    try:
        async with aiohttp.ClientSession() as session:
            if config.virus_total.enabled and config.virus_total.api_key == "":
                raise Exception("Virus Total check is enabled, but no API key was provided. "
                                "Add a valid API key in the config file.")
            async with session.get(url=url+'?apikey='+str(config.virus_total.api_key)+'&resource='+str(entry.url)) as response:
                if response.status == 200:
                    json = await response.json()
                    entry.flagged.virus_total = (json['positives'] / json['total']) > 0.1
                else:
                    entry.flagged.virus_total = False
    except Exception as e:
        print("Unable to get url {} due to the following error: {}.".format(url, str(e)))


async def check_virus_total(entry: HistoryEntry):
    async with sem:
        return await __check_virus_total(entry, "https://www.virustotal.com/vtapi/v2/url/report")


async def check_reputation(entry):
    if config.url_haus.enabled:
        await asyncio.gather(check_urlhaus(entry))
    if config.virus_total.enabled:
        if config.virus_total.api_key == '':
            raise Exception("Virus Total check is enabled, but no API key was provided. "
                            "Add a valid API key in the config file.")
        await asyncio.gather(check_virus_total(entry))


async def check_all_history(size):
    history = History(size)
    await asyncio.gather(*[check_reputation(entry) for entry in history.entries])
    #[print(str(i) + " " + str(history.entries[i]))for i in range(0, len(history.entries))]
    global flaggedEntries
    flaggedEntries = [entry for entry in history.entries if entry.flagged.url_haus or entry.flagged.virus_total]
    if len(flaggedEntries) == 0:
        print("No warning")
    else:
        [print(entry) for entry in flaggedEntries]

def main():
    config.load_file('src')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(check_all_history(config.max_entries))
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()

def result():
    if len(flaggedEntries) == 0:
        text = "No warning"
    else:
        text = flaggedEntries
    return text


if __name__ == '__main__':
    main()
