import json
import os.path
from src.Entities.ConfigEntry import ConfigEntry


class Config:

    def __init__(self):
        self.max_entries = None
        self.max_threads = 50
        self.url_haus = ConfigEntry()
        self.virus_total = ConfigEntry()

    def load_file(self, path = ''):
        if len(path) > 1:
            path = path if path[-1] != '/' else path+'/'
        file = path + 'config.json'
        if os.path.isfile(path + 'local.config.json'):
            file = path + 'local.config.json'
        with open(file) as json_file:
            data = json.load(json_file)
            if data['limit-entries'] == "True":
                self.max_entries = data['max-entries']
            else:
                self.max_entries = None
            self.max_threads = data['max-threads']
            self.url_haus = ConfigEntry(data['sources']['url-haus']['enabled'] == 'True')
            self.virus_total = ConfigEntry(data['sources']['virus-total']['enabled'] == 'True',
                                           data['sources']['virus-total']['api-key'])
            return self

    def __str__(self):
        return 'Config: \n' +\
               'max_entries = ' + self.max_entries +\
               'max_threads = ' + self.max_threads +\
               'url_haus = ' + str(self.url_haus) +\
               'virus_total = ' + str(self.virus_total)
