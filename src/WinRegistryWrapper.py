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

    def getHistory(self) -> tuple[int, int, int]:
        keyInfo = winreg.QueryInfoKey(self.key)
        
        return keyInfo
    
    def editHistory(self, index: int, value: str) -> None:
        return