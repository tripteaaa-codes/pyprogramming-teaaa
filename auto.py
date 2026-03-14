# Import the relevant modules

import pyautogui
import time

# Give the python file some time before continuing
time.sleep(3)

# # Mouse Functions

# #print the resolution of your
# print(pyautogui.size()) 
# #print the current position of the mouse 
# print(pyautogui.position())
# #Moves the mouse over time (3 seconds)
# pyautogui.moveTo(100, 100, 3)
# #Move the mouse relative to its current postion
# pyautogui.moveRel(100, 100, 3)
# #click
# pyautogui.tripleClick()
# pyautogui.click(500, 500, 3, 3, button="left")
# pyautogui.doubleClick()
# pyautogui.leftClick()
# pyautogui.rightClick()

# #scrolls up 500
# pyautogui.scroll(500)
# #scrolls down 500
# pyautogui.scroll(-500)

#Moves up and down
# pyautogui.mouseUp(100, 100, button="left")
# pyautogui.mouseDown(100, 100, button="left")

# #Examples of mouse up and down
# pyautogui.mouseDown(300, 400, button="left")
# pyautogui.moveTo(800, 400)
# pyautogui.mouseUp()
# pyautogui.moveTo(100, 400, 3)
 
# #spiral drawing using pyautogui
# time.sleep(1)
# distance = 300
# while distance > 0:
#     pyautogui.dragRel(distance, 0, 1, button="left")
#     distance = distance - 20
#     pyautogui.dragRel(0, distance, 1, button="left")
#     pyautogui.dragRel(-distance, 0, 1, button="left")
#     distance = distance - 20
#     pyautogui.dragRel(0, -distance, 1, button="left")
#     time.sleep(2)
#     pyautogui.leftClick()

# #keyboard function
# pyautogui.write("hello")
# pyautogui.press("enter")
# pyautogui.press("space")

#Dino Game - chrome
time.sleep(3)
for i in range(20):
    pyautogui.press("space")
    time.sleep(0.5)

#Screenshot in pyautogui
pyautogui.screenshot("screeenshot.png")