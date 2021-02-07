import pyautogui
import cv2
import numpy as np

count = 0
i = 0
while (count < 300):
    img = pyautogui.screenshot() # x,y,w,h
    img.save("%d.png"%(i))
    i = i+1
    img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
    count = count + 1
print ('0')