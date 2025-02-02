import cv2
import numpy as np
import pyautogui
import threading
from PIL import ImageGrab
import vgamepad as vg
import time

def screen_grab():
    while True:
        screen_width, screen_height = pyautogui.size()
        capture_width, capture_height = 1000, 800

        x1 = screen_width - capture_width
        y1 = 40
        x2 = screen_width
        y2 = 40 + capture_height

        getScreen = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))

        gray_color = cv2.cvtColor(getScreen, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray_color, threshold1=250, threshold2=300)


        gamepad = vg.VX360Gamepad()

        time.sleep(2)

        gamepad.left_trigger(255)
        gamepad.update()

        time.sleep(1)

        gamepad.left_trigger(0)
        gamepad.update()

        cv2.imshow("Game", edges)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

screen_grab()
