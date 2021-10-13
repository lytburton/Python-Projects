
"""db_assign.py: This script creates a database and adds new data into that database \
    using Python 3 and sqlite3"""



__author__ = "Lyttia Burton"
__version__ = 1.0


import sqlite3
#create a database table with 2 fields: an auto-increment primary int and a str field
conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )")
    conn.commit()
conn.close()



fileList = ('information.docx','Hello.txt', 'myImage.png','myMovie.mpg', 'World.txt','data.pdf','myPhoto.jpg')

#script will read from var fileList and determine the files which end with '.txt'
def findFiles():
    conn = sqlite3.connect('test2.db')
    
    for file in fileList:
        if file.endswith('.txt'): #add fileList files that end with '.txt' to database
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files(col_filename) VALUES(?)",(file,))
                #print qualifying text files to the console
                print(file)








if __name__ == "__main__":
    findFiles()
