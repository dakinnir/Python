'''
Graphical User Interface Guessing Game between the number of 1 to 100
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
        self.lbl = Label(self, text="Welcome!", font='Courier 20')
        self.lbl.grid(row=0, columnspan=4,padx = 60)
        self.lbl2 = Label(self, text="Input a number:")
        self.lbl2.grid(row=3,column=3)
        self.entry = Entry(self) #create entry box that user will input a guess
        self.entry.bind('<KeyPress>', self.enter_return)
        self.entry.grid(row=1, column=3, padx = 30)
        self.bttn_check = Button(self, text="Check", command=self.check_guess)
        self.bttn_check.grid(row=4, column=3)
        self.lbl3 = Label(self)
        self.lbl3.grid(row=6, column=3)
    def clear_text(self):
        self.entry.delete(0, 'end')

    def check_guess(self): #check if the input number is equal to the secret number
        #try/except to text for users input error
        try:
            guess = int(self.entry.get())  #assigning the output message
            #checking the number if greater than secret number
            if guess > Application.secret_number:
                self.lbl3['text'] = "The number you have guessed is higher. Try again"
            elif guess < Application.secret_number:
                self.lbl3["text"] = "The number you have guessed is lower. Try again."
            else:
                self.lbl3["text"] = "You guessed it right."
                messagebox.showinfo("Congratulations", "You're correct!")
                self.lbl3["text"] = "Continue guessing."
                self.lbl3['color'] #Tell user to keep going
                #clear the entry box
                self.clear_text()
        except:
            self.lbl3["text"] = "Invalid Value"

    def enter_return(self, event): #bind the key enter with the function check_guess
        if event.keysym == "Enter":
            #check if the guess input is correct
            self.check_guess()
        if event.keysym == "Return":
            self.check_guess()


# main
root = Tk()
root.title("Guessing Game")
# image = PhotoImage(file="guess.jpg")
root.maxsize(900, 600)
root.geometry("450x200")
root.resizable(width=TRUE, height=TRUE)
app = Application(root)
root.mainloop()
