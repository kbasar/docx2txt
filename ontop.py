#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      20053478
#
# Created:     09-03-2018
# Copyright:   (c) 20053478 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
import time

time.sleep(10)

root = Tk()
root.title("app")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("550x250+%d+%d" % (screen_width/2-275, screen_height/2-125))
root.configure(background='gold')
root.lift()

#Use this code to put tkinter gui ontop of every windows.
root.attributes('-topmost', True)
#use following code to allow other windows to be on top
root.update()
root.attributes('-topmost', False)

mainloop()

def main():
    pass

if __name__ == '__main__':
    main()
