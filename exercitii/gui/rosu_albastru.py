from tkinter import Tk, Frame, Label
import time


class Root(Tk):
    def __init__(self):
        super().__init__()
        
        self.rosu = Frame(self, \
        background="red")
        
        self.rosu.pack(\
            anchor="center", \
            fill="both", \
            side="top", \
            expand="yes")
            
        self.albastru = Frame(self, \
        bg="blue")
        
        self.albastru.pack(\
            anchor="center", \
            fill="both", \
            side="top", \
            expand="yes")
            
        for i in range(200):
            self.albastru.configure(bg="black")
            self.update()
            time.sleep(.1)
            self.albastru.configure(bg="blue")
            self.update()
            
            self.rosu.configure(bg="black")
            self.update()
            time.sleep(.1)
            self.rosu.configure(bg="red")
            self.update()
            
            

root = Root()
root.mainloop()
