#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      20053478
#
# Created:     07-03-2018
# Copyright:   (c) 20053478 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''step==1==
#-------------------------------------------------------------------------------

import tkinter module and create a base window



from tkinter import *
window = Tk()
window.title("Gui for Docx2txt")
window.mainloop()


'''

import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import docx2txtv3

window = Tk()
window.geometry("500x200")
window.title("Gui for Docx2txt")


sw_lbl = Label(window, text="Convert documents(.docx) to text (.txt) using Docx2txt", font=("Arial", 12))
sw_lbl.grid(column=0, row=0, columnspan=3)

label_docx_path = Label(window, text="Source docx dir: ", font=("Arial", 12))
label_docx_path.grid(column=0, row=1)

source_path_txt_var = tk.StringVar()
source_path_txt = tk.Entry(window,width=50)
source_path_txt.grid(column=1, row=1)

label_txt_path = Label(window, text="Dest. to save txt: ", font=("Arial", 12))
label_txt_path.grid(column=0, row=2)

dest_path_txt_var = tk.StringVar()
dest_path_txt = tk.Entry(window,width=50)
dest_path_txt.grid(column=1, row=2)



def clicked_browse_source():
    dir=filedialog.askdirectory()
    source_path_txt.delete(0,END)
    source_path_txt.insert(0,dir)
    return

#Clicked browsed destination folder button
def clicked_browse_dest():
    dir=filedialog.askdirectory()
    dest_path_txt.delete(0,END)
    dest_path_txt.insert(0,dir)
    return


btn_browse_source = Button(window, text="...docx dir",bg="gray", fg="blue", command=clicked_browse_source)
btn_browse_source.grid(column=2, row=1)

btn_browse_dest = Button(window, text="...docx dir",bg="gray", fg="blue", command=clicked_browse_dest)
btn_browse_dest.grid(column=2, row=2)


mgs_txt = Label(window, text="Welcome! Choose source & destination paths.", font=("Arial", 12))
mgs_txt.grid(column=0, row=5, columnspan=3)


def clicked_btn_convert():
    if os.path.isdir(source_path_txt.get()):
        mgs_txt.configure(text="Source path for docx: OK!")
    else:
        mgs_txt.configure(text="Error! Source docx path is invalid.")

    if os.path.isdir(dest_path_txt.get()):
        mgs_txt.configure(text="Dest. path for txt: OK!")
    else:
        mgs_txt.configure(text="Error! Destination txt path is invalid.")



    # Write code to check the source docx path validity
    #res = "Welcome to " + source_path_txt.get()
    #label_docx_path.configure(text= res)

btn_convert = Button(window, text="Convert docx to text",bg="orange", fg="blue",command=clicked_btn_convert)
btn_convert.grid(column=1, row=4)


window.mainloop()



def main():
    pass

if __name__ == '__main__':
    main()
