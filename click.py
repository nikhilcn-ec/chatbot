import re
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
def developer():
    w1=Toplevel()
    w1.geometry("500x350")
    w1.title("Developer_page")

    op=Image.open("logo.png")
    img=op.resize((50,50),  Image.LANCZOS)
    log=ImageTk.PhotoImage(img)


    f=Frame(w1,bg="light blue")
    f.pack()
    f1=LabelFrame(f,bg="Dodgerblue3")
    f1.pack(padx=10,pady=5)
    l1=Frame(f1)
    lg=Label(l1,image=log)
    lg.pack(padx=4,pady=5)
    l1.grid(row=0,column=0,sticky="nw")
    l2=Label(f1,bg="Dodgerblue3",text="Developer details",font=("Arial",14,"bold"))
    l2.grid(row=0,column=1,padx=110,pady=15,sticky="nw")
    det=Frame(f,height=280,width=440,bg="light blue")
    sen=Label(det,bg="light blue",text="   The Chatbot application was expertly developed by Nikhil CN on \n12th June 2023, utilizing the power of Python programming language. \nNikhil CN, a skilled developer, incorporated essential modules such \nas Tkinter, PIL, and Chatterbot to create a robust and efficient\n chatbot solution. The aim of this application is to provide users\n with a seamless and interactive conversational experience. Through\n the integration of advanced AI technology and user-friendly \ninterfaces, the Chatbot assists users by offering automated support,\n promptly answering queries, and enhancing overall user engagement.\n With its ability to understand and respond intelligently,\n the Chatbot aims to revolutionize communication\n and improve user satisfaction.",font=("Arial",10))
    sen.pack()
    det.pack(side="bottom",anchor="nw",padx=50,pady=30)
    w1.mainloop()











def about():
    w1=Toplevel()
    w1.geometry("500x350")
    w1.title("About_us_page")

    op=Image.open("logo.png")
    img=op.resize((50,50),  Image.LANCZOS)
    log=ImageTk.PhotoImage(img)


    f=Frame(w1,bg="light blue")
    f.pack()
    f1=LabelFrame(f,bg="Dodgerblue3")
    f1.pack(padx=10,pady=5)
    l1=Frame(f1)
    lg=Label(l1,image=log)
    lg.pack(padx=4,pady=5)
    l1.grid(row=0,column=0,sticky="nw")
    l2=Label(f1,bg="Dodgerblue3",text="About us",font=("Arial",14,"bold"))
    l2.grid(row=0,column=1,padx=160,pady=15,sticky="nw")
    det=Frame(f,height=280,width=600,bg="light blue")
    sen=Label(det,bg="light blue",text="Welcome to Chatbot, developed by Nikhil CN. With a passion for\ninnovation and expertise in Python programming, Nikhil has created\n this advanced chatbot application. Our previous projects include\n successful ventures in the field of IoT.Now, we bring our \ntechnical prowess and experience to the realm of conversational AI.\nUsing modules like Tkinter, PIL, and Chatterbot, we strive to provide \nseamless interactions and intelligent responses to our users.\nOur commitment is to enhance user engagement and deliver efficient \nautomated support, making communication a breeze. Join \nus on this exciting journey aswe revolutionize the way we interact \nwith technology.",font=("Arial",10))
    sen.pack()
    det.pack(side="bottom",anchor="nw",padx=50,pady=30)
    w1.mainloop()



def log_in():
    def submit():
        user=e1.get()
        pss=e2.get()
        if(user.lower()=="nikhil") and (pss=="1234"):
            try_demo()
        else:
            messagebox.showinfo(title="log_in error",message="invalid password or username")    
    w1=Toplevel()
    w1.geometry("500x350")
    w1.title("Log_in Page")

    op=Image.open("logo.png")
    img=op.resize((50,50),  Image.LANCZOS)
    log=ImageTk.PhotoImage(img)


    f=Frame(w1,bg="light blue")
    f.pack()
    f1=LabelFrame(f,bg="Dodgerblue3")
    f1.pack(padx=10,pady=5)
    l1=Frame(f1)
    lg=Label(l1,image=log)
    lg.pack(padx=4,pady=5)
    l1.grid(row=0,column=0,sticky="nw")
    l2=Label(f1,bg="Dodgerblue3",text="Log_in to Chatbot",font=("Arial",14,"bold"))
    l2.grid(row=0,column=1,padx=120,pady=15,sticky="nw")
    det=Frame(f,height=250,width=300)
    det.pack(side="bottom",anchor="center",padx=20,pady=20)
    lf=LabelFrame(det)
    lf.pack()
    t=Label(lf,text="Log in",font=("Arial",12,"bold"))
    t.grid(row=0,column=0,columnspan=2)
    u=Label(lf,text="User name:",font=("Arial",10))
    u.grid(row=1,column=0,sticky="news")
    p=Label(lf,text="Password:",font=("Arial",10))
    p.grid(row=2,column=0,sticky="news")
    e1=Entry(lf)
    e1.grid(row=1,column=1,sticky="news")
    e2=Entry(lf)
    e2.grid(row=2,column=1,sticky="news")
    b1=Button(lf,text="submit",bg="red",command=submit)
    b1.grid(row=3,column=0,columnspan=2)
    for widgets in lf.winfo_children():
        widgets.grid_configure(padx=10,pady=10)
    w1.mainloop()
     









def contact():
    w1=Toplevel()
    w1.geometry("500x350")
    w1.title("contact_page")

    op=Image.open("logo.png")
    img=op.resize((50,50),  Image.LANCZOS)
    log=ImageTk.PhotoImage(img)


    f=Frame(w1,bg="light blue")
    f.pack()
    f1=LabelFrame(f,bg="Dodgerblue3")
    f1.pack(padx=10,pady=5)
    l1=Frame(f1)
    lg=Label(l1,image=log)
    lg.pack(padx=4,pady=5)
    l1.grid(row=0,column=0,sticky="nw")
    l2=Label(f1,bg="Dodgerblue3",text="Contact",font=("Arial",14,"bold"))
    l2.grid(row=0,column=1,padx=160,pady=15,sticky="nw")
    det=Frame(f,height=280,width=600,bg="light blue")
    sen=Label(det,bg="light blue",text="For any inquiries or communication regarding the Chatbot\n application developed by Nikhil CN, you can reach out via email\n at nikhilcnn123@gmail.com. Please feel free to send any questions,\n feedback, or collaboration proposals to this email address.\n Unfortunately, I don't have access to specific phone numbers. \nHowever, email is a reliable means of contact, and Nikhil CN will be\n pleased to assist you through that medium.",font=("Arial",10))
    sen.pack()
    det.pack(side="bottom",anchor="nw",padx=50,pady=70)
    w1.mainloop()

def try_demo():
    def on():
        input = tb1.get()
        tb1.delete(0, END)
        response = myresponse(input)
        tb2.insert(END, "User: " + input + "\n")
        tb2.insert(END, "Chatbot: " + response + "\n")
        tb2.insert(END, "\n")

    def myresponse(input):
        m=input.lower()
        if "hi"in m or "hii" in m or "hello" in m:
            return "hello"
        elif "good morning" in m or  "good evening" in m or  "good night" in m or  "good afternoon" in m:
            return (m+",how can i help you!")
        elif "what" in m:
            if "name" in m:
                return "my name is chatbot"
            elif "age" in m:
                return "i am one day old"
        elif "how" in m:
            return "i am fine, how can i help you"
        if "name" in m:
            return "Nice to meet you"
        else:
            return "sorry ,i can't understand"
    w1=Toplevel()
    w1.geometry("700x700")
    w1.title("contact_page")

    op=Image.open("logo.png")
    img=op.resize((50,50),  Image.LANCZOS)
    log=ImageTk.PhotoImage(img)


    f=Frame(w1,bg="light blue")
    f.pack()
    f1=LabelFrame(f,bg="Dodgerblue3")
    f1.pack(padx=10,pady=5)
    l1=Frame(f1)
    lg=Label(l1,image=log)
    lg.pack(padx=4,pady=5)
    l1.grid(row=0,column=0,sticky="nw")
    l2=Label(f1,bg="Dodgerblue3",font=("Arial",14,"bold"))
    l2.grid(row=0,column=1,padx=300,pady=15,sticky="nw")


    det=Frame(f,height=500,width=500,bg="light blue")
    tb1=Entry(det,width=45,borderwidth=5,bg="ivory",font=("Arial",16,"bold"),relief=SUNKEN)
    tb1.grid(row=1,column=0,padx=5,pady=10,sticky="w")

    Button(det,text="send",bg="navy blue",font=("Arial",13,"bold"),fg="white",height=1,width=6,command=on).place(x=575,y=575)
    tb2=Text(det,height=25,width=50,bg="light cyan",font=("Arial",14,"bold"),relief=SUNKEN)
    tb2.grid(row=0,column=0,pady=5,padx=80)
    det.pack(side="bottom",anchor="nw",padx=5)
    w1.mainloop()
    
                