import tkinter as tk
from tkinter import ttk


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Dice, Game, Question, Pointsum, Pointtotal):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
class Game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


top = tk.Tk()
top.geometry("1920x1080")

#The main shape of the question board.
C = tk.Canvas(top, bg="#2a3698", height=1080, width=1920)

#Creates a rectangle for the board.
square = C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

#Creates horizontal lines for the board.
hz_line1 = C.create_line(100, 240, 1820, 240, width=10, fill="gold")
hz_line2 = C.create_line(100, 390, 1820, 390, width=10, fill="gold")
hz_line3 = C.create_line(100, 540, 1820, 540, width=10, fill="gold")
hz_line4 = C.create_line(100, 690, 1820, 690, width=10, fill="gold")
hz_line5 = C.create_line(100, 840, 1820, 840, width=10, fill="gold")

#Creates vertical line for the board.
vr_line1 = C.create_line(540, 100, 540, 980, width=10, fill="gold")
vr_line2 = C.create_line(955, 100, 955, 980, width=10, fill="gold")
vr_line3 = C.create_line(1370, 100, 1370, 980, width=10, fill="gold")

#The buttons to get to a question.

B1 = tk.Button(C, text=100, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45), command=lambda: controller.show_frame(Question))

B1.pack(pady=0, padx=0)
B1.place(bordermode="outside", height=140, width=430, x=105, y=245)

# The labels for categories.

L = tk.Label(C, text="ITa", bg="#2a3698", fg="white", font=("Impact", 50))

L.pack()
L.place(bordermode="outside", height=130, width=430, x=105, y=105)

C.pack(fill="both", expand=True)
top.mainloop()
