import AppKit
import pyautogui
import time

curr = pyautogui.position()  
moveToX = curr[0]
moveToY = curr[1]

count = 100
while count >0 :
    pyautogui.click(x=moveToX, y=moveToY, clicks=5, interval=0.1, button='left')
    time.sleep(8)
    pyautogui.scroll(-100, x=moveToX, y=moveToY)
    pyautogui.scroll(-100, x=moveToX, y=moveToY)
    print(count)
    count -= 1
# pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')


# pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

