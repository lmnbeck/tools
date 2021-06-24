# coding=UTF-8

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(3)
keyboard.press('\t')
keyboard.release('\t')
time.sleep(0.5)
keyboard.press('\r')
keyboard.release('\r')  
time.sleep(1)

for i in range(5):
    #点下拉列表位置
    keyboard.press('\t')
    keyboard.release('\t')
    time.sleep(0.5)
    keyboard.press('\t')
    keyboard.release('\t')
    time.sleep(0.5)
    keyboard.press('\t')
    keyboard.release('\t')
    time.sleep(0.5)

    #移动并且点下拉列表下一个位置 
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.5)
    
    keyboard.press('\t')
    keyboard.release('\t')
    time.sleep(0.5)
    keyboard.press('\r')
    keyboard.release('\r')
    
    time.sleep(1)


