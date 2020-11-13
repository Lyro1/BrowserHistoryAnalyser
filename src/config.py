import json
from src.Entities.ConfigEntry import ConfigEntry


class Config:

    def __init__(self):
        with open('config.json') as json_file:
            data = json.load(json_file)
            self.max_entries = data['max-entries']
            self.url_haus = ConfigEntry(data['sources']['url-haus']['enabled'] == 'True')
            self.virus_total = ConfigEntry(data['sources']['virus-total']['enabled'] == 'True',
                                           data['sources']['virus-total']['api-key'])
