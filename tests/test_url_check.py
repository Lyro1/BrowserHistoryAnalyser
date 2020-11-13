import pytest
from src.main import *
from src.Entities.HistoryEntry import HistoryEntry


@pytest.mark.asyncio
async def test_url_haus_flagged():
    entry = HistoryEntry("chrome", "http://182.59.75.73:42447/bin.sh")
    await check_urlhaus(entry, "https://urlhaus-api.abuse.ch/v1/url/")
    print("yet")
    assert entry.flagged.url_haus is True


@pytest.mark.asyncio
async def test_url_haus_clean():
    entry = HistoryEntry("chrome", "https://google.com")
    await check_urlhaus(entry, "https://urlhaus-api.abuse.ch/v1/url/")
    print("yet")
    assert entry.flagged.url_haus is False
