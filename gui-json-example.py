from tkinter import *
def save():
    savedData='Name is : '+name1.get()+'\n'+'Employee Salary is :'+name2.get()+'\n'+'Allowance is : '+name3.get()+'\n'+'Tax Deduction is : '+name4.get()+'\n'+'Net Salary is : '+name5.get()
    with open('savedData.txt','w') as f:
        f.writelines(savedData)
def isequal():
 salary=float(name2.get())
 allowance=float(name3.get())
 tax=(salary+allowance)/float(name4.get())
 net=salary+allowance-tax
 text_Input.set(str(net))
cal=Tk()
cal.title("Salary Calculate")
cal.geometry("800x400")
operator=""
text_Input=StringVar()
heading=Label(cal,font=("Verdana",25),text="Employee Salary")
heading.pack()
#define labels
name=Label(cal,font=("Verdana",15),text="Employee Name").place(x=10,y=45)
salary=Label(cal,font=("Verdana",15),text="Employee Salary").place(x=10,y=95)
allo=Label(cal,font=("Verdana",15),text="Allowance").place(x=10,y=150)
tax=Label(cal,font=("Verdana",15),text="Tax Deduction").place(x=10,y=205)
net=Label(cal,font=("Verdana",15),text="Net Salary").place(x=10,y=260)
#end labels
#define fields
name1=Entry(cal,font=(15)) #employee name
name1.place(x=250,y=50)
name2=Entry(cal,font=(15)) #employee brutto salary
name2.place(x=250,y=100)
name3=Entry(cal,font=(15)) #employee allowance
name3.place(x=250,y=150)
name4=Entry(cal,font=(15)) #employee tax deduction
name4.place(x=250,y=200)
name5=Entry(cal,font=(15), textvariable=text_Input) #employee net salary
name5.place(x=250,y=265)
#end fields
#define save button
save=Button(cal,font=("Verdana",15),text="Save",bg="black",fg="white",command=save).place(x=10,y
=300)
#end save button
#define net button
net=Button(cal,font=("Verdana",15),text="Net Salary",bg="black",fg="white",command=isequal).place(x=305,y=300)
#end net button
cal.mainloop()
