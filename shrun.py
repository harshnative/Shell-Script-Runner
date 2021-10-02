from genericpath import isfile
import settingsFile
import time
import sys
import os
import getpass
from pathlib import Path

# class containing global variables
class GlobalData:

    username = getpass.getuser()

    filePath = "/home/{}/Documents/shellScriptRunner.txt".format(username)

    settingsDict = {}





















# class for settings functionality
class Settings:

    # setting up the object 
    settingObj = settingsFile.SettingsClass(GlobalData.filePath)

    # method to return the dict
    @classmethod
    def returnDict(cls):
        try:
            returnedDict = cls.settingObj.getDict()

            # if the retruned dict length is zero then restore the settings file
            if(len(returnedDict) == 0):
                cls.restoreSettings()
                time.sleep(0.5)

            return returnedDict

        except Exception as e:
            return {}

    
    # method to restore the settings file with default settings
    @classmethod
    def restoreSettings(cls):
        try:
            cls.settingObj.regenerateSettingsFile()
            return True
        except Exception as e:
            return False



try:
    scriptToRun = sys.argv[1]
except IndexError:
    print("pass the name of the shell script to execute")
    sys.exit()


GlobalData.settingsDict = Settings.returnDict()

if(len(GlobalData.settingsDict) == 0):
    print("Add some scripts to settingsFile")
    sys.exit()




pathOfScriptToRun = GlobalData.settingsDict.get(scriptToRun , None)

if(pathOfScriptToRun.lower() == "none"):
    print("script {} not found".format(scriptToRun))

    print("\nyou can choose from these - ")

    for i,j in GlobalData.settingsDict.items():
        print(i)


my_file = Path(pathOfScriptToRun)
if(not(my_file.is_file())):
    print("script corresponding to {} not found , check path in setting file at {}".format(scriptToRun , GlobalData.filePath))


os.chdir(os.getcwd())
os.system("sh {}".format(pathOfScriptToRun))