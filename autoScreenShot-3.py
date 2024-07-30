# https://claude.ai/chat/03844ea1-142b-4e87-a35f-94c76de1840a
import pyautogui
import time
import os
import platform
import img2pdf
from PIL import Image

def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')

def take_screenshot(left, top, right, bottom, iteration):
    screenshot = pyautogui.screenshot(region=(left, top, right-left, bottom-top))
    filename = f"temp_screenshot_{iteration:02d}.png"
    screenshot.save(filename)
    print(f"Screenshot {iteration} taken")
    return filename

def create_pdf(image_files):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    pdf_filename = f"screenshots_{timestamp}.pdf"
    
    with open(pdf_filename, "wb") as f:
        f.write(img2pdf.convert(image_files))
    
    print(f"PDF saved as {pdf_filename}")
    
    # Remove temporary PNG files
    for file in image_files:
        os.remove(file)

def main():
    clear_terminal()
    print("Running AutoScreenshot Program by Hakase")
    print("----------------------------------------")
    print("Program will start in 3 seconds...")
    time.sleep(3)
    
    image_files = []
    
    for i in range(1019):
        print(f"\nIteration {i+1} of 1019")
        
        # Take screenshot
        print("Taking screenshot...")
        image_file = take_screenshot(500, 5, 1419, 1193, i+1)
        image_files.append(image_file)
        
        pyautogui.click(1612, 681)
        pyautogui.click(1612, 681)
        
        print("Sleeping for 1.5 seconds...")
        time.sleep(1.5)
        
        print("Scrolling down...")
        pyautogui.scroll(-10000)
        time.sleep(0.5)
        pyautogui.scroll(-10000)
        time.sleep(0.5)
        
        print("Clicking at X: 957, Y: 1098")
        pyautogui.click(957, 1098)
        
        time.sleep(0.5)
        
        print("Iteration complete")

    create_pdf(image_files)

if __name__ == "__main__":
    main()
    print("All iterations complete. Program ended.")