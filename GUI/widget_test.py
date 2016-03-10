from Tkinter import *

class Window(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.geometry("600x400+30+30")
        self.wButton = Button(self, text='text', command = self.OnButtonClick)
        self.wButton.pack()

    def OnButtonClick(self):
        self.top = Toplevel()
        self.top.title("title")
        self.top.geometry("300x150+30+30")
        self.top.transient(self)
        self.wButton.config(state='disabled')

        self.topButton = Button(self.top, text="CLOSE", command = self.OnChildClose)
        self.topButton.pack()

    def OnChildClose(self):
        self.wButton.config(state='normal')
        self.top.destroy()

if __name__ == "__main__":
    window = Window(None)

    window.title("title")

    window.mainloop()
