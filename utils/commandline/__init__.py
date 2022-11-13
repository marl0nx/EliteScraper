import ctypes
import os
import sys
import threading
import time


def clear():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def slow_title(value: str):
    def thread():
        title = ''
        if sys.platform.startswith('win'):
            for _ in [*value]:
                time.sleep(0.03)
                title += _
                ctypes.windll.kernel32.SetConsoleTitleW(title)
        else:
            pass
    t = threading.Thread(target=thread)
    t.start()


def update_title(value: str):
    if sys.platform.startswith('win'):
        ctypes.windll.kernel32.SetConsoleTitleW(value)
    else:
        pass
