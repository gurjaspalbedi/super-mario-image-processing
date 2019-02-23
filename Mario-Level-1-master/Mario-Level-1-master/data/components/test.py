#%%
import os
import time
os.chdir("G:\RL-Super-mario\Mario-Level-1-master\Mario-Level-1-master")

from pywinauto.application import Application
app = Application().start("mario_level_1.exe")
time.sleep(2)
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
# dlg_spec = app.UntitledNotepad
# # wait till the window is really open
# actionable_dlg = dlg_spec.wait('visible')



#shell.SendKeys("a") # CTRL+A may "select all" depending on which window's focused

#%%
# import win32com.client
# shell = win32com.client.Dispatch("WScript.Shell")
# hwnd = win32gui.FindWindowEx(0,0,0, "App title")
# win32gui.SetForegroundWindow(hwnd)
# shell.AppActivate("Super Mario Bros 1-1")
# shell.SendKeys("a")
# import win32gui
# hwnd = win32gui.FindWindowEx(0,0,0, "Super Mario Bros 1-1")
# win32gui.SetForegroundWindow(hwnd)
# import pyautogui

# for i in range(999):
#     pyautogui.press("a")
# Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa#%%


#%%


#%%
