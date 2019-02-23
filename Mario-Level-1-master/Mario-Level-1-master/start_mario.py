# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:31:56 2019

@author: gurjaspal
"""
import pyautogui
import time
import matplotlib.pyplot as plt
import numpy as np
from pywinauto.application import Application
app = Application().start("mario_level_1.exe")
import cv2
#time.sleep(3)
#pyautogui.PAUSE = 10

#print("working")
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
pyautogui.PAUSE = 1
pyautogui.click()
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
#pyautogui.PAUSE = 3
#im1 = pyautogui.screenshot('screenshot.png')
#pyautogui.screenshot('someButton.png', region=(0,0, 300, 400))
pyautogui.PAUSE = 3

from PIL import ImageGrab
import win32gui

hwnd = win32gui.FindWindow(None, r'Super Mario Bros 1-1')
win32gui.SetForegroundWindow(hwnd)
dimensions = win32gui.GetWindowRect(hwnd)

while True:
    plt.figure(1)
    image = ImageGrab.grab(dimensions)
    plt.imshow(image)
    plt.show()
#    print(image)
#    cv2.imshow('Image', np.array(image))
#position = pyautogui.locateOnScreen("mario_title.jpg", confidence = 0.1)
#print(position)
#for i in range(1000):
#pyautogui.keyDown('right')

#
#import win32com.client
#
#
#shell = win32com.client.Dispatch("WScript.Shell")
##shell.SendKeys("a") # CTRL+A may "select all" depending on which window's focused
#
#shell.SendKeys("{ENTER}")
 #Press tab... to change focus or whatever