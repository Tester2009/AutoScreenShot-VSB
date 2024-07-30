import pyautogui
import keyboard
import time

def get_corner_position(corner_name):
    print(f"Move your mouse to the {corner_name} corner and press 'c' to capture.")
    while True:
        if keyboard.is_pressed('c'):
            x, y = pyautogui.position()
            print(f"{corner_name} corner position: X: {x}, Y: {y}")
            time.sleep(0.2)  # Prevent multiple captures
            return x, y

def main():
    print("Select the area by capturing four corners.")
    top_left_x, top_left_y = get_corner_position("top-left")
    top_right_x, top_right_y = get_corner_position("top-right")
    bottom_left_x, bottom_left_y = get_corner_position("bottom-left")
    bottom_right_x, bottom_right_y = get_corner_position("bottom-right")
    
    print("\nFinal positions of all corners:")
    print(f"Top-left:     X: {top_left_x}, Y: {top_left_y}")
    print(f"Top-right:    X: {top_right_x}, Y: {top_right_y}")
    print(f"Bottom-left:  X: {bottom_left_x}, Y: {bottom_left_y}")
    print(f"Bottom-right: X: {bottom_right_x}, Y: {bottom_right_y}")
    
    print("\nWaiting for 3 seconds...")
    time.sleep(3)
    
    print("Clicking at position X: 1540, Y: 586...")
    pyautogui.click(1540, 586)
    
    print("Scrolling to the bottom...")
    pyautogui.scroll(-10000)  # A large negative value to ensure scrolling to the bottom
    
    print("Moving to position X: 954, Y: 984 and clicking...")
    pyautogui.click(954, 984)
    
    print("Program ended.")

if __name__ == "__main__":
    main()