from tkinter import *
# windows and widgets

window = Tk()

def gr_to_lb():
    grams=float(e1_value.get())*1000  # convert kilograms to grams
    pounds=float(e1_value.get())*2.20462  # convert kilograms to pounds
    ounces=float(e1_value.get())*35.274  # convert kilograms to ounces
    t1.delete("1.0", END)
    t2.delete("1.0", END)
    t3.delete("1.0", END)
    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)

t0=Label(window,text='Kg')
t0.grid(row=0,column=0)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)



e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1 = Button(window,text="Convert",command=gr_to_lb)
b1.grid(row=0,column=2)   # more control over position vs pack()






window.mainloop()