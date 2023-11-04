import ttkbootstrap as tk
from tkinter import messagebox
import ctypes as cp


class GUI(object):
    def __init__(self) -> None:
        self.root = tk.Window(themename='journal')
        screenWidth = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.root.winfo_screenheight()
        self.left = (screenWidth - 1000) / 2
        self.top = (screenHeight - 618) / 2
        self.__win()
        self.__noot()
        self.root.mainloop()
        pass

    def __win(self):
        self.root.geometry('%dx%d+%d+%d' % (1000, 618, self.left, self.top))
        self.root.resizable(0, 0)

    def __noot(self):
        self.nb = tk.Notebook(self.root, bootstyle='primary')
        self.f1 = tk.Frame(self.nb)
        self.f2 = tk.Frame(self.nb)
        self.__Lf1()
        self.nb.add(self.f1, text='连接PLC')
        self.nb.add(self.f2, text='开发中')
        self.nb.pack(side='top', fill='both', padx=3, pady=3, expand=True)

    def __Lf1(self):
        self.lf1 = tk.LabelFrame(
            self.f1, text='Connect', width=200, bootstyle='info')
        self.lf1.pack(side='left', fill='y', padx=3, pady=3)
        self.lf1_1 = tk.Frame(self.lf1, style='success',
                              height=100,)
        self.lf1_1.pack(side='top', fill='x')
        self.conLab = tk.Label(self.lf1_1, text='ip地址:'fo).pack(side='left')

        tk.Button(self.lf1, text='连接Plc', width=30).pack(
            side='top', padx=2, pady=3)
        tk.Button(self.lf1, text='断开Plc', width=15).pack(
            side='top', padx=2, pady=3)
        self.lf2 = tk.LabelFrame(self.f1, text='连接', bootstyle='info')
        self.lf2.pack(side='left', fill='both', padx=3, pady=3, expand=True)


GUI()
