class Game1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #The main shape of the question board.
        C = tk.Canvas(self, bg="dark blue", height=1080, width=1920)

        #Creates a rectangle for the board.
<<<<<<< HEAD:question_chose_panel.py
        rectangle = C.create_rectangle(100, 990, 1820, 100, width=10, outline="gold")
=======
        rectangle = C.create_rectangle(100, 980, 1820, 100, width=10, outline="gold", fill="#2a3698")
>>>>>>> origin/main:vocovillak.py

        #Creates horizontal lines for the board.
        hz_line1 = C.create_line(100, 240, 1820, 240, width=10, fill="gold")
        hz_line2 = C.create_line(100, 390, 1820, 390, width=10, fill="gold")
        hz_line3 = C.create_line(100, 540, 1820, 540, width=10, fill="gold")
        hz_line4 = C.create_line(100, 690, 1820, 690, width=10, fill="gold")
        hz_line5 = C.create_line(100, 840, 1820, 840, width=10, fill="gold")

        #Creates vertical line for the board.
        vr_line1 = C.create_line(540, 100, 540, 985, width=10, fill="gold")
        vr_line2 = C.create_line(955, 100, 955, 985, width=10, fill="gold")
        vr_line3 = C.create_line(1370, 100, 1370, 985, width=10, fill="gold")

        #The buttons to get to a question.

        B1 = tk.Button(C, text=100, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45), command=lambda: controller.show_frame(Question))

        B1.pack(pady=0, padx=0)
        B1.place(bordermode="outside", height=140, width=430, x=105, y=245)

        # The labels for categories.

        L = tk.Label(C, text="ITa", bg="#2a3698", fg="white", font=("Impact", 50))

        L.pack()
        L.place(bordermode="outside", height=130, width=430, x=105, y=105)

        C.pack(fill="both", expand=True)

        B2 = tk.Button(C, text=200, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45), command=lambda: controller.show_frame(Question))
        B2.pack(pady=0, padx=0)
        B2.place(bordermode="outside", height=140, width=430, x=105, y=395)

        B3 = tk.Button(C, text=300, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                       command=lambda: controller.show_frame(Question))
        B3.pack(pady=0, padx=0)
        B3.place(bordermode="outside", height=140, width=430, x=105, y=545)

        B4 = tk.Button(C, text=400, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                       command=lambda: controller.show_frame(Question))
        B4.pack(pady=0, padx=0)
        B4.place(bordermode="outside", height=140, width=430, x=105, y=695)

        B5 = tk.Button(C, text=500, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                       command=lambda: controller.show_frame(Question))

        B5.pack(pady=0, padx=0)
        B5.place(bordermode="outside", height=140, width=430, x=105, y=845)


        L = tk.Label(C, text="Õppetöö", bg="#2a3698", fg="white", font=("Impact", 50))

        L.pack()
        L.place(bordermode="outside", height=130, width=400, x=545, y=105)

        B6 = tk.Button(C, text=100, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                       command=lambda: controller.show_frame(Question))
        B6.pack(pady=0, padx=0)
        B6.place(bordermode="outside", height=140, width=405, x=545, y=245)

        B7 = tk.Button(C, text=200, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                       command=lambda: controller.show_frame(Question))
        B7.pack(pady=0, padx=0)
        B7.place(bordermode="outside", height=140, width=405, x=545, y=395)

        B8 = tk.Button(C, text=300, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                       command=lambda: controller.show_frame(Question))
        B8.pack(pady=0, padx=0)
        B8.place(bordermode="outside", height=140, width=405, x=545, y=545)

        B9 = tk.Button(C, text=400, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                       command=lambda: controller.show_frame(Question))
        B9.pack(pady=0, padx=0)
        B9.place(bordermode="outside", height=140, width=405, x=545, y=695)

        B10 = tk.Button(C, text=500, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                       command=lambda: controller.show_frame(Question))

        B10.pack(pady=0, padx=0)
        B10.place(bordermode="outside", height=140, width=405, x=545, y=845)

        L = tk.Label(C, text="Hobid", bg="#2a3698", fg="white", font=("Impact", 50))

        L.pack()
        L.place(bordermode="outside", height=130, width=400, x=965, y=105)

        B11 = tk.Button(C, text=100, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                       command=lambda: controller.show_frame(Question))
        B11.pack(pady=0, padx=0)
        B11.place(bordermode="outside", height=140, width=405, x=960, y=245)

        B12 = tk.Button(C, text=200, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                       command=lambda: controller.show_frame(Question))
        B12.pack(pady=0, padx=0)
        B12.place(bordermode="outside", height=140, width=405, x=960, y=395)

        B13 = tk.Button(C, text=300, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                       command=lambda: controller.show_frame(Question))
        B13.pack(pady=0, padx=0)
        B13.place(bordermode="outside", height=140, width=405, x=960, y=545)

        B14 = tk.Button(C, text=400, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                       command=lambda: controller.show_frame(Question))
        B14.pack(pady=0, padx=0)
        B14.place(bordermode="outside", height=140, width=405, x=960, y=695)

        B15 = tk.Button(C, text=500, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                        command=lambda: controller.show_frame(Question))

        B15.pack(pady=0, padx=0)
        B15.place(bordermode="outside", height=140, width=405, x=960, y=845)

        L = tk.Label(C, text="VOCO", bg="#2a3698", fg="white", font=("Impact", 50))

        L.pack()
        L.place(bordermode="outside", height=130, width=400, x=1375, y=105)

        B16 = tk.Button(C, text=100, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                        command=lambda: controller.show_frame(Question))
        B16.pack(pady=0, padx=0)
        B16.place(bordermode="outside", height=140, width=405, x=1375, y=245)

        B17 = tk.Button(C, text=200, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                        command=lambda: controller.show_frame(Question))
        B17.pack(pady=0, padx=0)
        B17.place(bordermode="outside", height=140, width=405, x=1375, y=395)

        B18 = tk.Button(C, text=300, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                        command=lambda: controller.show_frame(Question))
        B18.pack(pady=0, padx=0)
        B18.place(bordermode="outside", height=140, width=405, x=1375, y=545)

        B19 = tk.Button(C, text=400, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                        command=lambda: controller.show_frame(Question))
        B19.pack(pady=0, padx=0)
        B19.place(bordermode="outside", height=140, width=405, x=1375, y=695)

        B20 = tk.Button(C, text=500, bg="#2a3698", fg="white", activebackground="#3d4dd2", font=("Impact", 45),
                        command=lambda: controller.show_frame(Question))

        B20.pack(pady=0, padx=0)
        B20.place(bordermode="outside", height=140, width=405, x=1375, y=845)