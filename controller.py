from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
import decimal

from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

        self.titleFont = Font(family="Arial", size="18")
        self.labelFont = Font(family="Arial", size="12")
        self.buttonFont = Font(family="Arial", size="10")

    def main(self):
        self.view.main()

    def add_courses(self):
        if (self.view.entry_3.get() != '') & (self.view.entry_3.get().isdigit()):
            self.num_courses = int(self.view.entry_3.get())
            self.grades_list = []
            self.units_list = []
            self.frame_2 = ttk.Treeview(self.view.frame_2)
            self.cor_no = Label(self.view.frame_2,text="#No.",bg="skyblue",font=self.labelFont)
            self.cor_no.grid(row=0, column=0)
            self.lbl_units = Label(self.view.frame_2, text="Credits :", bg="skyblue",font=self.labelFont)
            self.lbl_units.grid(row=0, column=1)
            self.lbl_grades = Label(self.view.frame_2, text="Grades :", bg="skyblue", font=self.labelFont)
            self.lbl_grades.grid(row=0, column=2)
            #self.frame_2.grid()
            self.scrollbar = ttk.Scrollbar(self.view.frame_2, orient=VERTICAL, command= self.frame_2.yview)
            self.frame_2.config(yscroll=self.scrollbar.set)
            self.scrollbar.grid(rowspan=self.num_courses+1, column=3, sticky="ns")
            self.view.frame_2.bind("<Return>", lambda e: self.units_list)
            for i in range(0, self.num_courses):
                self.cor_label= Label(self.view.frame_2, text=str(i+1), font=self.labelFont)
                self.cor_label.grid(row=i+1, column=0, pady=0)
                self.units_list.append(Spinbox(self.view.frame_2, values=self.model.possible_credits()))
                self.units_list[i].grid(row=i + 1, column=1, padx=5, pady=5)
                self.grades_list.append(Spinbox(self.view.frame_2, values=self.model.possible_grades()))
                self.grades_list[i].grid(row=i + 1, column=2, padx=5, pady=5)
            self.btn_calcCG = Button(self.view, text="Calculate CGPA", command=self.calc_CG,font=self.buttonFont, bg="gray70")
            self.btn_calcCG.pack(pady=5)
            self.view.btn_1.config(state=DISABLED)
        else:
            messagebox.showerror("Error", "Enter a Valid Value")

    def calc_CG(self):
        if (self.view.entry_1.get() != '') & (self.view.entry_1.get().isdigit()):
            print("Calculating !")
            credits_this_sem = 0
            units_this_sem = 0
            for j in range(0, self.num_courses):
                credits_this_sem = credits_this_sem + float(self.units_list[j].get()) * (
                    self.model.coreesponding_point(self.grades_list[j].get()))
                units_this_sem = units_this_sem + float(self.units_list[j].get())
            final_cgpa = (credits_this_sem + float(self.view.entry_1.get()) * float(self.view.entry_2.get())) / (
                    units_this_sem + int(self.view.entry_2.get()))
            final_cgpa = round(final_cgpa, 4)
            messagebox.showinfo("Calculated CGPA ", "Your CGPA is " + str(final_cgpa))
        else:
            messagebox.showerror("Error", 'Please, enter \'0\' if previously no courses have been taken')


if __name__ == '__main__':
    cgpa = Controller()
    cgpa.main()
