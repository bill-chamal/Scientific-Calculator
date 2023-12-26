from tkinter import *
import math
#import parser
import tkinter.messagebox
import webbrowser

root = Tk()
root.title("Scientific Calculator")
root.configure(background="light grey")
root.geometry("565x695+0+0")
#root.resizable(width=False, height=False)
#root.iconbitmap('Calculator_ICO.ico')

calc = Frame(root)
calc.grid()


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        try:
            self.result = True
            self.current = float(self.current)
            if self.check_sum == True:
                self.valid_fuction()
            else:
                self.total = float(txtDisplay.get())
        except:
            tkinter.messagebox.showerror("Error", "Syntax ERROR")
            return

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_fuction(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_fuction()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def ClearEntry(self):
        self.result = False
        self.current = ""
        self.display(0)
        self.input_value = True

    def allClearEntry(self):
        self.ClearEntry()
        self.total = 0

    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def axp1(self):
        self.result = False
        self.current = math.exp1(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)


added_value = Calc()
# ==============Viewport=================#
txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")  # ==width=28==#
# =========================================!Buttons======================================#
bgnam = "White"
fgnam = "Black"
numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(
            Button(calc, width=6, height=2, font=('arial', 20, 'bold'), bg=bgnam, fg=fgnam, bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1
# ========================================BASIC=========================================#

btnClear = Button(calc, text=chr(67), width=13, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                  command=added_value.ClearEntry).grid(row=1, column=1, columnspan=2, pady=1)

btnAllClear = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                     command=added_value.allClearEntry).grid(row=1, column=0, pady=1)

# btnDel = Button(calc, text="<-", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey"
#                   ).grid(row=1, column=2, pady=1)

btnΑdd = Button(calc, text="+", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                command=lambda: added_value.operation("add")).grid(row=4, column=3, pady=1)

btnSubstract = Button(calc, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                      command=lambda: added_value.operation("sub")).grid(row=3, column=3, pady=1)

btnMultiply = Button(calc, text="*", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                     command=lambda: added_value.operation("multi")).grid(row=2, column=3, pady=1)

btnDivide = Button(calc, text=chr(247), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                   command=lambda: added_value.operation("divide")).grid(row=1, column=3, pady=1)

btnZero = Button(calc, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg=bgnam
                 , command=lambda: added_value.numberEnter(0)).grid(row=5, column=1, pady=1)

btnDot = Button(calc, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                command=lambda: added_value.numberEnter(".")).grid(row=5, column=2, pady=1)

btnPm = Button(calc, text=chr(177), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
               command=added_value.mathsPM).grid(row=5, column=0, pady=1)

btnEquals = Button(calc, text="=", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                   command=added_value.sum_of_total).grid(row=5, column=3, pady=1)

# ==========================================Scientific===================================#
# ========row=0=======#
btnSq = Button(calc, text="√", width=13, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
               command=added_value.squared).grid(row=0, column=4, columnspan=2, pady=1)
btnsurrounded = Button(calc, text="(", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                       command=lambda: added_value.numberEnter("(")).grid(row=0, column=6, pady=1)
btnsorroun = Button(calc, text=")", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                    command=lambda: added_value.numberEnter(")")).grid(row=0, column=7, pady=1)
# ========row=1=======#
btnPi = Button(calc, text="π", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
               command=added_value.pi).grid(row=1, column=4, pady=1)
btncos = Button(calc, text="cos", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                command=added_value.cos).grid(row=1, column=5, pady=1)
btntan = Button(calc, text="tan", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                command=added_value.tan).grid(row=1, column=6, pady=1)
btnSin = Button(calc, text="sin", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                command=added_value.sin).grid(row=1, column=7, pady=1)
# ========row=2=======#
btnN = Button(calc, text="n!", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
              ).grid(row=2, column=4, pady=1)
btnCosh = Button(calc, text="cosh", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                 command=added_value.cosh).grid(row=2, column=5, pady=1)
btntanh = Button(calc, text="tanh", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                 command=added_value.tanh).grid(row=2, column=6, pady=1)
btnsinh = Button(calc, text="sinh", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                 command=added_value.sinh).grid(row=2, column=7, pady=1)
# ========row=3=======#
btnLog = Button(calc, text="Ln", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                command=added_value.log).grid(row=3, column=4, pady=1)
btnExp = Button(calc, text="Exp", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                command=added_value.exp).grid(row=3, column=5, pady=1)
btnEqualsMod = Button(calc, text="Mod", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                      command=lambda: added_value.operation("mod")).grid(row=3, column=6, pady=1)
btnE = Button(calc, text="e", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
              command=added_value.e).grid(row=3, column=7, pady=1)
# ========row=4=======#
btnLog2 = Button(calc, text="Log2", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                 command=added_value.log2).grid(row=4, column=4, pady=1)
btndeg = Button(calc, text="deg", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                command=added_value.degrees).grid(row=4, column=5, pady=1)
btnacosh = Button(calc, text="scosh", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  command=added_value.acosh).grid(row=4, column=6, pady=1)
btnasinh = Button(calc, text="asinh", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  command=added_value.sinh).grid(row=4, column=7, pady=1)
# ========row=5=======#
btnlog10 = Button(calc, text="log10", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                  command=added_value.log10).grid(row=5, column=4, pady=1)
btnlog1p = Button(calc, text="log1p", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                  command=added_value.log1p).grid(row=5, column=5, pady=1)
btnexpm1 = Button(calc, text="expm1", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                  command=added_value.exp).grid(row=5, column=6, pady=1)
btnlgamma = Button(calc, text="lgamma", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="light grey",
                   command=added_value.lgamma).grid(row=5, column=7, pady=1)


# ===============Menu_Bar=================#
# ==============Defenitions===============#
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Are you sure you want to exit?")
    if iExit > 0:
        root.destroy()
        return


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("565x670+0+0")


def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("1110x670+0+0")


def About():
    About = tkinter.messagebox.showinfo("About Scientific Calculator", "Created by Bill Chamalidis 2019")


new = 2

url = "https://www.microsoft.com/en-us/Useterms/Retail/Windows/10/UseTerms_Retail_Windows_10_English.htm"
urlSendFedbck = "https://mail.google.com/mail/u/0/#search/basilischal17%40gmail.com?compose=new"


def ViewHlp():
    webbrowser.open(url, new=new)


def SdFbck():
    SdFbck = tkinter.messagebox.askyesno("Send FeedBack", "Do you want to open the browser?")
    if SdFbck > 0:
        tkinter.messagebox.showinfo("Send FeedBack", "To contact me, you must be connected to your Gmail address!")
        webbrowser.open(urlSendFedbck, new=new)
        return


menubar = Menu(calc)
# ==============File===============#
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Calculator", menu=filemenu)
filemenu.add_cascade(label="Standard", command=Standard)
filemenu.add_cascade(label="Scientific", command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)
# ==============Edit===============#
'''editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_cascade(label="Undo")
editmenu.add_cascade(label="Redo")
editmenu.add_separator()
editmenu.add_cascade(label="Cut")
editmenu.add_cascade(label="Copy")
editmenu.add_cascade(label="Paste")
editmenu.add_cascade(label="Delete")
editmenu.add_separator()
editmenu.add_command(label="Select All")'''
# =============Theme===============#
# thememenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Theme", menu=thememenu)
# thememenu.add_cascade(label="Light Theme", command = ThemeToggleWhite)
# thememenu.add_cascade(label="Dark Theme", command = ThemeToggleBlack)
# ==============Help===============#
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_cascade(label="View Help", command=ViewHlp)
helpmenu.add_cascade(label="Send FeedBack", command=SdFbck)
helpmenu.add_separator()
helpmenu.add_cascade(label="About Scientific Calculator", command=About)
# ----------------RUN------------------#
root.config(menu=menubar)
root.mainloop()
