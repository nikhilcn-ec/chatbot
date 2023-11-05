import re
from tkinter import *
from PIL import Image, ImageTk
import click as click
def main():
    root=Tk()
    root.geometry("500x350")
    root.title("chatbot-HOME")

    op1=Image.open("pic.png")
    img1=op1.resize((200,250),  Image.LANCZOS)
    photo=ImageTk.PhotoImage(img1)

    op=Image.open("logo.png")
    img=op.resize((50,50),  Image.LANCZOS)
    log=ImageTk.PhotoImage(img)




    fr=Frame(root,bg="light blue")
    fr.pack()
    lf=LabelFrame(fr,bg="Dodgerblue3")
    lf.pack()



    l1=Frame(lf)
    lg=Label(l1,image=log)
    lg.pack()
    l1.grid(row=0,column=0,padx=10,pady=3,sticky="new")



    f1=Frame(lf,height=50,width=300,bg="Dodgerblue3")
    b1=Button(f1,text="Developer",bg="LightCyan2",font=("Arial",10,"bold"),command=click.developer)
    b2=Button(f1,text="About",bg="LightCyan2",font=("Arial",10,"bold"),command=click.about)
    b3=Button(f1,text="Contact",bg="LightCyan2",font=("Arial",10,"bold"),command=click.contact)
    b4=Button(f1,text="Log in",bg="LightCyan2",font=("Arial",10,"bold"),command=click.log_in)



    f1.grid(row=0,column=1,padx=30)
    b1.grid(row=0,column=1)
    b2.grid(row=0,column=2)
    b3.grid(row=0,column=3)
    b4.grid(row=0,column=4)
    for widget in f1.winfo_children():
        widget.grid_configure(padx=20)
    
    intro=Frame(fr,height=200,width=200,bg="light blue")
    s1=Label(intro,text="INRODUCING",font=("Forte",14),bg="light blue")
    s2=Label(intro,text="your friendly and knowledgeable",font=("Forte",12),bg="light blue")
    s3=Label(intro,text="chatbot, equipped with advanced",font=("Forte",12),bg="light blue")
    s4=Label(intro,text="language capabilities to assist",font=("Forte",12),bg="light blue")
    s5=Label(intro,text="and engage in conversations",font=("Forte",12),bg="light blue")
    s1.grid(row=0,column=0,sticky="w")
    s2.grid(row=1,column=0)
    s3.grid(row=2,column=0)
    s4.grid(row=3,column=0)
    s5.grid(row=4,column=0)
    intro.pack(padx=10,pady=60,side="left",anchor="nw")
    
    pic=Frame(fr,height=200,width=200,bg="green")
    li=Label(pic,image=photo)
    li.pack()
    pic.pack(padx=10,pady=20)

    demo=Button(fr,text="try Demo",bg="red" ,fg="Black",font=("Arial",10,"bold"),command=click.try_demo)
    demo.place(x=80,y=280)   


    root.mainloop()