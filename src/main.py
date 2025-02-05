import time

import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
from pynput.keyboard import Controller, Key

base_point = (2040, 770)


def screen_grab():
    while True:
        # screen_width, screen_height = pyautogui.size()
        # capture_width, capture_height = 1024, 768
        #
        # x1 = screen_width - capture_width
        # y1 = 40
        # x2 = screen_width
        # y2 = 40 + capture_height
        #
        # getScreen = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
        #
        # gray_color = cv2.cvtColor(getScreen, cv2.COLOR_RGB2GRAY)
        # edges = cv2.Canny(gray_color, threshold1=200, threshold2=300)

        x1, y1 = 1536, 420
        x2, y2 = 2560, 847

        getScreen = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))

        gray_color = cv2.cvtColor(getScreen, cv2.COLOR_RGB2GRAY)

        edges = cv2.Canny(gray_color, threshold1=200, threshold2=300)

        contours, _ = cv2.findContours(
            edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        # Convert grayscale to BGR for drawing
        edge_display = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        # Find the closest edge points
        min_dist = float("inf")
        closest_point = None

        for contour in contours:
            for point in contour:
                px, py = point[0]  # Extract x, y coordinates
                # Euclidean distance
                dist = np.linalg.norm(np.array(base_point) - np.array((px, py)))

                if dist < min_dist:
                    min_dist = dist
                    closest_point = (px, py)

        # Draw the reference base point
        cv2.circle(
            edge_display, (base_point[0] - x1, base_point[1] - y1), 5, (0, 0, 255), -1
        )

        # Draw the closest edge point
        if closest_point:
            cv2.circle(
                edge_display,
                (closest_point[0] - x1, closest_point[1] - y1),
                5,
                (0, 255, 0),
                -1,
            )
            cv2.line(
                edge_display,
                (base_point[0] - x1, base_point[1] - y1),
                (closest_point[0] - x1, closest_point[1] - y1),
                (255, 0, 0),
                2,
            )

        # Display the result
        cv2.imshow("Track Edge Detection", edge_display)

        # Quit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
        # keyboard = Controller()
        # keyboard.press(Key.up)


def main():
    time.sleep(3)
    screen_grab()


main()
