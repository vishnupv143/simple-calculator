import time
import timeit

import tkinter as tk
from tkinter import PhotoImage
light= "#F6F6F6"
white ="#000000"
small=("arial",16)
large=("arial",40,"bold")
but= ("arial",24,"bold")
class caluclator():



    def __init__(self):
        self.core=tk.Tk()
        self.core.geometry('375x667')
        self.core.resizable(width=None,height=None)
        self.core.title("Netowrk")
        self.total = ""
        self.current =""
        self.display = self.display_frame()
        self.digit={
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            0:(4,2),".":(4,1)

        }
        self.operator={"/":"➗","*":"❌", "-":"➖","+":"➕"

        }
        self.button = self.button_frame()
        self.label,self.labels =self.display_label()
        for x in range(1,5):
            self.button.rowconfigure(x,weight=1)
            self.button.columnconfigure(x,weight=1)
        self.ip_button()
        self.operator_but()
        self.call_method()
        self.bind()







    def display_label(self):
        label = tk.Label(self.display,text=self.total,bg=light,fg=white,anchor=tk.E,font=small)
        label.pack(expand=True,fill='both')

        labels =tk.Label(self.display,text=self.current,bg=light,fg=white,anchor=tk.E,font=large)
        labels.pack(expand= True,fill ='both')
        return label,labels





    def display_frame(self):
        frame = tk.Frame(self.core,height=221,bg=light)
        frame.pack(expand=True,fill='both')
        return frame

    def update_total(self):

        self.label.config(text=self.total)

    def update_current(self):
        self.labels.config(text=self.current[:11])



    def add_to(self,value):
        self.current+= str(value)
        self.update_current()

    def ip_button(self):
        for digits,grid_value in self.digit.items():
            button = tk.Button(self.button,text=str(digits),bg=light,fg=white,font=but,borderwidth=0,command=lambda x=digits: self.add_to(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)

    def fun_operator(self,operator):
        self.current+=operator
        self.total+=self.current
        self.current =""
        self.update_total()
        self.update_current()

    def operator_but(self):
        i = 0
        for operator,symbol in self.operator.items():
            button = tk.Button(self.button,text=symbol,bg=light,fg=white,borderwidth=0,command=lambda y= operator:self.fun_operator(y))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1


    def bind(self):
        self.core.bind("<Return>",lambda event:self.evaluate())
        self.core.bind("<BackSpace>",lambda event:self.add_clear())
        for key in self.digit:
            self.core.bind(str(key),lambda event,digit=key:self.add_to(digit))

        for key in self.operator:
            self.core.bind(key,lambda event,digit=key:self.fun_operator(digit))


    def call_method(self):
        self.clear()
        self.equal()
        self.square()

    def add_clear(self):
        self.current=""
        self.total=""
        self.update_current()
        self.update_total()


    def clear(self):
        button =tk.Button(self.button,text="⚡",bg=light,fg=white,font=but,borderwidth=0,command=self.add_clear)
        button.grid(row=0,column=1,columnspan=2,sticky=tk.NSEW)


    def evaluate(self):
        self.total += self.current
        self.update_total()
        self.current = str(eval(self.total))
        self.total=""
        self.update_current()



    def equal(self):
        button = tk.Button(self.button, text="🐒", bg=light, fg=white,font=but,borderwidth=0,command=self.evaluate )
        button.grid(row=4, column=3,columnspan=2, sticky=tk.NSEW)


    def sq(self):
        self.current=str(eval(f'{self.current}**2'))
        self.update_current()

    def square(self):
        button = tk.Button(self.button, text="X²", bg=light, fg=white,font=small,borderwidth=0,command=self.sq )
        button.grid(row=0, column=3, sticky=tk.NSEW)


    def button_frame(self):
        frame =tk.Frame(self.core)
        frame.pack(expand=True,fill='both')
        return frame





    def run(self):
        self.core.mainloop()










if __name__ == '__main__':
    hp = caluclator()
    hp.run()