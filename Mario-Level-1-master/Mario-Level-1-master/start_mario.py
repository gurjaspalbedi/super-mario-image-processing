# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:31:56 2019

@author: gurjaspal
"""
import pyautogui
import time
import matplotlib.pyplot as plt
import numpy as np
from pynput import keyboard
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
i = 1
all_partitions = []
while True:
#    plt.figure(1)
    image = ImageGrab.grab(dimensions)
    image_np = np.array(image)
    time.sleep(3)
    plt.imsave("battak\screen"+str(i)+".jpg", np.array(image_np))
    i = i +1
#    print(image_np.shape)
#    for m in range(0, image_np.shape[0]-50,50):
#        for n in range(0, image_np.shape[1]-50,50):
#            partition = image_np[m: m + 50, n:n + 50]
#            all_partitions.append(partition)
#            if i < 5000:
##            np.savez_compressed('numpy_data.npz', all_partitions)
#                plt.imsave("partitions\partition"+str(i)+".jpg", np.array(partition))
##    plt.imshow(image)
##    plt.imsave("image_processing\screens\screen"+str(i)+".jpg", np.array(image))
#            i = i + 1