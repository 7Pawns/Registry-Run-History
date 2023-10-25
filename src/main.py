import WinRegistryWrapper

def main():
    reg = WinRegistryWrapper.WinRegistryWrapper(WinRegistryWrapper.winreg.HKEY_CURRENT_USER, 'Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU')
    print(reg.getHistory())

    return

if __name__ == "__main__":
    main()