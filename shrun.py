import settingsFile
import time
import sys

# class containing global variables
class GlobalData:
    settingsDict = {}

    settingsPath = "/opt/shellScriptRunner"

    dataBase = "linesOfCodeCounter_db.db"



# class for settings functionality
class Settings:

    # setting up the object 
    settingObj = settingsFile.SettingsClass(GlobalData.settingsPath)

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

    # method to open the settings file
    # returns True on successfull opening 
    # else returns false and logs error
    @classmethod
    def openSettingsFile(cls):
        result = cls.settingObj.openSettings()

        if(result == None):
            return True
        else:
            return False

    
    # method to restore the settings file with default settings
    @classmethod
    def restoreSettings(cls):
        try:
            cls.settingObj.regenerateSettingsFile()
            return True
        except Exception as e:
            return False




# cache the settings dict in main memory
try:
    GlobalData.settingsDict = Settings.returnDict()

# if the cache fails then the settings file retored may not have been written due to not availabilty of cpu
except Exception as e:
    time.sleep(1)

    # after one second jarvis will try again
    try:
        GlobalData.settingsDict = Settings.returnDict()

        # if jarvis fails this time also then the computer must have been in deadlock state or jarvis does not have read write permission to program's data folder
    except Exception as e:
        print("Could not load the settings file , cpu does not responded or shrun does not have read write permission , Try again in some time :(")
        print("\n\nPress enter to continue")
        input()
        sys.exit()






