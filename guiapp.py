from http.server import executable
import tkinter as tk
from tkinter import filedialog, Text
import os
from turtle import title 
def addApp():
    filename=filedialog.askopenfilename(initialdir="/",title="Select File"
    ,filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app,bg="white")
        label.pack()


root = tk.Tk()
apps=[]


canvas = tk.Canvas(root,height=700, width=700,bg="#263D42")
canvas.pack()

frame= tk.Frame(root,bg="white")
frame.place(relwidth =0.8, relheight=0.8,relx=0.1,rely=0.1)
openFile=tk.Button(root, text="Open file",padx=10,pady=5,fg="white",bg="#263D42",command=addApp)
openFile.pack()
runApps=tk.Button(root, text="Run Apps",padx=10,pady=5,fg="white",bg="#263D42")
runApps.pack()
root.mainloop()