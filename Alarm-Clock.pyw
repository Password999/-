try:
    from Tkinter import *
except:
    from tkinter import *

import time
import re
from tkinter import ttk
from winsound import PlaySound, SND_FILENAME, SND_ASYNC


class Clock():
    def __init__(self):
        self.root = Tk()
        self.root.wm_attributes('-topmost', 1)
        self.x, self.y, self.new_x, self.new_y = 0, 0, 1300, 800
        self.window_size = '524x155'
        self.root.geometry(f'{self.window_size}+{self.new_x}+{self.new_y}')  # 窗口大小 宽x高+X+Y
        self.root.overrideredirect(True)  # 标题栏隐藏
        self.root.resizable(0, 0)  # 固定窗口大小
        self.time_label = Label(text="", font=('Helvetica', 100), relief=FLAT, fg='white',
                                bg='black')
        self.time_label.pack()
        self.root.bind("<Button-1>", self.get_x_y) #鼠标单击事件
        self.root.bind("<Double-Button-1>", self.new_run) #鼠标双击事件
        self.root.bind("<B1-Motion>", self.move) #鼠标单击移动事件
        self.start_time = []  # 闹钟列表
        self.now_start = ''
        self.start_Hour = []
        for x in range(24):
            self.start_Hour.append('{:0>2}'.format(x))

        self.start_Minute = []
        for x in range(60):
            self.start_Minute.append('{:0>2}'.format(x))

        self.update_clock()
        self.root.mainloop()

    def get_x_y(self, event):
        self.x, self.y = event.x, event.y

    def move(self, event):
        self.new_x = (event.x - self.x) + self.root.winfo_x()
        self.new_y = (event.y - self.y) + self.root.winfo_y()
        s = f"{self.window_size}+{self.new_x}+{self.new_y}"
        self.root.geometry(s)

    def new_run(self, event):
        new = Toplevel(self.root)
        new.wm_attributes('-topmost', 1)
        new.geometry(f'{self.window_size}+{self.new_x}+{self.new_y}')
        new.overrideredirect(1)
        label_title = Label(new, text='闹钟列表', font=('Helvetica', 20)).pack()  # 标题
        time_list = Label(new, text='', wraplength=500, font=('Helvetica', 15))  # 闹钟列表
        time_list.pack()

        def old_label():
            if len(self.start_time) > 0:
                time_list['text'] = '、'.join(self.start_time)

        old_label()

        def add_label():
            self.text_time()
            a = '、'.join(self.start_time)
            time_list['text'] = a

        def starttime(*args):
            if str(self.H.get()).strip() == '':
                self.now_strat = '07:' + str(self.M.get())
            elif str(self.M.get()).strip() == '':
                self.now_strat = str(self.H.get()) + ':00'
            else:
                self.now_strat = str(self.H.get()) + ':' + str(self.M.get())

        self.H = ttk.Combobox(new, width=2)
        self.H['value'] = self.start_Hour
        self.H.place(x=20, y=125)
        self.H.bind("<<ComboboxSelected>>", starttime)
        Hlabel = Label(new, text='：时')
        Hlabel.place(x=60, y=125)
        self.M = ttk.Combobox(new, width=2)
        self.M['value'] = self.start_Minute
        self.M.place(x=93, y=125)
        self.M.bind("<<ComboboxSelected>>", starttime)
        Mlabel = Label(new, text='：分')
        Mlabel.place(x=130, y=125)
        OK = Button(new, text='添加', command=add_label).place(x=180, y=120)
        Quit = Button(new, text='退出', command=self.root.quit).place(x=450, y=120)
        close = Button(new, text='关闭', command=new.withdraw)
        close.place(x=400, y=120)
        new.mainloop()

    def text_time(self):  # 添加时间
        self.start_time.append(self.now_strat)
        self.start_time = list(set(self.start_time))

    def update_clock(self):  # 刷新时间
        now = time.strftime("%H:%M:%S")
        self.time_label.configure(text=now)
        self.root.after(1000, self.update_clock)
        if time.strftime('%S') == '00':  # 闹钟状态
            self.run_time()

    def run_time(self):  # 闹钟
        reg = re.compile(r'' + time.strftime('%H:%M'))
        t = reg.findall(str(self.start_time))
        if len(t) > 0:
            self.playsound()

    def playsound(self):  # 播放音乐
        PlaySound('./res/Sound.wav', SND_FILENAME | SND_ASYNC)

    def stop_sound(self):  # 关闭音乐
        PlaySound(None, SND_FILENAME)


if __name__ == '__main__':
    Clock()
