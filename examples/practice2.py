import tkinter as tk
from tkinter import *


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)



        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        for row in range(7):
            container.grid_rowconfigure(row, weight=1)
        for column in range(7):
            container.grid_columnconfigure(column, weight=1)

        self.frames = {}
        for F in (StartPage, Departure, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welkom bij NS", font='Verdana 50', fg='#005ca0', bg='#FBC311')
        label.grid(row=0,column=2,columnspan=4)

        button1 = tk.Button(self, text="Actuele reistijden", command=lambda: controller.show_frame("Departure"),bg='#005ca0', fg='white',width=20,height=5)
        button1.grid(row=2, column=2,sticky='nsew')
        button2 = tk.Button(self, text="Go to Page Two", command=lambda: controller.show_frame("PageTwo"),bg='#005ca0', fg='white',width=20,height=5)
        button2.grid(row=2,column=4)

class Departure(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Actuele vertrektijden", font='Verdana 50', fg='#005ca0', bg='#FBC311')
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start",command=lambda: controller.show_frame("StartPage"),bg='#005ca0', fg='white',width=20,height=5)
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Storingen", font='Verdana 50', fg='#005ca0', bg='#FBC311')
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start", command=lambda: controller.show_frame("StartPage"), bg='#005ca0', fg='white',width=20,height=5)
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.configure(background='#FBC311')
    app.mainloop()

