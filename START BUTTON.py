import tkinter
top = tkinter.Tk()

C = tkinter.Canvas(top, bg="dark blue", height=1080, width=1920)
B = tkinter.Button(C, text="START", fg="gold", bg="#2a3698", font=("Impact", 45))
B.pack()
B.place(bordermode="outside", height=200, width=500, x=700, y=700)
L = tkinter.Label(C, text="VOCO-VILLAK", fg="gold", bg="#2a3698", font=("Impact", 80))
L.pack()
L.place(bordermode="outside", height=200, width=700, x=600, y=300)
C.pack()

top.mainloop()