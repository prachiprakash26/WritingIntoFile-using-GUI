#############################################################
#       Whatever you write here,                            #
#       will be written in one file created                 #
#       with name of text file you provide                  #
#       in same location as this                            #
#       python script's                                     #
#                                                           #                
#       Amendments -                                        #
#       1. Added Styling                                    #
#       2. Added 'View All Text Files' Button               #
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
root.geometry("600x250")
# background color setting
root.configure(background='floral white')


#definition to exit
def exitThis():
    root.destroy()

        
#definition to write into file
def writeIntoFile():
    # Open a file
    textInput = user_input.get('1.0', END)
    filenameInput = user_text_file_name.get()
    filenameWithExt = filenameInput+".txt"
    if len(user_text_file_name.get()) != 0:
        if len(user_input.get("1.0", "end-1c")) != 0:
            file_open = open(filenameWithExt, "a")
            # Write into the file
            file_open.write(textInput)
            # Delete content in text
            user_input.delete('1.0', END)
            # Close opend file
            file_open.close()
        else:
            tkinter.messagebox.showinfo('Cannot Create/Append File','Enter something to SAVE File')
    else:
        tkinter.messagebox.showinfo('Cannot Create/Append File','File Name Cannot be empty')

    

#definition to delete text file
def deleteFile():
    #textFileName = "MyFile.txt"
    filenameInput = user_text_file_name.get()
    filenameWithExt = filenameInput+".txt"
    if filenameWithExt in os.listdir():
        os.remove(filenameWithExt)
        tkinter.messagebox.showinfo('Removed','Successfully Removed! : '+filenameWithExt)
    else:
        if len(user_text_file_name.get()) == 0:
            tkinter.messagebox.showinfo('Error!', 'Enter the file name you wish to delete! You can check "View All Text Files" to view the files')
        else:
            tkinter.messagebox.showinfo('Error!', filenameWithExt+' File not found in Directory '+ os.getcwd()+'!')
    user_text_file_name.delete(0,END)
   


#definition to find all text files
def viewTxtFiles():
    allTextFiles=""
    for file in os.listdir():
        if file.endswith(".txt"):
            allTextFiles += file+", "
    allTextFiles = allTextFiles[:-2]
    if len(allTextFiles) !=0:
        tkinter.messagebox.showinfo('All Text Files', "All text files present in Directory "+ os.getcwd() +" are :::: \n"+allTextFiles)
    else:
        tkinter.messagebox.showinfo('No Text File',"No .txt files present in Directory "+ os.getcwd()+" !")

user_ask_text_file_name = tkinter.Label(root, text="Enter the name of the file(without extension) which you want to create/append", font=('Comic Sans MS', 10), bg='yellow', fg='blue')
user_ask_text_file_name.pack()
user_text_file_name = tkinter.Entry(root)
user_text_file_name.pack()
user_text_file_name.focus_set()
user_question = tkinter.Label(root, text="Enter your text here. Click save when finished.", font=('Comic Sans MS', 10), bg='yellow', fg='blue')
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

deleteButton = Button(root, text="Delete Txt File", command=deleteFile, bg='Red', fg='white')
deleteButton.pack(side="right", expand=True, padx=4, pady=4)

ViewTxtFilesButton = Button(root, text="View All Text Files", command=viewTxtFiles, bg='blue', fg='white')
ViewTxtFilesButton.pack(side="right", expand=True, padx=4, pady=4)

print(os.getcwd())

#start the GUI
root.mainloop()


