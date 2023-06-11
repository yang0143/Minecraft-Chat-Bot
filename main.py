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
    # 生成所有小写字母列表
   all_letters = list("abcdefghijklmnopqrstuvwxyz")
    # 随机抽取6个不同的字母，生成一个排列并转换为字符串
   random_letters = ''.join(random.sample(all_letters, 6))
   return random_letters
   

class MCChatBot:
    
    def __init__(self):
        # 初始化窗口
        self.window = tk.Tk()
        self.window.title("Minecraft-Chat-Bot")
        self.window.geometry("350x200")

        # 定义控件
        text_label = tk.Label(self.window, text="输入你要发送的文本:")
        self.text_entry = tk.Entry(self.window, width=30)

        time_label = tk.Label(self.window, text="输入间隔时间:")
        self.time_entry = tk.Entry(self.window, width=30)

        count_label = tk.Label(self.window, text="输入发送次数:")
        self.count_entry = tk.Entry(self.window, width=30)

        self.start_button = tk.Button(
            self.window, text="开始", command=self.start_bot)
        self.stop_button = tk.Button(
            self.window, text="停止", command=self.stop_bot, state="disabled")

        # 布局控件
        text_label.pack()
        self.text_entry.pack()

        time_label.pack()
        self.time_entry.pack()

        count_label.pack()
        self.count_entry.pack()

        self.start_button.pack(side=tk.LEFT, padx=100)
        self.stop_button.pack(side=tk.RIGHT, padx=100)

        # 窗口循环
        self.window.mainloop()

    # 开始聊天机器人操作
    def start_bot(self):
        # 设置开始和停止按钮状态
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"

        # 解析输入内容
        try:
            text = self.text_entry.get()
            count = int(self.count_entry.get())
            interval = float(self.time_entry.get())
        except:
            print("错误：不可以输入非法的文本或小数")
            self.start_button["state"] = "normal"
            self.stop_button["state"] = "disabled"
            tk.messagebox.showerror("错误","错误：非法的输入 请检查输入是否合法:( 点击确定后就会直接退出哟。")
            sys.exit()  
        # 弹出提示框
       
            

        threading.Thread(target=PopupMenu).start()

        # 设置线程，可以在按下键盘时停止操作
        def stop_function():
            self.started = False

        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()

        self.started = True
        a = 0
        tk.messagebox.showinfo("提示","机器人将在3秒钟后开始发送信息 点击确定后 程序才能正常运行")
        time.sleep(3)
        while a < count and self.started:
            time.sleep(interval)
            pyperclip.copy(text)
            pyautogui.press('T')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.typewrite(' '+s())
            pyautogui.press('Enter')
            a += 1;

        # 停止监听键盘事件
        listener.stop()
        tk.messagebox.showinfo("提示","机器人已操作完成!")
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