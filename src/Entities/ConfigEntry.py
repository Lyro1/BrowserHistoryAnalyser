
class ConfigEntry:

    def __init__(self, enabled=False, api_key=""):
        self.enabled = enabled
        self.api_key = api_key

    def __str__(self):
        return 'enabled: '+str(self.enabled)+', apikey: '+self.api_key
