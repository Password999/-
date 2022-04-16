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
        self.root.geometry('524x191+1300+800')  # 窗口大小 宽x高+X+Y
        self.root.overrideredirect(1)  # 标题栏隐藏
        self.root.resizable(0, 0)  # 固定窗口大小
        self.time_button = Button(text="", font=('Helvetica', 100), command=self.new_run, relief=FLAT, fg='white',
                                  bg='black')
        self.time_button.pack()
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

    def new_run(self):
        new = Toplevel(self.root)
        new.geometry('524x191+1300+800')
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
        self.H.place(x=20, y=135)
        self.H.bind("<<ComboboxSelected>>", starttime)
        Hlabel = Label(new, text='：时')
        Hlabel.place(x=60, y=135)
        self.M = ttk.Combobox(new, width=2)
        self.M['value'] = self.start_Minute
        self.M.place(x=93, y=135)
        self.M.bind("<<ComboboxSelected>>", starttime)
        Mlabel = Label(new, text='：分')
        Mlabel.place(x=130, y=135)
        OK = Button(new, text='添加', command=add_label).place(x=180, y=130)
        Quit = Button(new, text='退出', command=self.root.quit).place(x=450, y=130)
        close = Button(new, text='关闭', command=new.withdraw)
        close.place(x=400, y=130)
        new.mainloop()

    def text_time(self):  # 添加时间
        self.start_time.append(self.now_strat)
        self.start_time = list(set(self.start_time))

    def update_clock(self):  # 刷新时间
        now = time.strftime("%H:%M:%S")
        self.time_button.configure(text=now)
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
