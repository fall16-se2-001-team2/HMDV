import codecs
import json
from Provider import Provider
class ProviderList:
    providers = []
    def __init__(self, fileName, count=2):
        with codecs.open(fileName, 'r', 'utf-8') as f:
            providersData = json.load(f)
        tally = 0
        for p in providersData:
            self.providers.append(Provider(p))
            tally += 1
            if tally == count:
                break

