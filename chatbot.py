from tkinter import *


def myresponse(input):
   m=input.lower()
   if "hi"in m or "hii" in m or "hello" in m:
      return "hello"
   if "good morning" in m or  "good evening" in m or  "good night" in m or  "good afternoon" in m:
      return (m+",how can i help you!")
   if "what" in m:
      if "name" in m:
         return "my name is chatbot"
      elif "age" in m:
         return "i am one day old"
   if "how" in m:
      return "i am fine, how can i help you"
   if "name" in m:
         return "Nice to meet you"
   else:
      return "sorry ,i can't understand and allowed to answer \n  only selective questions"
      
      
    
      
    
          
def run():
    
    
    def send():
        input = tb1.get()
        tb1.delete(0, END)
        response = myresponse(input)
        tb2.insert(END, "User: " + input + "\n")
        tb2.insert(END, "Chatbot: " + response + "\n")
        tb2.insert(END, "\n")
    
    
    
    
    
    root=Tk()
    root.geometry("700x700")
    root.maxsize(700,700)
    root.title("chatbot")


    f1=Frame(root,height=600,width=800,bg="light blue")
    f1.grid(row=0,column=0)
    f2=Frame(root,height=100,width=700)
    f2.grid(row=1,column=0)


    tb1=Entry(f2,width=50,borderwidth=1,bg="ivory",font=("Arial",16,"bold"),relief=SUNKEN)
    tb1.grid(row=0,column=0,pady=42)

    Button(f2,text="send",bg="navy blue",font=("Arial",13,"bold"),fg="white",height=1,width=6,command=send).grid(row=0,column=1,padx=2)

    tb2=Text(f1,height=25,width=50,bg="light cyan",font=("Arial",14,"bold"),relief=SUNKEN)
    tb2.grid(row=0,column=0,pady=15,padx=70)


    root.mainloop()




def valid():
    username="chandra"
    password="1234"
    input1=e1.get()
    input2=e2.get()
    if username==input1 and password==input2:
        run()
    else:
        tb.insert(END,"invalid password or username")
         




window=Tk()
window.geometry("400x200")
window.maxsize(700,700)
window.title("log in")



l1=Label(text="Log in",bg="ivory",fg="black",font=("Arial",18,"bold"))
l1.pack()



f=Frame(height=300,width=300)
f.pack(padx=8,pady=8)


l2=Label(f,text="User Name",font=("Arial",12))
l2.grid(row=0,column=0,pady=10)
l3=Label(f,text="password",font=("Arial",12))
l3.grid(row=1,column=0,pady=10)


e1=Entry(f,width=30)
e1.grid(row=0,column=1)
e2=Entry(f,width=30)
e2.grid(row=1,column=1)

b=Button(f,text="submit",height=1,width=5,bg="blue",fg="white",command=valid)
b.grid(row=2,column=1)

tb=Text(f,height=1,width=50)
tb.grid(row=3,column=1,pady=4)

window.mainloop()