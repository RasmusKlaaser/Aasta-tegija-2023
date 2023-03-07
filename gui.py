import tkinter
top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=250, width=300)


square = C.create_polygon(50, 60, 70, 80, fill="red")

C.pack()
top.mainloop()