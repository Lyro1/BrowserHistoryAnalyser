
class HistoryEntryFlags:

    def __init__(self):
        self.url_haus = None
        self.virus_total = None

    def __str__(self):
        return 'urlhaus: ' + str(self.url_haus) + ', virus total: ' + str(self.virus_total)