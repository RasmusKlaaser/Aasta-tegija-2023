import tkinter as tk
import random

point_total = 0


def numgen():
    list0 = []
    row = 0
    possible_results = [1, 2, 3, 4, 5]
    row = random.choice(possible_results)
    list0.append(row)
    return list0


list1 = []
for i in numgen():
    list1.append(i)
    final_num = list1[0]
    print(final_num)



question_hob_1 = ["Kas VOCO-s on tasuta jõusaal?   (JAH/EI)", "JAH", 100]
questions_hob_4 = ["Koolis on Improring.   (ÕIGE/VALE)", "ÕIGE", 400]
questions_hob_5 = [
    "Väiketehnika ringi on tehnikahuvilised, kelle sooviks on ehitada võistlusmasinad ja lisaks ka nendega kestvussõidu võistlustel osaleda.   (ÕIGE/VALE)",
    "ÕIGE", 500]
questions_ope_3 = ["Kas VOCO-s on õpiränded tasuta?   (JAH/EI)", "JAH", 300]
questions_ope_4 = ["Kas praktikakohast võib kujuneda esimene ja kindel töökoht.   (KINDLASTI/PIGEM MITTE)", "KINDLASTI",
                   400]
questions_ope_5 = ["VOCO-s on tunniplaan üksluine.  (ÕIGE/VALE SEE MUUTUB IGA NÄDAL)", "VALE SEE MUUTUB IGA NÄDAL", 500]
questions_voco_1 = [
    "Kas Tartu Rakenduslikus Kolledžis omandad koos tööalaste praktiliste oskustega nii kutse kui keskhariduse.  (JAH/EI)",
    "JAH", 100]
questions_voco_3 = ["Kas Tartu Rakenduslik Kolledž toetab õpilaste osalemist kutsevõistlustel.  (KINDLASTI MITTE/JAH)",
                    "JAH", 300]
questions_voco_4 = ["Mitu osakonda on VOCO-s?  (7/11)", "7", 400]

questions_hob_2 = ["Mis on VOCO rahvatantsurühma nimi?   (TRISKEL/MÕMMIKUD/TORNUM)", "TRISKEL", 200]
questions_hob_3 = ["Mis pille saab kooli bändis mängida?   (ELEKTRIKITARRI/OREL/OBOE)", "ELEKTRIKITARRI", 300]
questions_voco_2 = ["Kus toimub õppetöö ja praktika? (POMMIAUGUS/LABORITES/PÕLLUL)", "LABORITES", 200]
questions_voco_5 = ["Mis on Voco oma enda e-päeviku nimi?  (E-KOOL/STUUDIUM/SISEVEEB)", "SISEVEEB", 500]
question_4_2 = ["Mida tähendab lühend IT?   (FILM/INFO-TEADUS/INFO-TEHNOLOOGIA)", "INFO-TEHNOLOOGIA", 400]

question_1 = [
    "Kas selle erialaga saab olulise eelise õpigute jätkamiseks kõrgkoolis ja võib spetsialiseeruda IT valdkonna profiks?    (JAH/EI)",
    "JAH", 100]
question_2 = ["Milline eriala on eriliselt kiiresti kasvav ja maailma tulevik?     (TARKVARAARENDJA/VEEBIHALDUR)",
              "TARKVARAARENDAJA", 200]
question_3 = [
    "Tegu on globaalse kasvava ettevõtlusvaldkonnaga, kus heade spetsialistide järele on pidevalt suur nõudlus, mistõttu tarkvaraarendaja leiab hõlpsasti tööd ka väljaspool Eestit.      (ÕIGE/VALE)",
    "õige", 300]
question_4 = ["Tarkvaraarendajad saavad töötada vähestes valdkondades.    (ÕIGE/VALE)", "VALE", 400]
question_5 = [
    "Eesti IT-sektoris on palgatase keskmisest kõrgem ning tarkvaraarendaja töötasu alumine määr võib ületada Eesti keskmise töötasu. (ÕIGE/VALE)",
    "õige", 500]

question_1_2 = [
    "Kas IT-süsteemide spetsialist saab tööle IT-süsteemide spetsialistina või klienditoespetsialistina?    (SPETSIALIST/KLIENDITUGI)",
    "SPETSIALIST", 100]
question_2_2 = ["Kas tegu on ettevõttevaldkonnaga, kus spetsialistie järele on väike nõudlus?    (JAH/EI)", "EI", 200]
question_3_2 = ["Kas IT-spetsialist haldab arvutivõrke, telefoniteenuseid ja vajadusel ehitab müüri?      (JAH/EI)",
                "EI", 300]
# line 33
question_5_2 = [
    "Milliseid võtmeoskusi on vaja edukaks IT-spetsialisti karjääriks?  (ERINEVATE ARVUTIKEELTE TUNDMINE/INVESTEERIMINE/LOOGILINE MÕTLEMINE)",
    "LOOGILINE MÕTLEMINE", 500]


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
        for F in (StartPage, Job, Dice1, Dice2, Game1, Game2, Question1, PointSum1):
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

        #
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        rectangle = C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

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
            result = final_num
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
                B1['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
                B1['state'] = tk.DISABLED
            L2['text'] = result

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

        rectangle = C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold", fill="#2a3698")

        rectangle = C.create_rectangle(755, 480, 1165, 300, width=10, outline="gold", fill="black")

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
            result = final_num
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL
            L2['text'] = result

        def Cmd2():
            if B2['state'] == tk.NORMAL:
                B2['state'] = tk.DISABLED
            else:
                B2['state'] = tk.NORMAL

        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        rectangle = C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold", fill="#2a3698")

        rectangle = C.create_rectangle(755, 480, 1165, 300, width=10, outline="gold", fill="black")

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
        rectangle = C.create_rectangle(100, 990, 1820, 100, width=10, outline="gold", fill="#2a3698")

        # Creates horizontal lines for the board.
        hz_line1 = C.create_line(100, 240, 1820, 240, width=10, fill="gold")
        hz_line2 = C.create_line(100, 390, 1820, 390, width=10, fill="gold")
        hz_line3 = C.create_line(100, 540, 1820, 540, width=10, fill="gold")
        hz_line4 = C.create_line(100, 690, 1820, 690, width=10, fill="gold")
        hz_line5 = C.create_line(100, 840, 1820, 840, width=10, fill="gold")

        # Creates vertical line for the board.
        vr_line1 = C.create_line(540, 100, 540, 985, width=10, fill="gold")
        vr_line2 = C.create_line(955, 100, 955, 985, width=10, fill="gold")
        vr_line3 = C.create_line(1370, 100, 1370, 985, width=10, fill="gold")

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
        rectangle = C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold", fill="#2a3698")

        # Creates horizontal lines for the board.
        hz_line1 = C.create_line(100, 240, 1820, 240, width=10, fill="gold")
        hz_line2 = C.create_line(100, 390, 1820, 390, width=10, fill="gold")
        hz_line3 = C.create_line(100, 540, 1820, 540, width=10, fill="gold")
        hz_line4 = C.create_line(100, 690, 1820, 690, width=10, fill="gold")
        hz_line5 = C.create_line(100, 840, 1820, 840, width=10, fill="gold")

        # Creates vertical line for the board.
        vr_line1 = C.create_line(540, 100, 540, 980, width=10, fill="gold")
        vr_line2 = C.create_line(955, 100, 955, 980, width=10, fill="gold")
        vr_line3 = C.create_line(1370, 100, 1370, 980, width=10, fill="gold")

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

        rectangle = C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

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

        L2 = tk.Label(C, text="question1", bg="#2a3698", fg="yellow", font=("Impact", 50))

        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=260, width=600, x=655, y=300)

        # creating checkboxes

        CheckVar1 = tk.IntVar()
        CheckVar2 = tk.IntVar()
        C1 = tk.Checkbutton(C, text="Vastus 1", bg="#2a3698", font=("Impact", 50), variable=CheckVar1, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Rightanswer(), Action2()])
        C2 = tk.Checkbutton(C, text="Vastus 2", bg="#2a3698", font=("Impact", 50), variable=CheckVar2, onvalue=1,
                            offvalue=0, height=5, width=20, command=lambda: [Wronganswer(), Action2()])

        C1.pack()
        C2.pack()

        C1.place(bordermode="outside", height=130, width=350, x=600, y=600)
        C2.place(bordermode="outside", height=130, width=350, x=960, y=600)

        C.pack(fill="both", expand=True)


class PointSum1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        rectangle = C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B2 = tk.Button(C, text="Edasi >>>", bg="#2a3698", fg="yellow", activebackground="#3d4dd2", font=("Impact", 35),
                       command=lambda: controller.show_frame(Dice1))

        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=100, width=250, x=1565, y=875)

        L1 = tk.Label(C, text=f"Praegune Skoor", bg="#2a3698", fg="white", font=("Impact", 50))

        L1.pack(pady=0, padx=0)
        L1.place(bordermode="outside", height=130, width=1710, x=105, y=105)

        C.pack(fill="both", expand=True)

        L2 = tk.Label(C, text=point_total, bg="#2a3698", fg="yellow", font=("Impact", 100))
        L2.pack(padx=0, pady=0)
        L2.place(bordermode="outside", height=360, width=1000, x=465, y=300)


class Gameend(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        rectangle = C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold")

        B = tk.Button(C, text="RESTART", fg="gold", bg="#2a3698", font=("Impact", 45),
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