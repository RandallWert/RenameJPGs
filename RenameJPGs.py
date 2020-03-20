from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from PIL import Image
import os

def getPath(filename):
    for i in range(len(filename)-1,0,-1):
        if filename[i:i+1] == "/":
            return filename[0:i+1]

keepGoing = True

while keepGoing:
       
    root = Tk()
    root.update()
    filenameList = filedialog.askopenfilename(multiple=True)
    root.destroy()

    for filename in filenameList:
        im = Image.open(filename)
        exifData = im._getexif()

        try:
            for tag, value in exifData.items():
                if tag == 0x0132:
                    path = getPath(filename)
                    year = value[0:4]
                    month = value[5:7]
                    day = value[8:10]
                    hours = value[11:13]
                    minutes = value[14:16]
                    seconds = value[17:19]
                    newFilename = path + year + month + day + hours + minutes + seconds + ".jpg"
                    os.rename(filename, newFilename)
                    break

        except:
            messagebox.showerror(message='Error occured; possibly because no EXIF data exists.',title='Error')

    keepGoing = messagebox.askyesno(message='Select more jpg files to rename?',icon='question',title='More JPEGs?')

