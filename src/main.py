import WinRegistryWrapper

def main():
    reg = WinRegistryWrapper.WinRegistryWrapper(WinRegistryWrapper.winreg.HKEY_CURRENT_USER, WinRegistryWrapper.RUN_SUB_KEY, WinRegistryWrapper.winreg.KEY_ALL_ACCESS)
    print(reg.getHistory())

    reg.addValue(WinRegistryWrapper.winreg.REG_SZ, WinRegistryWrapper.SAMPLE_VALUE)
    print(reg.getHistory())

    reg.removeValue('b') # change to whatever
    print(reg.getHistory())

if __name__ == "__main__":
    main()