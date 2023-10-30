import winreg
from Consts import *

class WinRegistryWrapper:
    key: winreg.HKEYType = None

    def __init__(self, regKey: winreg.HKEYType, subKey: str, access = winreg.KEY_READ) -> None:
        try:
            self.key = winreg.OpenKeyEx(
                regKey,
                subKey,
                RESERVED,
                access
            )
        except OSError as osError:
            print(ERROR_PREFIX + osError)
            print(INFO_PREFIX + WRONG_KEY_INFO)
    
    def __del__(self):
        if (self.key != None):
            winreg.CloseKey(self.key)
    
    def getHistory(self) -> list:
        subKeys, valueCount, lastModified = winreg.QueryInfoKey(self.key)
        values = {}
        for i in range(valueCount):
            curValue = winreg.EnumValue(self.key, i)
            if (curValue[REG_KEY_NAME_INDEX] == MRU_LIST):
                mruList = curValue[REG_KEY_DATA_INDEX];
            
            else:
                values[curValue[REG_KEY_NAME_INDEX]] = curValue[REG_KEY_DATA_INDEX]

        else:
            sortedHistory = [values[name] for name in mruList]
        
        return sortedHistory
    
    def addValue(self, type: int, value: str) -> None:
        subKeys, valueCount, lastModified = winreg.QueryInfoKey(self.key)
        mruList = ''
        for i in range(valueCount):
            curValue = winreg.EnumValue(self.key, i)
            if (curValue[REG_KEY_NAME_INDEX] == MRU_LIST):
                mruList = curValue[REG_KEY_DATA_INDEX];
                break
        
        name = ''
        if (len(mruList) == MAX_MRU_LIST_LEN):
            name = mruList[-1]
        
        else:
            name = chr(ord(max(mruList)) + 1)

        updatedMruList = name + mruList
        winreg.SetValueEx(self.key, MRU_LIST, RESERVED, type, updatedMruList)

        winreg.SetValueEx(self.key, name, RESERVED, type, value)
        return
    
    def removeValue(self, value: str) -> None:
        subKeys, valueCount, lastModified = winreg.QueryInfoKey(self.key)
        mruList = ''
        for i in range(valueCount):
            curValue = winreg.EnumValue(self.key, i)
            if (curValue[REG_KEY_NAME_INDEX] == MRU_LIST):
                mruList = curValue[REG_KEY_DATA_INDEX]
                break
        
        mruList = mruList.replace(value, '')
        winreg.SetValueEx(self.key, MRU_LIST, RESERVED, winreg.REG_SZ, mruList)

        winreg.DeleteValue(self.key, value)
        return