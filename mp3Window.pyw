import tkinter as tk
import os
from tkinter import filedialog
from pygame  import mixer

def FindFileAndPlay():
    file = filedialog.askopenfilename()
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

def Pause():
    mixer.music.pause()

def UnPause():
    mixer.music.unpause()

Localpath = os.path.dirname(__file__)

janela = tk.Tk()
janela.iconbitmap(Localpath + "/files/mp3.ico")
bckg = "#6e6968"

janela.title("MP3 Player")
janela.configure(background=bckg)
#larguraXaltura+DistaciaEsquerda+DistanciaTopo
#100x100+50+50
janela.geometry("400x200")

ImagePlay = tk.PhotoImage(file=Localpath+"/files/play.png")
ImagePause = tk.PhotoImage(file=Localpath+"/files/pause.png")
ImageAdd = tk.PhotoImage(file=Localpath+"/files/plus.png")

txt1 = tk.Label(janela,text="Mp3 Player",background=bckg,font="Sans").place(x=130,y=-40,width=100,height=100)
Play= tk.Button(janela,image=ImageAdd,background=bckg,command=FindFileAndPlay,relief="flat",overrelief="flat",activebackground="#6e6968").place(x=160,y=20,width=50,height=50)
Pause = tk.Button(janela,image=ImagePause,background=bckg,command=Pause,relief="flat",overrelief="flat",activebackground="#6e6968").place(x=200,y=80,width=50,height=50)

UnPause = tk.Button(janela,image=ImagePlay,background=bckg,command=UnPause,relief="flat",overrelief="flat",activebackground="#6e6968").place(x=140,y=80,width=50,height=50)

janela.mainloop()


#a = filedialog.askopenfilename()
#By jão