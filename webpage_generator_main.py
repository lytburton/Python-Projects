#import the webbrowser module
import webbrowser

import webpage_generator_gui as genG




'''def getTxt():
    newMsg = genG.get(text())
    newTxt = newTxt.append(newMsg)
    newWebpage()'''
    
 
#this function writes an html file and opens it in a new webpage
def newWebpage(newTxt):
        #selected text
        
        #saleTxt = "<html><body><h1>"+ genG.textApnd +"</h1></body></html>"
    
        #creates an html file and writes the selected text above to it
        with open("sale.html","w") as file:
            file.write(newTxt)
            #opens the html file in a web browser
            webbrowser.open('sale.html')

#def newTxt():
    #genG.txtMsg.get()


if __name__ == "__main__":
    pass
