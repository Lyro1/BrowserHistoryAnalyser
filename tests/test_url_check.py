import pytest
from main import *
from src.Entities.HistoryEntry import HistoryEntry
from src.config import Config

config = Config()
config.load_file('../src/')

@pytest.mark.asyncio
async def test_url_haus_flagged():
    entry = HistoryEntry("chrome", "http://182.59.75.73:42447/bin.sh")
    await check_urlhaus(entry)
    assert entry.flagged.url_haus is True


@pytest.mark.asyncio
async def test_url_haus_clean():
    entry = HistoryEntry("chrome", "https://google.com")
    await check_urlhaus(entry)
    assert entry.flagged.url_haus is False


@pytest.mark.asyncio
async def test_virus_total_flagged():
    entry = HistoryEntry("chrome", "http://182.59.75.73:42447/bin.sh")
    await check_virus_total(entry)
    assert entry.flagged.virus_total is True


@pytest.mark.asyncio
async def test_virus_total_clean():
    entry = HistoryEntry("chrome", "https://google.com")
    await check_virus_total(entry)
    assert entry.flagged.virus_total is False
