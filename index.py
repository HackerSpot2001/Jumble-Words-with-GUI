from tkinter import *
from tkinter import ttk
import time
import random
from tkinter import messagebox

jumbled = [
    "LOPF",
    "PEHO",
    "IPTR",
    "OVLE",
    "FEEFOC",
    "TYPONH",
    "VAJA",
    "+C+",
    "#C",
    "XOCERD",
    "HVEEICA",
    "ENIENG",
    "SCRPITAVAJ",
    "YBUR",
    "NADAAC",
    "DIAIN",
    "HILDE",
    "DONONL",
    "ANICHA",
    "KOTTIK",
    "XICOMA",
    "TANBHU",
    "MUBMAI",
    "NAPJA",
    "YNOS",
    "BSA",
    "NNELCHA",
    "MANYERG",
    "ERICAAM",
    "CEFARN",
    "TUYOUBE",
    "BAFCEOOK",
    "GLEOOG",
    "OOZM",
    "TTTWIER",
    "GMARSINAT",
    "SESNGERME"
]

answer = [
    "FLOP",
    "HOPE",
    "TRIP",
    "LOVE",
    "COFFEE",
    "PYTHON",
    "JAVA",
    "C++",
    "C#",
    "CODERX",
    "ACHIEVE",
    "ENGINE",
    "JAVASCRIPT",
    "RUBY",
    "CANADA",
    "INDIA",
    "DELHI",
    "LONDON",
    "RUSSIA",
    "CHAINA",
    "TIKTOK",
    "MEXICO",
    "BHUTAN",
    "MUMBAI",
    "JAPAN",
    "SONY",
    "SAB",
    "CHANNEL",
    "GERMANY",
    "AMERICA",
    "FRANCE",
    "YOUTUBE",
    "FACEBOOK",
    "GOOGLE",
    "ZOOM",
    "TWITTER",
    "INSTAGRAM",
    "MESSENGER"
]

def change_txt():
    global jumbled,textvar
    num = random.randint(0,jumbled.__len__())
    word1 = jumbled[num]
    textvar.set(word1)

def check():
    global answer,root
    word=entry1.get()
    word=word.upper()
    if word in answer:
        messagebox.showinfo("Success","Your Answer is Right")
        entry1.delete(0,END)
        change_txt()
    else:
        messagebox.showerror("Error","Your Answer is Wrong")
        entry1.delete(0,END)




if __name__ == "__main__":
    root= Tk()
    root.geometry("450x450")
    root.minsize(350,400)
    root.title("Jumbled Words")
    root.configure(background="#4C4B4B")
    num = random.randint(0,jumbled.__len__())
    word= jumbled[num]
    textvar = StringVar()
    textvar.set(f"{word}")
    label = Label(root,textvariable=textvar,font="sans-serif 19 bold",borderwidth=6,relief=RIDGE).pack(pady=10)
    entry1 = Entry(root,font="sans-serif 14",width=30,fg="white",borderwidth=3,relief=SOLID,bg="#2C3335")
    entry1.pack(pady=6,ipady=5,ipadx=20)
    Button(root,text="check".upper(),bg="#FF4848",fg="#2F363F" ,font=("comic sans ms", 14),padx=15,pady=0,command=check).pack(pady=20)
    Button(root,text="reset".upper(),bg="#0A79DF",fg="white" ,font=("comic sans ms", 14),padx=15,pady=0,command=change_txt).pack()
    root.mainloop()