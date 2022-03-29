import pyautogui
import time
import pyperclip

time.sleep(5) #waiting 5 seconds to start the spam.

pyperclip.copy('@')


for i in range(9999): # you can change the number "9999" to any number. It indicates how many times it will spam.
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite("everyone")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(1) #spamming every 1 second. you can change this.








