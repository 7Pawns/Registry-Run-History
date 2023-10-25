import WinRegistryWrapper

def main():
    reg = WinRegistryWrapper.WinRegistryWrapper(WinRegistryWrapper.winreg.HKEY_CURRENT_USER, WinRegistryWrapper.RUN_SUB_KEY)
    print(reg.getHistory())


if __name__ == "__main__":
    main()