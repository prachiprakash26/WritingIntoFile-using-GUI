#############################################################
#       Whatever you write here,                            #
#       will be written in one file created                 #
#       with name MyFile.txt in same location as this       #
#       pyhton script's                                     #
#############################################################
import tkinter
import time
from tkinter import *
import os
from tkinter import messagebox
tkinter.messagebox

#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("Write into Text File!! - MyFile.txt")
#set the size.
root.geometry("400x200")
# background color setting
root.configure(background='floral white')


#definition to exit
def exitThis():
    root.destroy()

        
#definition to write into file
def writeIntoFile():
    # Open a file
    textInput = user_input.get('1.0', END)
    if len(user_input.get("1.0", "end-1c")) != 0:
        file_open = open("MyFile.txt", "a")
        # Write into the file
        file_open.write(textInput)
        # Delete content in text
        user_input.delete('1.0', END)
        # Close opend file
        file_open.close()
    else:
        tkinter.messagebox.showinfo('Cannot Create/Append File','Enter something to SAVE File')
    

#definition to delete text file
def deleteFile():
    textFileName = "MyFile.txt"
    if textFileName in os.listdir():
        os.remove(textFileName)
        tkinter.messagebox.showinfo('Removed','Successfully Removed!'+textFileName)
    else:
        tkinter.messagebox.showinfo('Error!', 'File not found!: '+textFileName)


user_question = tkinter.Label(root, text="Enter your text here. Click save when finished. Check MyFile.txt", font=('Comic Sans MS', 10), bg='yellow', fg='blue')
user_question.pack()
#user_input = tkinter.Entry(root)
user_input = tkinter.Text(root, height=5, width=20)
user_input.config(highlightthickness='2')
user_input.pack(side="top", expand=True, padx=4, pady=4)
user_input.focus_set()

exitButton = Button(root, text="EXIT", command=exitThis, bg='Orange', fg='black')
exitButton.pack(side="left", expand=True, padx=4, pady=4)

saveButton = Button(root, text="SAVE", command=writeIntoFile, bg='Green', fg='white')
saveButton.pack(side="right", expand=True, padx=4, pady=4)

deleteButton = Button(root, text="Delete MyFile.txt!!", command=deleteFile, bg='Red', fg='white')
deleteButton.pack(side="right", expand=True, padx=4, pady=4)

#start the GUI
root.mainloop()


