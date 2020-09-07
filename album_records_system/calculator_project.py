'''
Graphical User Interface Calculator
'''


#importing necessary modules/packages
from tkinter import *

from tkinter import messagebox
import random

#Homework 9.20-9.21
class Application(Frame):
    secret_number = random.randint(1,101)  # setting the computer random number under the class so it doesn't reset everytime we call the check_guess function


    def __init__(self, master):
        #initializing methods
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    #our user Interface
    def create_widgets(self):
        #creating the label text
        label1 = Label(root, text="Calculator").grid(row=0, column=6, columnspan=6) #grid your objects properly
        operationLabel = Label(root, text="Operation").grid(row=8, rowspan=2, column=5) #grid your objects properly
        addButton = Button(root, text="Addition (+)").grid(row=7, column=7)
        subtractButton = Button(root, text="Subtraction (-)").grid(row=8,column=7)
        multiplyButton = Button(root, text="Multiply (*)", command=self.multiply).grid(row=9,column=7)
        divideButton = Button(root, text="Division (/)").grid(row=10, column=7)

        first_number = StringVar()
        label2 = Label(root, text="First Number").grid(row=3, column=5)
        entry1 = Entry(root, textvariable=first_number).grid(row=3, column=7, columnspan=7)

        second_number = StringVar()
        label3 = Label(root, text="Second Number").grid(row=4, column=5)
        entry2 = Entry(root, textvariable=second_number).grid(row=4, column=7, columnspan=7)

        # output Value
        lbl3 = Label(root).grid(row=9, column=3)

    def clear_text(self):
        self.entry.delete(0, 'end')
    def numberValid(self):
        return first_number.isdigit() or second_number.isdigit()



    def multiply(self): # mulplication function
        try:
            first = int(self.entry1.get())  # assigning the output message
            #checking the number if greater than secret number
            second = int(self.entry2.get())
            if first.isdigit() and second.isdigit():
                lbl3["text"] = "Successful"
                messagebox.showinfo(first*second)
        #     elif guess < Application.secret_number:
        #         lbl3["text"] = "The number you have guessed is lower. Try again."
        #     else:
        #         lbl3["text"] = "You guessed it right."
        #         messagebox.showinfo("Congratulations", "You're correct!")
        #         lbl3["text"] = "Continue guessing."
        #         lbl3['color'] #Tell user to keep going
        #         #clear the entry box
        #         self.clear_text()
        # except:
        #     lbl3["text"] = "Invalid Value"

    def enter_return(self, event): #bind the key enter with the function check_guess
        if event.keysym == "Enter":
            #check if the guess input is correct
            self.check_guess()
        if event.keysym == "Return":
            self.check_guess()


# main
root = Tk()
root.title("Simple Calculator Project")
# image = PhotoImage(file="guess.jpg")
root.maxsize(900, 600)
root.geometry("500x250")
root.resizable(width=TRUE, height=TRUE)
app = Application(root)
root.mainloop()
