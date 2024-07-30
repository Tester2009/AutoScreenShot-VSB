import pyautogui
import time
import os
import platform

def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')

def take_screenshot(left, top, right, bottom):
    screenshot = pyautogui.screenshot(region=(left, top, right-left, bottom-top))
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot.save(f"screenshot_{timestamp}.png")
    print(f"Screenshot saved as screenshot_{timestamp}.png")

def main():
    clear_terminal()
    print("Running AutoScreenshot Program by Hakase")
    print("----------------------------------------")
    print("Program will start in 3 seconds...")
    time.sleep(3)
    
    for i in range(10):
        print(f"\nIteration {i+1} of 10")
        
        # Take screenshot
        print("Taking screenshot...")
        take_screenshot(500, 5, 1419, 1193)
        
        # Click at specified point
        print("Clicking at X: 1612, Y: 681")
        pyautogui.click(1612, 681)
        
        # Sleep for 1 second
        print("Sleeping for 1 second...")
        time.sleep(1)
        
        # Scroll down
        print("Scrolling down...")
        pyautogui.scroll(-10000)  # Large negative value to scroll to bottom
        
        # Sleep for 1 second
        print("Sleeping for 1 second...")
        time.sleep(1)
        
        # Click at specified point
        print("Clicking at X: 957, Y: 1098")
        pyautogui.click(957, 1098)
        
        print("Iteration complete")

if __name__ == "__main__":
    main()
    print("All iterations complete. Program ended.")