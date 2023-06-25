from tkinter import *
from tkinter import ttk
y=0
a=ttk.Notebook()
frame1=ttk.Frame(a)
frame2=ttk.Frame(a)
frame3=ttk.Frame(a)
frame4=ttk.Frame(a)
frame5=ttk.Frame(a)
root=ttk.Frame(a)
c=0
def quiz(y):
    global c
    a.add(frame1,text="Q1")
    a.add(frame2,text="Q2")
    a.add(frame3,text="Q3")
    a.add(frame4,text="Q4")
    a.add(frame5,text="Q5")
    
    Label(frame1,text="Total keywords in python ?",font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame1,text="33",font=("Arial",30,"bold"),bg="light blue",command=a1_right).grid(row=3,column=1)
    Button(frame1,text="31",font=("Arial",30,"bold"),bg="light blue",command=a1_wrong).grid(row=3,column=2)
    Button(frame1,text="30",font=("Arial",30,"bold"),bg="light blue",command=a1_wrong).grid(row=3,column=3)
       
    Label(frame2,text="output of 2**3",font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame2,text="6",font=("Arial",30,"bold"),bg="light blue",command=a2_wrong).grid(row=3,column=1)
    Button(frame2,text="7",font=("Arial",30,"bold"),bg="light blue",command=a2_wrong).grid(row=3,column=2)
    Button(frame2,text="8",font=("Arial",30,"bold"),bg="light blue",command=a2_right).grid(row=3,column=3)

    Label(frame3,text="output of np.arange(1,5)?",font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame3,text="[1,2,3,4]",font=("Arial",30,"bold"),bg="light blue",command=a3_right).grid(row=3,column=1)
    Button(frame3,text="[0,1,2,3,4]",font=("Arial",30,"bold"),bg="light blue",command=a3_wrong).grid(row=3,column=2)
    Button(frame3,text="[1,2,3,4,5]",font=("Arial",30,"bold"),bg="light blue",command=a3_wrong).grid(row=3,column=3)

    Label(frame4,text="keyword used to declare a function ?",font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame4,text="def",font=("Arial",30,"bold"),bg="light blue",command=a4_right).grid(row=3,column=1)
    Button(frame4,text="fun",font=("Arial",30,"bold"),bg="light blue",command=a4_wrong).grid(row=3,column=2)
    Button(frame4,text="class",font=("Arial",30,"bold"),bg="light blue",command=a4_wrong).grid(row=3,column=3)

    Label(frame5,text="output of 2*12",font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame5,text="23",font=("Arial",30,"bold"),bg="light blue",command=a5_wrong).grid(row=3,column=1)
    Button(frame5,text="42",font=("Arial",30,"bold"),bg="light blue",command=a5_wrong).grid(row=3,column=2)
    Button(frame5,text="24",font=("Arial",30,"bold"),bg="light blue",command=a5_right).grid(row=3,column=3)
    Button_next=Button(frame5,text="check results",font=("verdana",40),bg="yellow",fg="black",command=res).grid(row=4,column=2)

def a1_right():
    global c
    c=c+1
    Label(frame1,text="Correct" ,font=("Arial",40,"bold"),background="green",fg="Yellow").grid(row=1,column=2)
    #Label(frame1,text="Marks obtained:1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)
def a1_wrong():           
    Label(frame1,text="InCorrect ",font=("Arial",40,"bold"),background="red",fg="Yellow").grid(row=1,column=2)
    #Label(frame1,text="Marks obtained:0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)
def a2_right():
    global c
    c=c+1
    Label(frame2,text="Correct",font=("Arial",40,"bold"),background="green",fg="Yellow").grid(row=1,column=2)
    #Label(frame2,text="Marks obtained:1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)
def a2_wrong():
    Label(frame2,text="InCorrect",font=("Arial",40,"bold"),background="red",fg="Yellow").grid(row=1,column=2)
    #Label(frame2,text="Marks obtained:0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)
def a3_right():
    global c
    c=c+1
    Label(frame3,text="Correct ",font=("Arial",40,"bold"),background="green",fg="Yellow").grid(row=1,column=2)
    #Label(frame3,text="Marks obtained:1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)
def a3_wrong():
    Label(frame3,text="InCorrect ",font=("Arial",40,"bold"),background="red",fg="Yellow").grid(row=1,column=2)
    #Label(frame3,text="Marks obtained:0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)
def a4_right():
    global c
    c=c+1
    Label(frame4,text="Correct",font=("Arial",40,"bold"),background="green",fg="Yellow").grid(row=1,column=2)
    #Label(frame4,text="Marks obtained:1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)
def a4_wrong():
    Label(frame4,text="InCorrect",font=("Arial",40,"bold"),background="red",fg="Yellow").grid(row=1,column=2)
    #Label(frame4,text="Marks obtained:0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)
def a5_right():
    global c
    c=c+1
    Label(frame5,text="Correct ",font=("Arial",40,"bold"),background="green",fg="Yellow").grid(row=1,column=2)
    #Label(frame5,text="Marks obtained:1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)
    
def a5_wrong():
    Label(frame5,text="InCorrect",font=("Arial",40,"bold"),background="red",fg="Yellow").grid(row=1,column=2)
    #Label(frame5,text="Marks obtained:0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)
def res():
    Label(frame5,text="your final score is:"+str(c),font=("verdana",40),fg="blue").grid(row=5,column=2)
    if(int(c)>=3):
        Label(frame5,text="Congratulations!",font=("italic",40),fg="green").grid(row=6,column=2)
    else:
        Label(frame5,text="sorry better luck next time",font=("verdana",40),fg="red").grid(row=6,column=2)
        
quiz(y)
a.pack()
a.mainloop()

