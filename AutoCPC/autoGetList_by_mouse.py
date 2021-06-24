# coding=UTF-8

from pymouse import PyMouse
from pynput.keyboard import Key, Listener
import time
import os

def autoGetList():
    m = PyMouse()
    a = m.position()    #获取当前坐标的位置(这个东西到时候可以新建个py 获取坐标)
    print(a)

    time.sleep(3)
    m.move(1080, 540)   #下拉列表位
    x = 1080
    y = 540
    try:
        for i in range(25):
            m.click(x, 540, button=1, n=1)   #点下拉列表位置
            
            time.sleep(1)
            m.click(1080, y,1,1)     #移动并且点下拉列表下一个位置 
            y = y + 10
            
            time.sleep(1) 
            m.click(1030, 875,1,2)  #移动并且左击【获取别表】
            
            time.sleep(1)
    except KeyboardInterrupt:
        print('Interrupted!')
        return

def on_press(key):
    # 监听按键
    print('{0} pressed'.format(key))

def on_release(key):
    # 监听释放
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

# 连接事件以及释放
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# if __name__ == "__main__":
    autoGetList() 
