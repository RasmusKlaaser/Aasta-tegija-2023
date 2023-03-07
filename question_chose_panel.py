import tkinter
top = tkinter.Tk()

# The main shape of the question board.

C = tkinter.Canvas(top, bg="dark blue", height=1080, width=1920)

square = C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

hz_line1 = C.create_line(100, 240, 1820, 240, width=10, fill="gold")
hz_line2 = C.create_line(100, 390, 1820, 390, width=10, fill="gold")
hz_line3 = C.create_line(100, 540, 1820, 540, width=10, fill="gold")
hz_line4 = C.create_line(100, 690, 1820, 690, width=10, fill="gold")
hz_line5 = C.create_line(100, 840, 1820, 840, width=10, fill="gold")

vr_line1 = C.create_line(540, 100, 540, 980, width=10, fill="gold")
vr_line2 = C.create_line(955, 100, 955, 980, width=10, fill="gold")
vr_line3 = C.create_line(1370, 100, 1370, 980, width=10, fill="gold")

C.pack()

# The buttons to get to a question.

B = tkinter.Button(top, state="disabled")
top.mainloop()
