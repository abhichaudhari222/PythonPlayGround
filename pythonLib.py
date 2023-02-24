import pyautogui
import time
pyautogui.FAILSAFE = False
while True:
    for i in range(40,50):
        pyautogui.moveTo(50 ,i * 5)
    time.sleep(10)
    

    

