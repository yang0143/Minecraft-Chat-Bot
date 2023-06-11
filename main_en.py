from tkinter.tix import PopupMenu
import pyperclip
import pyautogui
import sys
import time
import random
from tkinter import messagebox
import threading
from pynput import keyboard
import tkinter as tk

def s():
    # Generate a list of all lowercase letters
    all_letters = list("abcdefghijklmnopqrstuvwxyz")
    # Randomly select 6 different letters, create a permutation, and convert it to a string
    random_letters = ''.join(random.sample(all_letters, 6))
    return random_letters

class MCChatBot:
    
    def __init__(self):
        # Initialize the window
        self.window = tk.Tk()
        self.window.title("Minecraft-Chat-Bot")
        self.window.geometry("350x200")

        # Define the widgets
        text_label = tk.Label(self.window, text="Enter the text you want to send:")
        self.text_entry = tk.Entry(self.window, width=30)

        time_label = tk.Label(self.window, text="Enter the interval time:")
        self.time_entry = tk.Entry(self.window, width=30)

        count_label = tk.Label(self.window, text="Enter the number of times to send:")
        self.count_entry = tk.Entry(self.window, width=30)

        self.start_button = tk.Button(
            self.window, text="Start", command=self.start_bot)
        self.stop_button = tk.Button(
            self.window, text="Stop", command=self.stop_bot, state="disabled")

        # Layout the widgets
        text_label.pack()
        self.text_entry.pack()

        time_label.pack()
        self.time_entry.pack()

        count_label.pack()
        self.count_entry.pack()

        self.start_button.pack(side=tk.LEFT, padx=100)
        self.stop_button.pack(side=tk.RIGHT, padx=100)

        # Window loop
        self.window.mainloop()

    # Start the chatbot operation
    def start_bot(self):
        # Set the state of the start and stop buttons
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"

        # Parse the input content
        try:
            text = self.text_entry.get()
            count = int(self.count_entry.get())
            interval = float(self.time_entry.get())
        except:
            print("Error: Invalid text or decimal value entered")
            self.start_button["state"] = "normal"
            self.stop_button["state"] = "disabled"
            tk.messagebox.showerror("Error", "Error: Invalid input. Please check if the input is valid. The program will exit after clicking OK.")
            sys.exit()

        threading.Thread(target=PopupMenu).start()

        # Set up a thread to stop the operation when a key is pressed
        def stop_function():
            self.started = False

        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()

        self.started = True
        a = 0
        tk.messagebox.showinfo("Prompt", "The bot will start sending messages in 3 seconds. Click OK to run the program normally.")
        time.sleep(3)
        while a < count and self.started:
            time.sleep(interval)
            pyperclip.copy(text)
            pyautogui.press('T')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.typewrite(' ' + s())
            pyautogui.press('Enter')
            a += 1;

        # Stop listening for keyboard events
        listener.stop()
        tk.messagebox.showinfo("Prompt", "The bot has finished the operation!")
         # 恢复按钮状态
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"

    # 停止聊天机器人操作
    def stop_bot(self):
        self.started = False
        
    # 监听F2键盘事件
    def on_press(self, key):
        if key == keyboard.Key.f2:
            self.started = False
            return False
    
    def on_release(self, key):
        pass


if __name__ == "__main__":
    MCChatBot()