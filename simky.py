#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      20053478
#
# Created:     08-03-2018
# Copyright:   (c) 20053478 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import pyautogui
import time
import winsound


f1=r"C:\Users\20053478\Desktop\Source.txt"

dirx=r"C:\Users\20053478\Desktop\dirs"

time.sleep(10)
for filename in os.listdir(dirx):
    with open(filename,'r') as fx:
        for line in fx:
            pyautogui.typewrite(line, interval=0.01)

    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)


''''
    for filename in os.listdir(source_path_txt.get()):
                document = Document(os.path.join(source_path_txt.get(), filename))
                print(filename)
                savetxt = os.path.join(dest_path_txt.get(), ntpath.basename(filename).split('.')[0] + ".txt")
                print('Reading ' + filename)
                # print(savetxt)
                fullText = []
                for para in document.paragraphs:
                    # print(para.text)
                    fullText.append(para.text)
                    with open(savetxt, 'w', encoding='utf-8') as newfile:
                        for item in fullText:
                            newfile.write("%s\n" % item)
            mgs_txt.configure(text="Convertion done!")
while True:
    time.sleep(10) # sleep 10 before starting first and next type work
    pyautogui.typewrite('Hello world!', interval=0.01)

'''


def main():
    pass

if __name__ == '__main__':
    main()
