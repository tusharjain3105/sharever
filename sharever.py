from tkinter import *
from tkinter import filedialog
import qrcode
import os
import threading
from PIL import Image, ImageTk
import ntpath
import os
import shutil

ipconfig = os.popen("ipconfig").read()
i = ipconfig.find('192')
ip = ipconfig[i:i+14].strip()
file = False
def createServer():
    os.system('python -m http.server')

def startServer():
    if(path.get()!=''):
        if(file):
            url.config(text=f"http://{ip}:8000/{file}")
        else:
            url.config(text=f"http://{ip}:8000/")
        img.pack()
        url.pack()
        threading.Thread(target=createServer).start()


def shareFile():
    if(file):
        img.pack()
        print(path)
        url.config(text=f"http://{ip}:8000/")
        url.pack()
        threading.Thread(target=createServer).start()


qr = qrcode.make(f"http://{ip}:8000/")
qr.save("qr.png")
qr = Image.open("qr.png").resize((250, 250), Image.ANTIALIAS)


def folderDialog():
    path.delete(0, END)
    dir = filedialog.askdirectory(
        initialdir=os.getcwd(), title="Select A Folder")
    path.insert(0, dir)
    os.chdir(dir)


def fileDialog():
    global file
    path.delete(0, END)
    file = filedialog.askopenfile(
        initialdir='', title="Select A Folder").name
    path.insert(0, file)
    dir = os.path.dirname(file)
    os.chdir(dir)
    file = ntpath.basename(file)
    qr = qrcode.make(f"http://{ip}:8000/{file}")
    qr.save("qr.png")
    qr = Image.open("qr.png").resize((250, 250), Image.ANTIALIAS)
    qr = ImageTk.PhotoImage(qr)
    img.config(image=qr)
    img.photo_ref = qr

def recieveThread():
    os.system('python manage.py runserver 0.0.0.0:8000')

def recieve():
    img.pack()
    url.config(text=f"http://{ip}:8000/")
    url.pack()
    threading.Thread(target=recieveThread).start()

def refer():
    qr = qrcode.make(f"http://{ip}:8000/sharever.zip")
    qr.save("qr.png")
    qr = Image.open("qr.png").resize((250, 250), Image.ANTIALIAS)
    qr = ImageTk.PhotoImage(qr)
    img.config(image=qr)
    img.photo_ref = qr
    img.pack()
    url.config(text=f"http://{ip}:8000/sharever.zip")
    url.pack()
    threading.Thread(target=createServer).start()

if __name__ == "__main__":
    tk = Tk()
    tk.iconphoto(False, PhotoImage(file="logo-short.png"))
    tk.config(bd=5)
    tk.title("Sharever By CODEVER")
    tk.resizable(0, 0)
    tk.grid_rowconfigure(0, weight=1)
    tk.grid_columnconfigure(0, weight=1)
    tk.grid_columnconfigure(1, weight=1)
    tk.geometry('500x520')
    path = Entry(tk, bd=3, width=60)
    path.insert(0, '')
    path.pack()
    browseDir = Button(tk, text='Browse Directory', command=folderDialog)
    browseDir.pack(ipadx=10)
    browseFile = Button(tk, text='Browse File', command=fileDialog)
    browseFile.pack(ipadx=10)
    startDir = Button(tk, text='Share', command=startServer)
    startDir.pack(ipadx=10)
    startRecieve = Button(tk, text='Recieve', command=recieve)
    startRecieve.pack(ipadx=10)
    refer = Button(tk, text='Send Sharever', command=refer)
    refer.pack(ipadx=10)
    qr = ImageTk.PhotoImage(qr)
    img = Label(tk, image=qr)
    url = Label(tk,text='Hello')
    tk.mainloop()






