from pynput.keyboard import Controller, Key
import time

keyboard = Controller()
time.sleep(2)
keyboard.press(Key.up)
