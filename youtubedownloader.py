from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("700x500")
root.resizable(0, 0)
root.title("YouTube Video Downloader")

link = StringVar()
Label(root, text="Paste Link: ", font="arial 18 italic").place(x=160, y=60)
link_enter = Entry(root, width=120, textvariable=link).place(x=40, y=90)


def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download("C:\\Users\\fatih\\Desktop\\Python")
    Label(root, text="Downloaded", font="arial 16 italic").place(x=250, y=175)


Button(root, text="download", font="arial 15 italic",
       bg="pale violet red", padx=2, command=Downloader).place(x=300, y=350)
root.mainloop()
