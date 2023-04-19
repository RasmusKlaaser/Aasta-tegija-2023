import tkinter as tk
import random

point_total = 0

row1 = 100
row2 = 200
row3 = 300
row4 = 400
row5 = 500


def num_gen():
    nums = []
    possible_results = ["1", "2", "3", "4", "5"]
    for num in range(50):
        row = random.choice(possible_results)
        nums.append(row)
    return nums


dice_nums = num_gen()

roll_final = []
for i in num_gen():
    roll_final.append(i)
    final_num = roll_final[0]
    print(final_num)


class Vocovillak(tk.Tk):

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
        for F in (StartPage, Job, Dice1, Dice2, Game1, Game2, Question1,  Question2,  Question3,  Question4,  Question5,
                  Question6,  Question7,  Question8,  Question9,  Question10,  Question11,  Question12,  Question13,
                  Question14,  Question15,  Question16,  Question17,  Question18,  Question19,  Question20,
                  Question21,  Question22,  Question23,  Question24,  Question25, PointSum1):
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


# The start page.

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Makes a background.
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        # Creates a button to continue to the next page.
        B = tk.Button(C, text="START", fg="gold", bg="#2a3698", font=("Impact", 45),
                      command=lambda: controller.show_frame(Job))

        # Moves the button into the correct place.
        B.pack()
        B.place(bordermode="outside", height=200, width=500, x=700, y=700)

        # Makes the title of the game.
        L = tk.Label(C, text="VOCO-VILLAK", fg="gold", bg="#2a3698", font=("Impact", 80))

        # Moves the title to the correct place.
        L.pack(pady=0, padx=0)
        L.place(bordermode="outside", height=200, width=700, x=600, y=300)

        C.pack(fill="both", expand=True)


class Job(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, text="Tarkvaraarendaja", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: controller.show_frame(Dice1))

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=740, width=855, x=105, y=235)

        B2 = tk.Button(C, text="Süsteemide Spetsialist", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: controller.show_frame(Dice2))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=740, width=855, x=960, y=235)

        L = tk.Label(C, text="Vali eriala!", bg="#2a3698", fg="white", font=("Impact", 50))

        L.pack(pady=0, padx=0)
        L.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        C.pack(fill="both", expand=True)


class Dice1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        result = 0

        def Diceroll1():
            result1 = final_num
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED
            L2['text'] = result1

        def Cmd1():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold", fill="#2a3698")

        C.create_rectangle(755, 480, 1165, 300, width=10, outline="gold", fill="black")

        B1 = tk.Button(C, text="Veereta", bg="#2a3698", fg="yellow", activebackground="#3d4dd2", font=("Impact", 45),
                       command=Diceroll1)

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=200, width=400, x=755, y=540)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: [controller.show_frame(Game1), Cmd1()])
        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Täring", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text=result, bg="black", fg="#3d4dd2", font=("Impact", 45))

        L2.pack(pady=0, padx=0)
        L2.place(bordermode="outside", height=170, width=400, x=760, y=305)

        C.pack(fill="both", expand=True)


class Dice2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        result = 0

        def Diceroll2():
            result2 = final_num
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
            L2['text'] = result2

        def Cmd2():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL

        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold", fill="#2a3698")

        C.create_rectangle(755, 480, 1165, 300, width=10, outline="gold", fill="black")

        B1 = tk.Button(C, text="Veereta", bg="#2a3698", fg="yellow", activebackground="#3d4dd2", font=("Impact", 45),
                       command=Diceroll2)

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=200, width=400, x=755, y=540)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: [controller.show_frame(Game2), Cmd2()])

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Täring", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text=result, bg="black", fg="#3d4dd2", font=("Impact", 45))

        L2.pack(pady=0, padx=0)
        L2.place(bordermode="outside", height=170, width=400, x=760, y=305)

        C.pack(fill="both", expand=True)


class Game1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # The main shape of the question board.
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        # Creates a rectangle for the board.
        C.create_rectangle(100, 990, 1820, 100, width=10, outline="gold", fill="#2a3698")

        # Creates horizontal lines for the board.
        C.create_line(100, 240, 1820, 240, width=10, fill="gold")
        C.create_line(100, 390, 1820, 390, width=10, fill="gold")
        C.create_line(100, 540, 1820, 540, width=10, fill="gold")
        C.create_line(100, 690, 1820, 690, width=10, fill="gold")
        C.create_line(100, 840, 1820, 840, width=10, fill="gold")

        # Creates vertical line for the board.
        C.create_line(540, 100, 540, 985, width=10, fill="gold")
        C.create_line(955, 100, 955, 985, width=10, fill="gold")
        C.create_line(1370, 100, 1370, 985, width=10, fill="gold")

        # The buttons to get to a question.

        B1 = tk.Button(C, state=tk.DISABLED, text=100, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: controller.show_frame(Question1))

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=430, x=105, y=245)

        # The labels for categories.

        L = tk.Label(C, text="ITa", bg="#2a3698", fg="white", font=("Impact", 50))

        L.pack()
        L.place(bordermode="outside", height=130, width=430, x=105, y=105)

        B2 = tk.Button(C, state=tk.DISABLED, text=200, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: controller.show_frame(Question1))
        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=140, width=430, x=105, y=395)

        B3 = tk.Button(C, state=tk.DISABLED, text=300, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question1))
        B3.pack(pady=0, padx=0)
        B3.place(bordermode="outside", height=140, width=430, x=105, y=545)

        B4 = tk.Button(C, state=tk.DISABLED, text=400, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question1))
        B4.pack(pady=0, padx=0)
        B4.place(bordermode="outside", height=140, width=430, x=105, y=695)

        B5 = tk.Button(C, state=tk.DISABLED, text=500, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question1))

        B5.pack(pady=0, padx=0)
        B5.place(bordermode="outside", height=140, width=430, x=105, y=845)

        L = tk.Label(C, text="Õppetöö", bg="#2a3698", fg="white", font=("Impact", 50))

        L.pack()
        L.place(bordermode="outside", height=130, width=400, x=545, y=105)

        B6 = tk.Button(C, state=tk.DISABLED, text=100, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question1))
        B6.pack(pady=0, padx=0)
        B6.place(bordermode="outside", height=140, width=405, x=545, y=245)

        B7 = tk.Button(C, state=tk.DISABLED, text=200, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question2))
        B7.pack(pady=0, padx=0)
        B7.place(bordermode="outside", height=140, width=405, x=545, y=395)

        B8 = tk.Button(C, state=tk.DISABLED, text=300, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question2))
        B8.pack(pady=0, padx=0)
        B8.place(bordermode="outside", height=140, width=405, x=545, y=545)

        B9 = tk.Button(C, state=tk.DISABLED, text=400, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question1))
        B9.pack(pady=0, padx=0)
        B9.place(bordermode="outside", height=140, width=405, x=545, y=695)

        B10 = tk.Button(C, state=tk.DISABLED, text=500, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question1))

        B10.pack(pady=0, padx=0)
        B10.place(bordermode="outside", height=140, width=405, x=545, y=845)

        L = tk.Label(C, text="Hobid", bg="#2a3698", fg="white", font=("Impact", 50))

        L.pack()
        L.place(bordermode="outside", height=130, width=400, x=965, y=105)

        B11 = tk.Button(C, state=tk.DISABLED, text=100, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question2))
        B11.pack(pady=0, padx=0)
        B11.place(bordermode="outside", height=140, width=405, x=960, y=245)

        B12 = tk.Button(C, state=tk.DISABLED, text=200, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question2))
        B12.pack(pady=0, padx=0)
        B12.place(bordermode="outside", height=140, width=405, x=960, y=395)

        B13 = tk.Button(C, state=tk.DISABLED, text=300, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question1))
        B13.pack(pady=0, padx=0)
        B13.place(bordermode="outside", height=140, width=405, x=960, y=545)

        B14 = tk.Button(C, state=tk.DISABLED, text=400, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question1))
        B14.pack(pady=0, padx=0)
        B14.place(bordermode="outside", height=140, width=405, x=960, y=695)

        B15 = tk.Button(C, state=tk.DISABLED, text=500, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question1))

        B15.pack(pady=0, padx=0)
        B15.place(bordermode="outside", height=140, width=405, x=960, y=845)

        L = tk.Label(C, text="VOCO", bg="#2a3698", fg="white", font=("Impact", 50))

        L.pack()
        L.place(bordermode="outside", height=130, width=400, x=1375, y=105)

        B16 = tk.Button(C, state=tk.DISABLED, text=100, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question1))
        B16.pack(pady=0, padx=0)
        B16.place(bordermode="outside", height=140, width=440, x=1375, y=245)

        B17 = tk.Button(C, state=tk.DISABLED, text=200, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question2))
        B17.pack(pady=0, padx=0)
        B17.place(bordermode="outside", height=140, width=440, x=1375, y=395)

        B18 = tk.Button(C, state=tk.DISABLED, text=300, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question1))
        B18.pack(pady=0, padx=0)
        B18.place(bordermode="outside", height=140, width=440, x=1375, y=545)

        B19 = tk.Button(C, state=tk.DISABLED, text=400, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question1))
        B19.pack(pady=0, padx=0)
        B19.place(bordermode="outside", height=140, width=440, x=1375, y=695)

        B20 = tk.Button(C, state=tk.DISABLED, text=500, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question2))

        B20.pack(pady=0, padx=0)
        B20.place(bordermode="outside", height=140, width=440, x=1375, y=845)

        if final_num == 1:
            B1['state'] = tk.NORMAL
            B6['state'] = tk.NORMAL
            B11['state'] = tk.NORMAL
            B16['state'] = tk.NORMAL
        elif final_num == 2:
            B2['state'] = tk.NORMAL
            B7['state'] = tk.NORMAL
            B12['state'] = tk.NORMAL
            B17['state'] = tk.NORMAL
        elif final_num == 3:
            B3['state'] = tk.NORMAL
            B8['state'] = tk.NORMAL
            B13['state'] = tk.NORMAL
            B18['state'] = tk.NORMAL
        elif final_num == 4:
            B4['state'] = tk.NORMAL
            B9['state'] = tk.NORMAL
            B14['state'] = tk.NORMAL
            B19['state'] = tk.NORMAL
        elif final_num == 5:
            B5['state'] = tk.NORMAL
            B10['state'] = tk.NORMAL
            B15['state'] = tk.NORMAL
            B20['state'] = tk.NORMAL

        C.pack(fill="both", expand=True)


class Game2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # The main shape of the question board.
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        # Creates a rectangle for the board.
        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold", fill="#2a3698")

        # Creates horizontal lines for the board.
        C.create_line(100, 240, 1820, 240, width=10, fill="gold")
        C.create_line(100, 390, 1820, 390, width=10, fill="gold")
        C.create_line(100, 540, 1820, 540, width=10, fill="gold")
        C.create_line(100, 690, 1820, 690, width=10, fill="gold")
        C.create_line(100, 840, 1820, 840, width=10, fill="gold")

        # Creates vertical line for the board.
        C.create_line(540, 100, 540, 980, width=10, fill="gold")
        C.create_line(955, 100, 955, 980, width=10, fill="gold")
        C.create_line(1370, 100, 1370, 980, width=10, fill="gold")

        # The buttons to get to a question.

        B1 = tk.Button(C, state=tk.DISABLED, text=100, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: controller.show_frame(Question3))

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=430, x=105, y=245)

        # The labels for categories.

        L = tk.Label(C, text="ITa", bg="#2a3698", fg="white", font=("Impact", 50))

        L.pack()
        L.place(bordermode="outside", height=130, width=430, x=105, y=105)

        B2 = tk.Button(C, state=tk.DISABLED, text=200, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: controller.show_frame(Question3))
        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=140, width=430, x=105, y=395)

        B3 = tk.Button(C, state=tk.DISABLED, text=300, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question3))
        B3.pack(pady=0, padx=0)
        B3.place(bordermode="outside", height=140, width=430, x=105, y=545)

        B4 = tk.Button(C, state=tk.DISABLED, text=400, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question4))
        B4.pack(pady=0, padx=0)
        B4.place(bordermode="outside", height=140, width=430, x=105, y=695)

        B5 = tk.Button(C, state=tk.DISABLED, text=500, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question3))

        B5.pack(pady=0, padx=0)
        B5.place(bordermode="outside", height=140, width=430, x=105, y=845)

        L = tk.Label(C, text="Õppetöö", bg="#2a3698", fg="white", font=("Impact", 50))

        L.pack()
        L.place(bordermode="outside", height=130, width=400, x=545, y=105)

        B6 = tk.Button(C, state=tk.DISABLED, text=100, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question3))
        B6.pack(pady=0, padx=0)
        B6.place(bordermode="outside", height=140, width=405, x=545, y=245)

        B7 = tk.Button(C, state=tk.DISABLED, text=200, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question4))
        B7.pack(pady=0, padx=0)
        B7.place(bordermode="outside", height=140, width=405, x=545, y=395)

        B8 = tk.Button(C, state=tk.DISABLED, text=300, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question4))
        B8.pack(pady=0, padx=0)
        B8.place(bordermode="outside", height=140, width=405, x=545, y=545)

        B9 = tk.Button(C, state=tk.DISABLED, text=400, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45),
                       command=lambda: controller.show_frame(Question3))
        B9.pack(pady=0, padx=0)
        B9.place(bordermode="outside", height=140, width=405, x=545, y=695)

        B10 = tk.Button(C, state=tk.DISABLED, text=500, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question3))

        B10.pack(pady=0, padx=0)
        B10.place(bordermode="outside", height=140, width=405, x=545, y=845)

        L = tk.Label(C, text="Hobid", bg="#2a3698", fg="white", font=("Impact", 50))

        L.pack()
        L.place(bordermode="outside", height=130, width=400, x=965, y=105)

        B11 = tk.Button(C, state=tk.DISABLED, text=100, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question4))
        B11.pack(pady=0, padx=0)
        B11.place(bordermode="outside", height=140, width=405, x=960, y=245)

        B12 = tk.Button(C, state=tk.DISABLED, text=200, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question4))
        B12.pack(pady=0, padx=0)
        B12.place(bordermode="outside", height=140, width=405, x=960, y=395)

        B13 = tk.Button(C, state=tk.DISABLED, text=300, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question3))
        B13.pack(pady=0, padx=0)
        B13.place(bordermode="outside", height=140, width=405, x=960, y=545)

        B14 = tk.Button(C, state=tk.DISABLED, text=400, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question3))
        B14.pack(pady=0, padx=0)
        B14.place(bordermode="outside", height=140, width=405, x=960, y=695)

        B15 = tk.Button(C, state=tk.DISABLED, text=500, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question3))

        B15.pack(pady=0, padx=0)
        B15.place(bordermode="outside", height=140, width=405, x=960, y=845)

        L = tk.Label(C, text="VOCO", bg="#2a3698", fg="white", font=("Impact", 50))

        L.pack()
        L.place(bordermode="outside", height=130, width=400, x=1375, y=105)

        B16 = tk.Button(C, state=tk.DISABLED, text=100, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question3))
        B16.pack(pady=0, padx=0)
        B16.place(bordermode="outside", height=140, width=440, x=1375, y=245)

        B17 = tk.Button(C, state=tk.DISABLED, text=200, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question4))
        B17.pack(pady=0, padx=0)
        B17.place(bordermode="outside", height=140, width=440, x=1375, y=395)

        B18 = tk.Button(C, state=tk.DISABLED, text=300, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question3))
        B18.pack(pady=0, padx=0)
        B18.place(bordermode="outside", height=140, width=440, x=1375, y=545)

        B19 = tk.Button(C, state=tk.DISABLED, text=400, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question3))
        B19.pack(pady=0, padx=0)
        B19.place(bordermode="outside", height=140, width=440, x=1375, y=695)

        B20 = tk.Button(C, state=tk.DISABLED, text=500, bg="#2a3698", fg="white", activebackground="#3d4dd2",
                        font=("Impact", 45),
                        command=lambda: controller.show_frame(Question4))

        B20.pack(pady=0, padx=0)
        B20.place(bordermode="outside", height=140, width=440, x=1375, y=845)

        if final_num == 1:
            B1['state'] = tk.NORMAL
            B6['state'] = tk.NORMAL
            B11['state'] = tk.NORMAL
            B16['state'] = tk.NORMAL
        elif final_num == 2:
            B2['state'] = tk.NORMAL
            B7['state'] = tk.NORMAL
            B12['state'] = tk.NORMAL
            B17['state'] = tk.NORMAL
        elif final_num == 3:
            B3['state'] = tk.NORMAL
            B8['state'] = tk.NORMAL
            B13['state'] = tk.NORMAL
            B18['state'] = tk.NORMAL
        elif final_num == 4:
            B4['state'] = tk.NORMAL
            B9['state'] = tk.NORMAL
            B14['state'] = tk.NORMAL
            B19['state'] = tk.NORMAL
        elif final_num == 5:
            B5['state'] = tk.NORMAL
            B10['state'] = tk.NORMAL
            B15['state'] = tk.NORMAL
            B20['state'] = tk.NORMAL

        C.pack(fill="both", expand=True)


class Question1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Kas VOCO-s on tasuta jõusaal?", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Jah", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Ei", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Koolis on Improring", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Vale", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Õige", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Väiketehnika ringi on tehnikahuvilised, kelle sooviks on ehitada võistlusmasinad \n"
                              " ja lisaks ka nendega kestvussõidu võistlustel osaleda", bg="#2a3698", fg="yellow",
                      font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Õige", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Vale", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Kas VOCO-s on õpiränded tasuta?", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Ei", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Jah", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Kas praktikakohast võib kujuneda \n"
                              " esimene ja kindel töökoht.", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Jah", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Ei", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="VOCO-s on tunniplaan üksluine.", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Vale, see muutub iga nädal", bg="#2a3698", font=("Impact", 50), variable=CheckVar1,
                            onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Õige", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Kas Tartu Rakenduslikus Kolledžis omandad koos tööalaste \n"
                              " praktiliste oskustega nii kutse kui keskhariduse", bg="#2a3698", fg="yellow",
                      font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Jah", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Ei", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Kas Tartu Rakenduslik Kolledž toetab \n "
                              "õpilaste osalemist kutsevõistlustel.", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Kindlasti mitte", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Jah", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Mitu osakonda on VOCO-s?", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="7", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="11", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Mis on VOCO rahvatantsurühma nimi?", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Triskel", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Mõmmikud", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])
        C3 = tk.Checkbutton(C, text="Tornum", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question11(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Mis pille saab kooli bändis mängida?", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Elektrikitarr", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Orel", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])
        C3 = tk.Checkbutton(C, text="Oboe", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question12(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Kus toimub õppetöö ja praktika?", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Labborites", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Pommiaugus", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])
        C3 = tk.Checkbutton(C, text="Põllul", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question13(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Mis on Voco oma enda e-päeviku nimi?", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Siseveeb", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="E-kool", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])
        C3 = tk.Checkbutton(C, text="Stuudium", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question14(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Mida tähendab lühend IT", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Info-teadus", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Info-tehnoloogia", bg="#2a3698", font=("Impact", 50), variable=CheckVar2,
                            onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question15(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Kas selle erialaga saab olulise eelise õpigute jätkamiseks kõrgkoolis \n"
                              "ja võib spetsialiseeruda IT valdkonna profiks?", bg="#2a3698", fg="yellow",
                      font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Jah", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Ei", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question16(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Milline eriala on eriliselt \n"
                              " kiiresti kasvav ja maailma tulevik?", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Veebihaldur", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Tarkvaraarendaja", bg="#2a3698", font=("Impact", 50), variable=CheckVar2,
                            onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question17(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Tegu on globaalse kasvava ettevõtlusvaldkonnaga, kus heade spetsialistide järele \n"
                              " on pidevalt suur nõudlus, mistõttu tarkvaraarendaja \n"
                              " leiab hõlpsasti tööd ka väljaspool Eestit.", bg="#2a3698", fg="yellow",
                      font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Õige", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Vale", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question18(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Tarkvaraarendajad saavad töötada vähestes \n"
                              " valdkondades.", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Õige", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Vale", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question19(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Eesti IT-sektoris on palgatase keskmisest kõrgem ning tarkvaraarendaja \n"
                              "töötasu alumine määr võib ületada \n"
                              " Eesti keskmise töötasu", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Õige", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Vale", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class Question20(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def Rightanswer():
            global point_total
            point_total += 100

        def Wronganswer():
            global point_total
            point_total -= 100

        def Answer():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED

        def Action1():
            if C2['state'] == tk.NORMAL:
                C2['state'] = tk.DISABLED
            else:
                C2['state'] = tk.NORMAL
            if C1['state'] == tk.NORMAL:
                C1['state'] = tk.DISABLED
            else:
                C1['state'] = tk.NORMAL

        def Action2():
            if B1['state'] == tk.NORMAL:
                B1['state'] = tk.DISABLED
            else:
                B1['state'] = tk.NORMAL

        # Creates board
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B1 = tk.Button(C, state=tk.DISABLED, text="Vasta", bg="#2a3698", fg="white", activebackground="#3d4dd2",
                       font=("Impact", 45), command=lambda: [Answer(), Action1()])

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=405, x=755, y=835)

        B2 = tk.Button(C, state=tk.DISABLED, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2",
                       font=("Impact", 35), command=lambda: controller.show_frame(PointSum1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Vasta küsimusele!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="Kas IT-süsteemide spetsialist saab tööle IT-süsteemide \n"
                              "spetsialistina või \n"
                              "klienditoespetsialistina?", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Klienditugi", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Spetsialist", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class PointSum1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B2 = tk.Button(C, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2", font=("Impact", 35),
                       command=lambda: controller.show_frame(Dice1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text=f"Praegune Skoor", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L2 = tk.Label(C, text="current score:", bg="#2a3698", fg="yellow", font=("Impact", 70))
        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=360, width=1000, x=465, y=300)

        C.pack(fill="both", expand=True)

        L2 = tk.Label(C, text=point_total, bg="#2a3698", fg="yellow", font=("Impact", 100))
        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=360, width=1000, x=465, y=300)


class Gameend(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B2 = tk.Button(C, text="RESTART", fg="gold", bg="#2a3698", font=("Impact", 45),
                       command=lambda: controller.show_frame(Job))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text="Mängu Lõpp!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        L1 = tk.Label(C, text="Teie, skoor kokku!", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        C.pack(fill="both", expand=True)


print(point_total)

app = Vocovillak()
app.mainloop()
