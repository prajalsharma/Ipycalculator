from tkinter import *
from tkinter import messagebox
import math
from time import *
from tkinter.font import Font
a=Tk(className=" Prajal Calculator")
a.configure(background="#A8E1F8")
sq=StringVar()
ld=StringVar()
sc=StringVar()
sx=StringVar()
svl=StringVar()
pw=StringVar()
pnt=StringVar()
vac=StringVar()
vcn=StringVar()
lt=StringVar()
vl=StringVar()
v=StringVar()
v1=StringVar()
v2=StringVar()
v3=StringVar()
vp=StringVar()
v4=StringVar()
v5=StringVar()
v6=StringVar()
vm=StringVar()
v7=StringVar()
v8=StringVar()
v9=StringVar()
vml=StringVar()
vz=StringVar()
vdz=StringVar()
veq=StringVar()
vd=StringVar()
vl.set("Value")
l=Label(a,textvariable=vl,fg="blue",bg="#A8E1F8",bd=3,width=20)
l.grid(row=1,column=1)
t1=Entry(a,textvariable=v,bd=5,cursor="arrow",relief="raised",width=45)
t1.grid(row=1,column=2,columnspan=4)
text=Text(a)
mfnt=Font(family="Times New Roman",size=8,weight="bold")
text.configure(font=mfnt)
v1.set("1")
def one():
    t1.insert(END,"1")
b1=Button(a,text="1",fg="black",font=mfnt,activebackground="cyan",bd=7,relief="raised",cursor="spider",width=7,command=one,textvariable=v1)
b1.grid(row=3,column=2)
v2.set("2")
def two():
    t1.insert(END,"2")
b2=Button(a,text="2",fg="black",font=mfnt,activebackground="cyan",bd=7,relief="raised",cursor="spider",width=7,textvariable=v2,command=two)
b2.grid(row=3,column=3)
v3.set("3")
def three():
    t1.insert(END,"3")
b3=Button(a,text="3",fg="black",font=mfnt,activebackground="cyan",bd=7,relief="raised",cursor="spider",width=7,textvariable=v3,command=three)
b3.grid(row=3,column=4)
vp.set("+")
def add():
    t1.insert(END,"+")
bp=Button(a,text="+",font=mfnt,activebackground="cyan",fg="Red",bd=7,relief="raised",cursor="spider",width=7,textvariable=vp,command=add)
bp.grid(row=3,column=5)
v4.set("4")
def four():
    t1.insert(END,"4")
b4=Button(a,text="4",fg="black",font=mfnt,activebackground="cyan",bd=7,relief="raised",cursor="spider",width=7,textvariable=v4,command=four)
b4.grid(row=4,column=2)
v5.set("5")
def five():
    t1.insert(END,"5")
b5=Button(a,text="5",fg="black",font=mfnt,activebackground="cyan",bd=7,relief="raised",cursor="spider",width=7,textvariable=v5,command=five)
b5.grid(row=4,column=3)
v6.set("6")
def six():
    t1.insert(END,"6")
b6=Button(a,text="6",fg="black",font=mfnt,activebackground="cyan",bd=7,relief="raised",cursor="spider",width=7,textvariable=v6,command=six)
b6.grid(row=4,column=4)
vm.set("-")
def minus():
    t1.insert(END,"-")
bm=Button(a,text="-",font=mfnt,activebackground="cyan",fg="Red",bd=7,relief="raised",cursor="spider",width=7,textvariable=vm,command=minus)
bm.grid(row=4,column=5)
v7.set("7")
def seven():
    t1.insert(END,"7")
b7=Button(a,text="7",fg="black",font=mfnt,activebackground="cyan",bd=7,relief="raised",cursor="spider",width=7,textvariable=v7,command=seven)
b7.grid(row=5,column=2)
v8.set("8")
def eth():
    t1.insert(END,"8")
b8=Button(a,text="8",fg="black",font=mfnt,activebackground="cyan",bd=7,relief="raised",cursor="spider",width=7,textvariable=v8,command=eth)
b8.grid(row=5,column=3)
v9.set("9")
def nine():
    t1.insert(END,"9")
b9=Button(a,text="9",fg="black",font=mfnt,activebackground="cyan",bd=7,relief="raised",cursor="spider",width=7,textvariable=v9,command=nine)
b9.grid(row=5,column=4)
vml.set("*")
def mul():
    t1.insert(END,"*")
bml=Button(a,text="*",font=mfnt,activebackground="cyan",fg="Red",bd=8,relief="raised",cursor="spider",width=7,textvariable=vml,command=mul)
bml.grid(row=5,column=5)
vz.set("0")
def zero():
    t1.insert(END,"0")
b0=Button(a,text="0",fg="black",font=mfnt,activebackground="cyan",bd=7,relief="raised",cursor="spider",width=7,textvariable=vz,command=zero)
b0.grid(row=6,column=2)
vdz.set("00")
def dzero():
    t1.insert(END,"00")
b00=Button(a,text="00",fg="black",font=mfnt,activebackground="cyan",bd=8,relief="raised",cursor="spider",width=7,textvariable=vdz,command=dzero)
b00.grid(row=6,column=3)
veq.set("=")
def eq():
    try:
        s=eval(t1.get())
    except Exception as e:
        messagebox.showerror("Error","Operation Can not Perform!!!!")
        t1.delete(0,END)
    else:
        t1.delete(0,END)
        t1.insert(0,s)
beq=Button(a,text="=",font=mfnt,activebackground="cyan",fg="Red",bd=7,relief="raised",cursor="spider",width=7,textvariable=veq,command=eq)
beq.grid(row=6,column=4)
vd.set("/")
def div():
    t1.insert(END,"/")
bd=Button(a,text="/",font=mfnt,activebackground="cyan",bd=8,fg="Red",relief="raised",cursor="spider",width=7,textvariable=vd,command=div)
bd.grid(row=6,column=5)

vac.set("<-")
def scan():
    t1.delete(len(t1.get())-1)
ac=Button(a,text="<-",font=mfnt,bd=7,activebackground="cyan",fg="Red",relief="raised",cursor="spider",width=7,textvariable=vac,command=scan,height=1)
ac.grid(row=7,column=2)
pnt.set(".")
def pnt():
    t1.insert(END,".")
pnt=Button(a,text=".",font=mfnt,bd=7,activebackground="cyan",fg="Black",relief="raised",cursor="spider",width=7,textvariable=pnt,command=pnt,height=1)
pnt.grid(row=7,column=3)
vcn.set("Cancel")
def can():
    t1.delete(0,END)
can=Button(a,text="Cancel",font=mfnt,bd=7,activebackground="cyan",fg="Red",relief="raised",cursor="spider",width=7,textvariable=vcn,command=can)
can.grid(row=7,column=4)
pw.set("Pow[^]")
def pwr():
    p=(t1.get())
    try:
        r=(pow(float(p),2))
    except Exception as e:
         messagebox.showerror("Error","It is not Allowed !!!!")
         t1.delete(0,END)
    else:
        t1.delete(0,END)
        t1.insert(END,r)
pwr=Button(a,text="Power",font=mfnt,bd=7,activebackground="cyan",fg="Red",relief="raised",cursor="spider",width=7,textvariable=pw,command=pwr)
pwr.grid(row=7,column=5)
def xdv():
    try:
        z1=t1.get()
        tmp=(1/(float(z1)))
    except Exception as e:
        messagebox.showerror("Error","Can not perform this Operation!!!")
        t1.delete(0,END)
    else:
        t1.delete(0,END)
        t1.insert(0,tmp)
sx.set("1/x")
sx=Button(a,bd=7,command=xdv,font=mfnt,activebackground="cyan",fg="Blue",relief="raised",cursor="spider",width=7,textvariable=sx)
sx.grid(row=8,column=2)
def cube():
    p=(t1.get())
    try:
        r=(pow(float(p),3))
    except Exception as e:
         messagebox.showerror("Error","It is not Allowed !!!!")
         t1.delete(0,END)
    else:
        t1.delete(0,END)
        t1.insert(END,r)   
sc.set("x3")
sc=Button(a,bd=7,command=cube,font=mfnt,activebackground="cyan",fg="Blue",relief="raised",cursor="spider",width=7,textvariable=sc)
sc.grid(row=8,column=3)
def sroot():
    z1=(t1.get())
    try:
         tmp=eval("math.sqrt(float(z1))")
    except Exception as e:
         messagebox.showerror("Error","It is not Allowed !!!!")
         t1.delete(0,END)
    else:
         t1.delete(0,END)
         t1.insert(END,tmp)
sq.set("root")
sq=Button(a,bd=7,command=sroot,font=mfnt,activebackground="cyan",fg="Blue",relief="raised",cursor="spider",width=7,textvariable=sq)
sq.grid(row=8,column=4)
def lg():
    z1=(t1.get())
    try:
         tmp=eval("math.log(float(z1),10)")
    except Exception as e:
         messagebox.showerror("Error","It is not Allowed !!!!")
         t1.delete(0,END)
    else:
         t1.delete(0,END)
         t1.insert(END,tmp)
svl.set("log b(10)")
svl=Button(a,command=lg,font=mfnt,text="val",bd=7,activebackground="cyan",fg="Blue",relief="raised",width=7,textvariable=svl)
svl.grid(row=8,column=5)
text=Text(a)
mnt=Font(family="Forte",size=12,weight="bold",slant="italic",underline=1)
text.configure(font=mnt)
lm=Label(a,font=mnt,textvariable=lt,anchor="se",fg="Red",bg="#A8E1F8",cursor="spider",width=25,relief="flat")
lt.set("Created By Prajal Sharma")
lm.grid(row=9,column=6)
a.resizable(width=False,height=False)
def tm():
    messagebox.showinfo("Current Date And Time",ctime())
ld=Button(a,font=mnt,text="Date and Time?",fg="Red",bg="#A8E1F8",anchor="sw",cursor="spider",command=tm,relief="flat")
ld.grid(row=9,column=1)
def quit(event=None):
    try:
        x=messagebox.askokcancel("Calculator","Do you want to close it")
        if x==True:
            a.destroy()
    except Exception as e:
        print(e)
bqt=Button(a,font=mnt,text="Exit",command=quit,fg="blue",bg="yellow",bd=4,activebackground="cyan",relief="raised",cursor="spider")
bqt.grid(row=1,column=7)
a.mainloop()

    




