import tkinter as tk
from tkinter import *
from tkinter import messagebox

from PIL.Image import Resampling

from arXSysem import LoadsAr
from XSystem import LoadsEn
from PIL import Image, ImageTk
import tkinter.font as tkFont


class Main:
    # UI Properties
    ui_title = "Medical Expert System for Diagnosing"
    ui_dimensions = "630x550"
    ui_background_color = "#FFFFFF"

    # Buttons Properties
    yesBtn_bgColor = "#5FB691"
    noBtn_bgColor = "#5FB691"
    lable_bgColor = "white"
    app_icon = Image.open('images/doc_1.png')

    def __init__(self):

        # object of TK() window
        self.root = Tk()
        app_icon = ImageTk.PhotoImage(self.app_icon)
        self.root.wm_iconphoto(False, app_icon)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.title(self.ui_title)
        self.root.geometry(self.ui_dimensions)
        self.root.config(bg="white")

        self.answer = ""
        self.temp = ""

        img = Image.open("images/bac.jpg")
        bgApp = ImageTk.PhotoImage(img)

        # Add image
        label = Label(self.root, image=bgApp)
        label.place(x=0, y=0)

        helvFont22 = tkFont.Font(family="Helvetica", size=22, weight="bold")
        helvFont20 = tkFont.Font(family="Helvetica", size=20, weight="bold")

        self.var = tk.IntVar()

        # Create an object of tkinter ImageTk

        # frame = Frame(self.root, width=50, height=50)
        # frame.pack()
        # frame.place(anchor='center', relx=0.5, rely=0.5)
        # img = ImageTk.PhotoImage(Image.open("images/doc.jpg"))
        img = (Image.open("images/doc.jpg"))
        resized_image = img.resize((130, 130), Resampling.LANCZOS)
        new_image = ImageTk.PhotoImage(resized_image)

        # Create an Image Label
        header_img = Label(self.root, image=new_image)
        header_img.grid(row=0, column=0)
        header_img.place(relx=0.85, rely=0.2, anchor=CENTER)

        header_label = Label(self.root,
                             text="             نظام خبير لتشخيص أمراض الجهاز البولي",
                             wraplength=550,
                             justify="center",
                             bg='#ffff00',
                             fg="#2577c8",
                             font=helvFont22)
        header_label.grid(row=0, column=1)
        header_label.place(relx=0.3, rely=0.2, anchor=CENTER)

        # self.label1 = Label(self.root, image="::tk::icons::question")
        # self.label1.grid(row=0, column=0)

        self.label2 = Label(self.root,
                            text="اختر اللغة",
                            wraplength=400,
                            justify="center",
                            bg="white",
                            font=helvFont20)
        self.label2.grid(row=1, column=2, ipady=20)
        self.label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.btn1 = Button(self.root, text="عربي", command=lambda: self.var.set(1), width=15, height=3,
                           bg=self.yesBtn_bgColor)
        self.btn1.grid(row=3, column=1, ipady=10, ipadx=10)
        self.btn1.place(relx=0.3, rely=0.65, anchor=CENTER)

        self.btn2 = Button(self.root, text="انكليزي", command=lambda: self.var.set(0), width=15, height=3,
                           bg=self.noBtn_bgColor)
        self.btn2.grid(row=3, column=2, ipady=10, ipadx=10)
        self.btn2.place(relx=0.7, rely=0.65, anchor=CENTER)

        self.btn1.wait_variable(self.var)
        if self.var.get() == 1:
            self.root.destroy()
            engine = LoadsAr()
            engine.reset()
            engine.run()
        elif self.var.get() == 0:
            self.root.destroy()
            engine = LoadsEn()
            engine.reset()
            engine.run()
        elif self.var.get() == -1:
            self.root.destroy()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.var.set(-1)


Main()
