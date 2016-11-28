

class county:
    def __init__(self, jsonObj):
        self.jsonObj = jsonObj
        self.geo = jsonObj.get("geometry")
        self.name = jsonObj.get("name").lower()
        self.nameFull = jsonObj.get("name") + " County"

