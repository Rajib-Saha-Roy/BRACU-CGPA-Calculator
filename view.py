import tkinter as tk
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk


class View(tk.Tk):

    def __init__(self, controller):
        super().__init__()

        labelFont = Font(family="Arial", size="12")
        buttonFont = Font(family="Arial", size="10")

        self.controller = controller
        self.title("CGPA Calculator")
        self.geometry('600x800+0+0')
        self.wm_iconbitmap('C:/Users/Rajib Saha/PycharmProjects/mewpro/CGPA.ico')

        ###### BG IMAGE #########
        self.bg = ImageTk.PhotoImage(file="C:/Users/Rajib Saha/PycharmProjects/mewpro/grad.jpg")
        self.bg_image = Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_1 = Frame(self, bg="lightblue")
        self.frame_1.pack()

        self.lbl_1 = Label(self.frame_1, text="Previous CGPA :", bg="lightblue", font=labelFont)
        self.lbl_1.grid(row=0, column=0)
        self.entry_1 = Entry(self.frame_1)
        self.entry_1.grid(row=0, column=1)

        self.lbl_2 = Label(self.frame_1, text="Previous Earned Credits :", bg="lightblue", font=labelFont)
        self.lbl_2.grid(row=1, column=0)
        self.entry_2 = Entry(self.frame_1)
        self.entry_2.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_3 = Label(self.frame_1, text="Number of Courses to add :", bg="lightblue", font=labelFont)
        self.lbl_3.grid(row=2, column=0)
        self.entry_3 = Entry(self.frame_1)
        self.entry_3.grid(row=2, column=1)

        self.btn_1 = Button(self, text="Add Credits & Grades ",
                            command=controller.add_courses, bg="gray70", font=buttonFont)
        self.btn_1.pack(pady=5)

        self.frame_2 = Frame(self, bg="lightblue")
        self.frame_2.pack()

    def main(self):
        self.mainloop()
