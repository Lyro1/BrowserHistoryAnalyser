from browser_history import get_history
from .HistoryEntry import HistoryEntry


class History(object):

    def __init__(self, max_length=None):
        self.entries = []
        self.__get_entries(max_length)
        self.maxLength = max_length

    def __get_entries(self, max_length):
        history = get_history()
        history_entries = history.entries
        history_entries.reverse()
        self.entries = []
        if max_length is not None:
            for entry in history_entries[:max_length]:
                self.entries.append(HistoryEntry(entry[1]))
        else:
            for entry in history_entries:
                self.entries.append(HistoryEntry(entry[1]))
