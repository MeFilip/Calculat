from tkinter import *


class Calculator:

    def __init__(self):
        self.expression = ""
        self.gui()

    def gui(self):
        # create a window
        window = Tk()
        window.title('Calculator')
        window.geometry('358x388')
        window.resizable(0, 0)

        # create a display frame to show the expression
        self.expression_field = Entry(window, font=('arial', 20, 'bold'), bd=0, justify='right')
        self.expression_field.grid(row=0, column=0, columnspan=4, pady=10)
        self.expression_field.insert(0, '0')

        # create buttons
        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90,
                                                                                                              y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180,
                                                                                                              y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show('1')).place(x=0,
                                                                                                              y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show('2')).place(x=90,
                                                                                                              y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show('3')).place(x=180,
                                                                                                              y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show('4')).place(x=0,
                                                                                                              y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show('5')).place(x=90,
                                                                                                              y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show('6')).place(x=180,
                                                                                                              y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show('7')).place(x=0,
                                                                                                              y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show('8')).place(x=180,
                                                                                                              y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show('9')).place(x=90,
                                                                                                              y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show('0')).place(x=90,
                                                                                                              y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=180,
                                                                                                              y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270,
                                                                                                              y=350)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270,
                                                                                                              y=200)
        Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270,
                                                                                                              y=50)
        Button(width=11, height=4, text='x', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270,
                                                                                                              y=125)
        Button(width=11, height=4, text='=', relief='flat', bg='white', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', relief='flat', bg='white', command=self.clear).place(x=0, y=350)

        # run the main loop
        window.mainloop()

    def show(self, char):
        self.expression += str(char)
        self.expression_field.delete(0, END)
        self.expression_field.insert(0, self.expression)

    def clear(self):
        self.expression = ""
        self.expression_field.delete(0, END)
        self.expression_field.insert(0, "0")

    def solve(self):
        try:
            self.expression = str(eval(self.expression))
            self.expression_field.delete(0, END)
            self.expression_field.insert(0, self.expression)
        except:
            self.expression_field.delete(0, END)
            self.expression_field.insert(0, "Error")

