import tkinter
from tkinter import *


import webpage_generator_main as genM #imports main file
from webpage_generator_main import *


class ParentWindow(Frame): #tkinter frame class inherited by user defined class
    def __init__(self, master, *args, **kwargs): 
        Frame.__init__(self, master,*args, **kwargs)
        #master frame configuration
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry("{}x{}".format(700,400))
        self.master.title("Webpage Generator")
        self.master.config(bg="lightgray")

        self.lblTxt = 'Enter a message to post on your webpage below: '
        
        #label with instructions for the user
        self.lblInfo = Label(self.master,text= self.lblTxt, font= ('Helvetica,24,bold'), fg='black', bg='lightgray')
        self.lblInfo.grid(row=0 ,column=0, padx=(30,0), pady=(70,0))
        #allows the user to input text
        self.txtMsg = Entry(self.master,text='', font= ('Helvetica,24'), fg='black', bg='white',width=40)
        self.txtMsg.grid(row=1 ,column=0, padx=(30,0), pady=(30,0), sticky=NW )
        #button to submit user input
        self.btnSubmit = Button(self.master, text = 'Create New Webpage!', width=20, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=0, padx=(30,0), pady=(30,0), sticky=SW )
        #button to close the frame
        self.btnClose = Button(self.master, text = 'Close Generator', width=20, height=2, command=self.close)
        self.btnClose.grid(row=2, column=0, padx=(30,0), pady=(30,0), sticky=SE )



    def submit(self): #Generates a web page that sets the user’s input as the body text for the web page
        text = self.txtMsg.get() #gets user input
        newTxt = "<html><body><h1>"+ text +"</h1></body></html>"
        genM.newWebpage(newTxt) #initiate the web page generation process with user input


    def close(self):
        self.master.destroy()
    
    


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
