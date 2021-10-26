import shutil
import os
from os import path

import tkinter
from tkinter import *
import tkinter.filedialog

import datetime
from datetime import *

#gets the source folder path
def getPathSelect():
    dir_selected = tkinter.filedialog.askdirectory()
    dir_path = StringVar()
    dir_path.set(dir_selected)
    myDirSelect = dir_path.get()
    lblDisplay1.config(text='{}/'.format(myDirSelect))
    print('Folder selected!',myDirSelect)

#gets the destination folder path
def getPathReceive():
    dir_selected = tkinter.filedialog.askdirectory()
    dir_path = StringVar()
    dir_path.set(dir_selected)
    myDirReceive = dir_path.get()
    lblDisplay2.config(text='{}/'.format(myDirReceive))
    print('Folder received!',myDirReceive)

#closes the program
def close():
        tk.destroy()

#transfers files from source folder to destination folder
def move_files():
  
    source = lblDisplay1.cget('text')
    destination = lblDisplay2.cget('text')
    src_path = os.path.abspath(source)
    dest_path = os.path.abspath(destination)
    myfiles = os.listdir(src_path)
    
    #current time
    time_now = datetime.now()
    print('The current time is: \n', time_now)

    #current time minus one day
    one_day_ago = time_now + timedelta(days = -1)
    print('\nExactly a day ago the time was: \n', one_day_ago)
    #check to see if the folder is empty
    if len(myfiles) == 0:
        print('\nThis folder is empty!')

    else:

        #get the list of files in source folder and get the time each was last modified
        for i in myfiles:
            
            #set the file path
            srcFinal = '{}/{}'.format(src_path,i)
            file_path = os.path.abspath(srcFinal)
            
            #time file was last modified
            lastModified = os.path.getmtime(file_path)
            print('\n{} was last modified on: \n'.format(i),lastModified)
            
            #time file was last modified converted to datetime
            lastModDate = datetime.fromtimestamp(lastModified)
            print('\nHere is the modification converted to a datetime format: \n',lastModDate)
            
            #compare time file modified to time_now and one_day_ago
            if lastModDate >= one_day_ago and lastModDate <= time_now:
                
                #if modified time is between these values move to destination folder
                shutil.copy(srcFinal, dest_path)
                os.remove(srcFinal)
                lblDisplay3.config(text='Your files were moved successfully!')
                print('{} was moved successfully!'.format(i))
            else:
                lblDisplay3.config(text='Oops! Something went wrong. Please try again.')



#provide a user interface using tkinter
tk = Tk()


tk.resizable(width=False, height=False)
tk.geometry("{}x{}".format(600,600))
tk.title("File Transfer Program")
tk.config(bg="lightgray")

#instructions for the user for use in label format
selectMsg='Step 1: Click the button below to select the folder you wish to transfer files from: '
receiveMsg='Step 2 : Click the button below to select the folder you wish to transfer files to: '
fileChkMsg='Step 3: Click the button below to send your selected files to the destination folder: '

#introductory header
lblHeading = Label(tk,text='Welcome to the File Transfer Program!', font= ('Helvetica,16'), fg='white', bg='black')
lblHeading.grid(row=0 ,column= 0, padx=(0,0), pady=(30,0))

#label for selecting source folder        
lblSelect = Label(tk,text=selectMsg, font= ('Helvetica,16'), fg='black', bg='white')
lblSelect.grid(row=1 ,column= 0, padx=(20,0), pady=(30,0))

#label for showing selected source folder
lblDisplay1 = Label(tk,text='', font= ('Helvetica,16'), fg='black', bg='lightgray')
lblDisplay1.grid(row=2 ,column= 0, padx=(0,0), pady=(10,0))

#label for showing selected destination folder
lblDisplay2 = Label(tk,text='', font= ('Helvetica,16'), fg='black', bg='lightgray')
lblDisplay2.grid(row=5 ,column= 0, padx=(0,0), pady=(10,0))

#label for showing reporting success
lblDisplay3 = Label(tk,text='', font= ('Helvetica,16'), fg='black', bg='lightgray')
lblDisplay3.grid(row=8 ,column= 0, padx=(0,0), pady=(10,0))

#label for selecting destination folder
lblReceive = Label(tk,text=receiveMsg, font= ('Helvetica,16'), fg='black', bg='white')
lblReceive.grid(row=4 ,column= 0, padx=(20,0), pady=(30,0))

#label for sending files modified files from source to destination folders
lblFileChk = Label(tk,text=fileChkMsg, font= ('Helvetica,16'), fg='black', bg='white')
lblFileChk.grid(row=7 ,column= 0, padx=(20,0), pady=(30,0))

#button allows the user to browse and select a source folder
btnSelect = Button(tk, text = 'Browse...', width=20, height=2, fg='white', bg='black',command= getPathSelect)
btnSelect.grid(row=3, column=0, padx=(0,0), pady=(10,0))

#button allows the user to browse and select a destination folder
btnReceive = Button(tk, text = 'Browse...', width=20, height=2, fg='white', bg='black',command=getPathReceive)
btnReceive.grid(row=6, column=0, padx=(0,0), pady=(10,0))

#Manual file check button 
btnFileChk = Button(tk, text = 'Send Files', width=20, height=2, fg='white', bg='darkred', command=move_files)
btnFileChk.grid(row=9, column=0, padx=(0,0), pady=(10,0))

#Allows user to close the window
btnClose = Button(tk, text = 'Close Program', width=20, height=2, fg='white', bg='black', command=close)
btnClose.grid(row=10, column=0, padx=(0,0), pady=(10,0))



if __name__ == "__main__":
    tk.mainloop()

