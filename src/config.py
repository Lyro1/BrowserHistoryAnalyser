import json
import os.path
from src.Entities.ConfigEntry import ConfigEntry


class Config:

    def __init__(self):
        self.limit_entries = False
        self.max_entries = None
        self.max_threads = 50
        self.url_haus = ConfigEntry()
        self.virus_total = ConfigEntry()

    def load_file(self, path=''):
        if len(path) > 1:
            path = path + '/' if path[-1] != '/' else path
        file = path + 'config.json'
        if os.path.isfile(path + 'local.config.json'):
            file = path + 'local.config.json'
            print("charge local config")
        with open(file) as json_file:
            data = json.load(json_file)
            self.limit_entries = data['limit-entries']
            if data['limit-entries']:
                self.max_entries = data['max-entries']
            else:
                self.max_entries = None
            self.max_threads = data['max-threads']
            self.url_haus = ConfigEntry(data['sources']['url-haus']['enabled'])
            self.virus_total = ConfigEntry(data['sources']['virus-total']['enabled'],
                                           data['sources']['virus-total']['api-key'])
            return self

    def modif_file(self, limit_entries=None, max_entries=None, max_threads=None, url_haus_conf=None, virus_total_conf=None,
                   path=''):
        if len(path) > 1:
            path = path + '/' if path[-1] != '/' else path
        response = {}
        response['limit-entries'] = limit_entries if limit_entries is not None else self.limit_entries
        response['max-entries'] = max_entries if max_entries is not None else self.max_entries
        response['max-threads'] = max_threads if max_threads is not None else self.max_threads
        response['sources'] = {
            'url-haus':
                {
                    'enabled': url_haus_conf.enabled if url_haus_conf is not None and url_haus_conf.enabled is not None else self.url_haus.enabled
                },
            'virus-total':
                {
                    'enabled': virus_total_conf.enabled if virus_total_conf is not None and virus_total_conf.enabled is not None else self.virus_total.enabled,
                    'api-key': virus_total_conf.api_key if virus_total_conf is not None and virus_total_conf.api_key is not None else self.virus_total.api_key,
                }
        }
        str_response = json.dumps(response, indent=4)
        file = open(path + 'local.config.json', 'w')
        file.write(str_response)
        file.close()

    def __str__(self):
        return 'Config: \n' + \
               'max_entries = ' + self.max_entries + \
               'max_threads = ' + self.max_threads + \
               'url_haus = ' + self.url_haus + \
               'virus_total = ' + self.virus_total