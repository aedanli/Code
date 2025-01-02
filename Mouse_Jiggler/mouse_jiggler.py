import pyautogui
import time
import random

def move_mouse():
    while True:
        x, y = pyautogui.position()
        print(f"Current position: ({x}, {y})")

        x_rand = random.randint(-500,500)
        y_rand = random.randint(-500,500)
        pyautogui.moveRel(x_rand, y_rand, duration=0.25)
        print(f"Moved to: ({x + x_rand}, {y + y_rand})")

        pyautogui.moveRel(x_rand*-1, y_rand*-1, duration=0.25)
        print(f"Moved back to: ({x}, {y})")

        time.sleep(300)

if __name__ == "__main__":
    print("Starting the mouse jiggler script...")
    move_mouse()

