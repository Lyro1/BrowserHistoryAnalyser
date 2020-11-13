import browserhistory as bh
from .HistoryEntry import HistoryEntry

class History(object):

    def __init__(self, maxLength = None):
        self.entries = []
        self.__get_entries(maxLength)
        self.maxLength = maxLength

    def __get_entries(self, maxLength):
        history = bh.get_browserhistory()
        self.entries = []
        for browser in history:
            if maxLength is not None and len(self.entries) >= maxLength:
                return
            for entry in history[browser]:
                self.entries.append(HistoryEntry(browser, entry[0]))
