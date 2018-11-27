import time
from pynput.mouse import Controller, Button
from pynput.keyboard import  Controller as Controller1
lon = 330

def shoot():
    mouse = Controller()
    mouse.press(Button.right)
    time.sleep(0.1)
    mouse.release(Button.right)
    time.sleep(1)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)
    mouse.move(1, 0)
    time.sleep(1)
    mouse.press(Button.right)
    time.sleep(0.1)
    mouse.release(Button.right)
    time.sleep(1)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)

def mo(long,ids):
    keyboard = Controller1()
    if ids == 0:
        if long == 0:
            shoot()
        if long>0:
            while long > 0:
                for i in range(lon):
                    keyboard.press('d')
                    keyboard.release('d')
                    time.sleep(0.001)
                time.sleep(1)
                long = long - 1
            shoot()
        if long<0:
            while long < 0:
                for i in range(lon):
                    keyboard.press('a')
                    keyboard.release('a')
                    time.sleep(0.001)
                time.sleep(1)
                long = long + 1
            shoot()
    if ids == 1:
        for i in range(lon):
            keyboard.press('a')
            keyboard.release('a')
            time.sleep(0.001)
        time.sleep(1)
        long = long - 1


def move(num):
    mouse = Controller()
    keyboard = Controller1()
    mouse.position = (750, 400)
    # print(mouse.position)
    #
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)
    time.sleep(1)
    for i in range(350):
        keyboard.press('s')
        keyboard.release('s')
        time.sleep(0.001)

    time.sleep(1)
    for i in range(700):
        keyboard.press('d')
        keyboard.release('d')
        time.sleep(0.001)
    time.sleep(1)
    for i in range(len(num) - 2):
            long = num[i+1] - num[i]
            mo(long, 0)
    long = num[4] - num[5]
    mo(long,1)
