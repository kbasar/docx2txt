#-------------------------------------------------------------------------------
# Name:        gui_typex
# Purpose:provide user interface for Text to voice announce with text to typing program
#
# Author:      Khairul Basar
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
# import docx2txtv3
from docx import Document
import ntpath
import shutil

#=======for text to type & text to voice
import pyautogui
import time
import winsound
import pyttsx3

window = Tk()
window.geometry("520x200")
window.title("Gui for Typex")

cwd = os.getcwd()

sw_lbl = Label(window, text="Use Typex to type text files in your text field", font=("Arial", 12))
sw_lbl.grid(column=0, row=0, columnspan=3)

label_docx_path = Label(window, text="Textfile dir: ", font=("Arial", 12))
label_docx_path.grid(column=0, row=1, sticky="W")

source_path_txt_var = tk.StringVar()
source_path_txt = tk.Entry(window, width=50)
source_path_txt.grid(column=1, row=1, sticky="W")
source_path_txt.insert(END, cwd)
label_txt_path = Label(window, text="Delay time(s): ", font=("Arial", 12))
label_txt_path.grid(column=0, row=2, sticky="W")

# delay for typing
dest_path_txt_var = tk.StringVar()
dest_path_txt = tk.Entry(window, width=10)
dest_path_txt.grid(column=1, row=2, sticky="W")
dest_path_txt.insert(END, 45)


# rate of typing Label
rate_label_txt = Label(window, text="Rate of type: ", font=("Arial", 12))
rate_label_txt.grid(column=1, row=2, sticky="N")

# rate of typing
rate_type_txt_var = tk.StringVar()
rate_type_txt = tk.Entry(window, width=10)
rate_type_txt.grid(column=1, row=2, sticky="E")
rate_type_txt.insert(END, 0.01)


def clicked_browse_source():
    dir = filedialog.askdirectory()
    source_path_txt.delete(0, END)
    source_path_txt.insert(0, dir)
    return

# Clicked browsed destination folder button


'''
def clicked_browse_dest():
	dir = filedialog.askdirectory()
	dest_path_txt.delete(0, END)
	dest_path_txt.insert(0, dir)
	return
'''


def say(s):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate)
    voices = engine.getProperty('voices')
    # for voice in voices:
    engine.setProperty('voice', 'english-us')
    # print voice.id
    engine.say(s)
    a = engine.runAndWait()  # blocks


def typex(dir, delaytime, interval):
    for filename in os.listdir(dir):
        fx = os.path.abspath(filename)
        #configure(text='Starting to type file  ' + filename)
        say('Starting to type file  ' + filename)
        say('filename: ' + filename)
        say('I repeat, filename: ' + filename)
        say('Waiting  ' + str(round(delaytime, 2)) + 'seconds before starting')
        # print(fx)
        d1 = delaytime / 3.0  # 1/3rd div of whole wait time
        # 2xd1=2/3rd of whole time, 3xd1=whole time
        time.sleep(d1)
        #mgs_txt.configure(text='Waiting  ' + str(round(2 * d1, 2)) + 'seconds before starting')
        say('Waiting  ' + str(round(2 * d1, 2)) + 'seconds before starting')
        time.sleep(d1)
        say('Waiting  ' + str(round(d1, 2)) + 'seconds before starting')
        time.sleep(d1)
        with open(dir + "\\" + filename, "r") as fxo:
            # print(fxo.read())
            for line in fxo:
                pyautogui.typewrite(line, interval)

        mgs_txt.configure(text='Finished typing file:  ' + filename)
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        say('Finished typing file:  ' + filename)
        say("Waiting to for" + str(delaytime / 2.0) + 'seconds')
        time.sleep(delaytime / 2.0)


btn_browse_source = Button(window, text="...file dir", bg="gray", fg="yellow", command=clicked_browse_source)
btn_browse_source.grid(column=2, row=1, sticky="W")

'''
btn_browse_dest = Button(window, text="...text dir", bg="gray", fg="blue", command=clicked_browse_dest)
btn_browse_dest.grid(column=2, row=2)
'''

mgs_txt = Label(window, text="Welcome! Typex is used to type existing text" + "\n" + " from a text file into active text field", font=("Arial", 12))
mgs_txt.grid(column=0, row=5, columnspan=3, sticky="N")


def clicked_btn_convert():
    oks = 0
    okd = 0
    rate = 0
    if os.path.isdir(source_path_txt.get()):
        mgs_txt.configure(text="Source path for docx: OK!")
        oks = 1
    else:
        mgs_txt.configure(text="Error! Source text path is invalid.")

    if oks == 1:
        try:
            delay = float(dest_path_txt.get())
            # rate or interval between typing two chars
            rate = float(rate_type_txt.get())
            mgs_txt.configure(text="Program started...")
            if top_is_checked.get():
                window.attributes('-topmost', True)
            else:
                window.attributes('-topmost', True)
                window.update()
                window.attributes('-topmost', False)

            oks = 2
        except:
            mgs_txt.configure(text="Error: Invalid time delay!")
            oks = 0

    if oks == 2:
        typex(os.path.abspath(source_path_txt.get()), delay, rate)


btn_convert = Button(window, text="Click to start", bg="orange", fg="blue", command=clicked_btn_convert)
btn_convert.grid(column=1, row=4)

top_is_checked = IntVar()
check = Checkbutton(window, text="Always on top", onvalue=1, offvalue=0, variable=top_is_checked)
check.grid(column=0,row=4, sticky='W')


btn_exit = Button(window, text="Exit", bg="light gray", fg="blue", width=10, command=window.destroy)
btn_exit.grid(column=2, row=6, sticky='W')



def main():
    window.mainloop()


if __name__ == '__main__':
    main()
