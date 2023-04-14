import pyperclip
import keyboard
import os
import winreg

def add_to_startup():
    pth = os.path.dirname(os.path.realpath(__file__))
    s_name = "winzard.pyw"
    address = os.path.join(pth, s_name)
    key = winreg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    open_key = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(open_key, "WinZard", 0, winreg.REG_SZ, address)
    winreg.CloseKey(open_key)

def clear_clipboard():
    pyperclip.copy('')
    print('Clipboard cleared.')

def main():
    shortcut_key = 'ctrl+end'
    keyboard.add_hotkey(shortcut_key, clear_clipboard)
    add_to_startup()
    keyboard.wait()

if __name__ == '__main__':
    main()