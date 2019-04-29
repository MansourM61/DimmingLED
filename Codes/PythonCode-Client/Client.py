# -*- coding: utf-8 -*-
"""
Arduino LED Brightness Controller
Mojtaba Mansour Abadi
OCRG
Northumbria University
"""


import serial
import time
from tkinter import *
import os


class WinApp(Frame):

    # Main Window
    WinTitle = "LED Brightness Controller"    

    def __init__(self, master = None):
        Frame.__init__(self, master)
        master.protocol("WM_DELETE_WINDOW", self.quitapp)
        self.master = master

        self.master.title(self.WinTitle)

        self.create_app_frame()
        
        self.ledlux_s.config(from_=0, to=100, orient=HORIZONTAL, resolution=1, length=300)
        self.ledLux.set(50)
        self.ledState.set(False)

        self.appfrm.pack()

        master.resizable(False, False)
        
        os.system('xset r off')
        
        self.ser = serial.Serial('/dev/ttyACM0', 230400)

        self.master.after(100, self.refreshPort);
        pass

    def create_app_frame(self):
        self.appfrm = Frame(master=self, relief=GROOVE, padx=5, pady=5 ,borderwidth=1)
        
        self.ledLux = DoubleVar()
        self.ledState = IntVar()
        
        self.Frame_1 = Frame(master=self.appfrm , relief=GROOVE, padx=5, pady=5 ,borderwidth=1)
                
        self.quitbtt = Button(master=self.Frame_1, text="Exit", command=self.quitapp, width=20)
        self.ledstat = Checkbutton(master=self.Frame_1, text="LED", command=self.changestate, variable=self.ledState, width=20)

        self.ledlux_s = Scale(master=self.appfrm, label="LED Brightness", command=self.changelux, variable=self.ledLux, width=20)        

        self.quitbtt.grid(row=0, column=0)
        self.ledstat.grid(row=0, column=1)
        
        self.Frame_1.pack()
        self.ledlux_s.pack()
        pass
    
    def quitapp(self):
        print("Exiting the app...\n")
        self.master.destroy()
        self.ser.close()
        os.system('xset r on')
        pass

    def changestate(self):
        state = "on" if(self.ledState.get()) else "off"
        print("LED state is changed to " + state)
        value = self.ledLux.get() * (1 if self.ledState.get() else 0)
        self.ser.write(b"L:" + str.encode(str(value)) + b"$\n")
        pass

    def changelux(self, d):
        lux = self.ledLux.get()
        print("Lux is changed to " + str(lux))
        value = self.ledLux.get() * (1 if self.ledState.get() else 0)
        self.ser.write(b"L:" + str.encode(str(value)) + b"$\n")
        time.sleep(0.1)
        pass

    def refreshPort(self):
        self.ser.flush()
        self.master.after(100, self.refreshPort);
        pass


def main():
    root = Tk()
    App = WinApp(master = root)
    App.pack()
    root.mainloop()
    pass

if __name__ == '__main__':
    main()