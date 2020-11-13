from .HistoryEntryFlags import HistoryEntryFlags

class HistoryEntry(object):

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.flagged = HistoryEntryFlags()

    def __str__(self):
        return self.browser + ': ' + self.url + ' - flagged: ' + str(self.flagged)