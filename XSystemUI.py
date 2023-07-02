import tkinter as tk
from distutils.command.config import config
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk


class XSystemUI:
    # UI Properties
    ui_title = "Medical Expert System for Diagnosing"
    ui_dimensions = "600x500"
    ui_background_color = "#FFFFFF"

    # Buttons Properties
    yesBtn_bgColor = "#5FB691"
    noBtn_bgColor = "#5FB691"
    label_bgColor = "white"
    app_icon = Image.open('images/doc_1.png')

    def getYes(self):
        if self.lan == 1:
            return "yes"
        else:
            return "نعم"

    def getNo(self):
        if self.lan == 1:
            return "no"
        else:
            return "لا"

    def const_text_1(self):
        if self.lan == 1:
            return "SELF CARE"
        else:
            return ".رعاية ذاتية"

    def const_text_2(self):
        if self.lan == 1:
            return "Recommendations".center(20, "*")
        else:
            return "التوصيات".center(20, "*")

    def get_first_question(self):
        if self.lan == 1:
            return "Q1: Do you have pain or burning with urination?"
        else:
            return "هل لديك حرقة في البول؟"

    def __init__(self, lan):

        self.lan = lan
        self.root = Tk()
        app_icon = ImageTk.PhotoImage(self.app_icon)
        self.root.wm_iconphoto(False, app_icon)
        self.root.title(self.ui_title)
        self.root.geometry(self.ui_dimensions)
        self.root.config(bg=self.ui_background_color)
        self.answer = ""
        self.temp = ""

        helvFont22 = tkFont.Font(family="Helvetica", size=22, weight="bold")
        helvFont20 = tkFont.Font(family="Helvetica", size=20, weight="bold")
        self.helvFont14 = tkFont.Font(family="Helvetica", size=14, weight="bold")

        self.var = tk.IntVar()

        self.label2 = Label(self.root,
                            text=self.get_first_question(),
                            wraplength=400,
                            justify="center",
                            bg="white",
                            font=helvFont22)
        self.label2.grid(row=0, column=1)
        self.label2.place(relx=0.5, rely=0.35, anchor=CENTER)

        self.btn1 = Button(self.root, text=self.getYes(), command=lambda: self.var.set(1), width=15, height=3,
                           bg=self.yesBtn_bgColor)
        self.btn1.grid(row=1, column=0)
        self.btn1.place(relx=0.3, rely=0.7, anchor=CENTER)

        self.btn2 = Button(self.root, text=self.getNo(), command=lambda: self.var.set(0), width=15, height=3,
                           bg=self.noBtn_bgColor)
        self.btn2.grid(row=1, column=2)
        self.btn2.place(relx=0.7, rely=0.7, anchor=CENTER)

        self.btn1.wait_variable(self.var)
        if self.var.get():
            self.temp = self.getYes()
        else:
            self.temp = self.getNo()

    def ask_question(self, question):
        self.label2['text'] = question
        self.label2.place(relx=0.5, rely=0.35, anchor=CENTER)

        self.btn1 = Button(self.root, text=self.getYes(), command=lambda: self.var.set(1), width=15, height=3,
                           bg=self.yesBtn_bgColor)
        self.btn1.grid(row=1, column=0)
        self.btn1.place(relx=0.3, rely=0.7, anchor=CENTER)

        self.btn2 = Button(self.root, text=self.getNo(), command=lambda: self.var.set(0), width=15, height=3,
                           bg=self.noBtn_bgColor)
        self.btn2.grid(row=1, column=2)
        self.btn2.place(relx=0.7, rely=0.7, anchor=CENTER)

        self.btn1.wait_variable(self.var)

        if self.var.get():
            self.answer = self.getYes()
        else:
            self.answer = self.getNo()

        return self.answer

    def print_result(self, header, body, advice):
        self.root.destroy()

        self.root = Tk()
        app_icon = ImageTk.PhotoImage(self.app_icon)
        self.root.wm_iconphoto(False, app_icon)
        self.root.title("Diagnosis Result")
        ui_dimensions = "750x690"
        self.root.geometry(ui_dimensions)
        self.root.config(bg=self.ui_background_color)
        self.var = tk.IntVar()

        self.header_label = Label(self.root,
                                  text=header,
                                  wraplength=400,
                                  justify="center",
                                  font=self.helvFont14,
                                  bg=self.label_bgColor)

        self.body_label = Label(self.root,
                                text=body,
                                wraplength=700,
                                justify="center",
                                font=self.helvFont14,
                                fg="red",
                                bg=self.label_bgColor)

        self.label4 = Label(self.root,
                            text=self.const_text_2(),
                            wraplength=400,
                            justify="center",
                            font=self.helvFont14,
                            fg="green",
                            bg=self.label_bgColor)

        self.label3 = Label(self.root,
                            text=self.const_text_1(),
                            wraplength=400,
                            justify="center",
                            font=self.helvFont14,
                            bg=self.label_bgColor)

        self.advice_label = Label(self.root,
                                  text=advice,
                                  wraplength=400,
                                  justify="center",
                                  font=self.helvFont14,
                                  bg=self.label_bgColor)

        self.header_label.grid(row=1, column=0)
        self.body_label.grid(row=2, column=0)
        self.label4.grid(row=3, column=0)
        self.label3.grid(row=4, column=0)
        self.advice_label.grid(row=5, column=0)

        self.header_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.body_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.label4.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.label3.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.advice_label.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.btn1 = Button(self.root, text="OK", command=lambda: self.var.set(1), width=18, height=3,
                           bg=self.yesBtn_bgColor)
        self.btn1.grid(row=6, column=0)
        self.btn1.place(relx=0.5, rely=0.8, anchor=CENTER)

        self.btn1.wait_variable(self.var)
        return 0
