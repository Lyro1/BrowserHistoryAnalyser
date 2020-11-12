
class HistoryEntryFlags:

    def __init__(self):
        self.url_haus = None
        self.virus_total = None

    def __str__(self):
        return 'urlhaus: ' + self.url_haus + ', virus total: ' + self.virus_total