from PreferenceManager import PreferenceManager
import os

def RunApp(AppFileName):
    import types
    import importlib.machinery

    loader = importlib.machinery.SourceFileLoader(AppFileName, "PyOS-session-data/Apps/" + AppFileName + ".py")
    mod = types.ModuleType(loader.name)
    loader.exec_module(mod)

def InstallApp(AppCode, AppFileName, AppName):
    AppPref = PreferenceManager("Apps")
    AppPref.Set(AppFileName, AppName)
    Install_Code = open("PyOS-session-data/Apps/" + AppFileName, "w")
    Install_Code.write(AppCode)
    Install_Code.close()

def RemoveApp(AppFileName):
    AppPref = PreferenceManager("Apps")
    AppPref.Remove(AppFileName)
    os.remove("PyOS-session-data/Apps/" + AppFileName)

def GetAppName(AppFileName):
    AppPref = PreferenceManager("Apps")
    return AppPref.Get(AppFileName)

def GetAppList():
    AppPref = PreferenceManager("Apps")
    return AppPref.GetAttributes()
