import ttkbootstrap as tk
from tkinter import messagebox
import ctypes as cp
import _class.plc
import layout
import multiprocessing as mp
import threading
import layout


class GUI(object):

    def __init__(self) -> None:
        self.plc = _class.plc.Plc()
        self.root = tk.Window(themename='simplex')
        screenWidth = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.root.winfo_screenheight()
        self.left = (screenWidth - 1000) / 2
        self.top = (screenHeight - 618) / 2
        self.__win()
        self.__noot()
        self.__f1()
        self.root.mainloop()
        pass
# ---------------------------------------------------------------------------- #

    def __win(self):
        self.root.geometry('%dx%d+%d+%d' % (1000, 618, self.left, self.top))
        self.root.resizable(0, 0)
        self.root.title('Tool_V0.1_by-KamiDreame')

    def __noot(self):
        self.nb = tk.Notebook(self.root, bootstyle='info')
        self.f1 = tk.Frame(self.nb)
        self.f2 = tk.Frame(self.nb)
        self.nb.add(self.f1, text='连接PLC')
        self.nb.add(self.f2, text='开发中')
        self.nb.pack(side='top', fill='both', padx=3, pady=3, expand=True)

    def __f1(self):
        lf1 = layout.Layout._LableFrame('Empty', self.f1, '连接PLC_ip', 300, 10,
                                        'left', 'y', 3, 3, False)
        self.ipEntry = layout.Layout._Entry('ipEntry', lf1, 17, 'top', 3, 3)
        self.firstRestButton = layout.Layout._Button('firstRestButton', lf1,
                                                     '尝试连接', 20, 'top', 3, 3,
                                                     (self.connectPLC))
        self.firstRestButton.config(bootstyle='info')
        # ---------------------------------------------------------------------------- #
        lf2 = layout.Layout._LableFrame('lf2', self.f1, '数据',100,100,'left','both',3,3,True)
        pass

    def connectPLC(self):
        self.plc.connect(self.ipEntry.get())
        if self.plc.cStatus == 1:
            self.firstRestButton.config(text='当前连接状态:已连接', bootstyle='Primary')
        else:
            self.firstRestButton.config(text='当前连接状态:未连接', bootstyle='info')
    
    def checkPlcData(self):
        
        pass

if __name__ == '__main__':
    main = GUI()
