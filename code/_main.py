import ttkbootstrap as tk
from tkinter import messagebox
import ctypes as cp
import _class.plc
import multiprocessing as mp
import threading


class GUI(object):

    def __init__(self) -> None:
        self.plc = _class.plc.Plc()
        self.root = tk.Window(themename='journal')
        screenWidth = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.root.winfo_screenheight()
        self.left = (screenWidth - 1000) / 2
        self.top = (screenHeight - 618) / 2
        self.__win()
        self.__noot()
        self.root.mainloop()
        pass


# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #

    def __win(self):
        self.root.geometry('%dx%d+%d+%d' % (1000, 618, self.left, self.top))
        self.root.resizable(0, 0)
        self.root.title('Tool')

    def __noot(self):
        self.nb = tk.Notebook(self.root, bootstyle='primary', style='NB')
        self.f1 = tk.Frame(self.nb)
        self.f2 = tk.Frame(self.nb)
        self.nb.add(self.f1, text='连接PLC')
        self.nb.add(self.f2, text='开发中')
        self.nb.pack(side='top', fill='both', padx=3, pady=3, expand=True)
if __name__ == '__main__':
    main = GUI()
