import pyautogui as p
import keyboard

import time
import keyboard  # Import the keyboard module


target=input("Enter The Name You Want To Send Message\n")

p.moveTo(x=1469, y=1054) ## Tab
p.leftClick()
time.sleep(1)
p.moveTo(x=268, y=155) ## Search Box
p.leftClick()
time.sleep(1)
p.write(target)
time.sleep(1)
p.moveTo(x=193, y=280)
p.leftClick()

i = 0
while i < 1:  # Use "i < 5" for a more Pythonic loop
    p.moveTo(x=1215, y=987)
    p.leftClick()
    p.write("https://youtu.be/A8SythA_P_U?si=Oh8RBGtRW2S8yZZO")
    p.leftClick()
    p.moveTo(x=1873, y=974)
    p.leftClick()

    if keyboard.is_pressed('q'):  # Check for "q" press
        break  # Exit the loop if "q" is pressed

    i += 1  # Increment the counter


# p.dragTo(x=260, y=278,duration=5
# p.moveRel(100, 50) # move x=100, y=50 distances from its current position


# def click_until_q():
#     while True:
#         p.click(x=50, y=100)  # Click at the specified coordinates

#         try:  # Use a try-except block to handle potential errors gracefully
#             if keyboard.is_pressed('q'):  # Check if "q" is pressed
#                 break  # Exit the loop
#         except:
#             pass  # Ignore any errors that might occur

# click_until_q()

# p.write("message", interval=0.4)

