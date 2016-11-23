import sys
import json
from Provider import Provider
class ProviderList:
    providers = []
    def __init__(self, fileName):
        with open(fileName) as f:
            for line in f:
                data = line
                self.providers.append(Provider(data))