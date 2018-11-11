import json

class PreferenceManager:
    __jsonFilePath = "PyOS-session-data/pref.json"
    __rootDictionary = None

    def __init__(self, path):
        if self.__rootDictionary is None:
            self.__LoadJson()

        path = path.strip("/")

        self.__path = path
        self.__localDictionary = self.__rootDictionary

        if path != "":
            for folder in path.split("/"):
                self.__localDictionary = self.__localDictionary[folder]

    @classmethod
    def __LoadJson(cls):
        jsonFile = open(cls.__jsonFilePath, "r")
        cls.__rootDictionary = json.loads(jsonFile.read())
        jsonFile.close()

    @classmethod
    def __SaveJson(cls):
        jsonFile = open(cls.__jsonFilePath, "w")
        jsonFile.write(json.dumps(cls.__rootDictionary, sort_keys=True, indent=4))
        jsonFile.close()

    def Set(self, key, value):
        self.__localDictionary[key] = value
        self.__SaveJson()

    def Get(self, key):
        return self.__localDictionary[key]

    def GetAttributes(self):
        return list(self.__localDictionary.keys())

    def Remove(self, key):
        del self.__localDictionary[key]
        self.__SaveJson()

    def CreateSubFolder(self, name):
        self.Set(name, dict())
        return self.GetSubFolder(name)

    def GetSubFolder(self, path):
        return PreferenceManager(self.__path + "/" + path)