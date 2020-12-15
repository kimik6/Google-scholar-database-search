####          KIMIA KAMIYAB
import  backend
from tkinter import *
root = Tk()
root.title("KIMIA KAMIYAB     Google Scholar")
root.geometry("500x340")
root.resizable(width=False,height=False)
color_bg = 'light gray'
color2_bg='lightblue'
root.configure(bg=color2_bg)
topFrame=Frame(root,width=500,height=160,bg=color_bg)
topFrame.grid(row=0, column=0)
l1 = Label(topFrame, text="First Name")
l1.grid(row=0,column=0)
#l1.configure(bg=color_bg)

l2 = Label(topFrame, text="Last Name")
l2.grid(row=2,column=0)
#l2.configure(bg=color_bg)

firstname_text = StringVar()
e1 = Entry(topFrame,textvariable=firstname_text,highlightbackground = "red", highlightcolor= "red")
e1.grid(row=0,column=1)

lastname_text = StringVar()
e2 = Entry(topFrame,textvariable=lastname_text)
e2.grid(row=2,column=1)
y=' '
def insert_user(fn='',ln=''):
    list2.delete(0, END)
    y=backend.insert(fn,ln)
    list2.insert(END, y)



list2 =Listbox(topFrame, width=45 ,height=1,bg=color_bg,bd=0)
list2.grid(row=1,column=3,rowspan=2,columnspan=1)

b1 =Button(topFrame, text="Submit to Database",width=45,command= lambda:insert_user(e1.get(),e2.get()))
b1.grid(row=3, column=3)
b1.configure(bg='dark gray')

bottomFrame=Frame(root,width=500,height=300,bg=color2_bg)
bottomFrame.grid(row=5, column=0)

l3 = Label(bottomFrame, text="First Name")
l3.grid(row=5,column=0)
l3.configure(bg=color2_bg)

l4 = Label(bottomFrame, text="Last Name")
l4.grid(row=6,column=0)
l4.configure(bg=color2_bg)

firstname_text2 = StringVar()
e3 = Entry(bottomFrame,textvariable=firstname_text2)
e3.grid(row=5,column=1)

lastname_text2 = StringVar()
e4 = Entry(bottomFrame,textvariable=lastname_text2)
e4.grid(row=6,column=1)
OptionList = [
"intrests",
"Articles",
"affiliation",
]
variable = StringVar(bottomFrame)
variable.set(OptionList[0])

opt = OptionMenu(bottomFrame, variable, *OptionList)
opt.config(width=15, font=('Helvetica', 10))
opt.grid(row=6,column=5)

list1 =Listbox(bottomFrame, width=50 ,height=12)
list1.grid(row=7,column=0,rowspan=5,columnspan=4)
sb1 = Scrollbar(bottomFrame,orient="vertical", command=list1.yview)
sb1.grid(row=7,column=4,rowspan=5)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
sb2 = Scrollbar(bottomFrame,orient=HORIZONTAL, command=list1.xview)
sb2.grid(row=12,column=0,columnspan=4)
list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)

def search_user(fN,lN,mode):
    list1.delete(0, END)
    d = backend.search(fN, lN, mode)
    if d == 'This user doesnt exists':
        list1.insert(END, d)
    else:
        for i in d:
            list1.insert(END, i)

b2 =Button(bottomFrame, text="Search",width=15,command=lambda :search_user(e3.get(),e4.get(),variable.get()))
b2.grid(row=7, column=5)
b2.configure(bg='dark gray')

root.mainloop()