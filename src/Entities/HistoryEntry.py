from .HistoryEntryFlags import HistoryEntryFlags


class HistoryEntry(object):

    def __init__(self, url):
        self.url = url
        self.flagged = HistoryEntryFlags()

    def __str__(self):
        return self.url + ' - flagged: ' + str(self.flagged)
