from tkinter import *
from tkinter.font import *
import random
from collections import defaultdict
from tkinter import messagebox
root=Tk()
root.resizable(0,0)
'''-----------------------------SAVING NAMES------------------------------'''

name=[]
with open("iname.csv","r") as f:
    for lines in f:
        name.append(lines[:-1])
        random.shuffle(name)
#print(name)

'''------------------------------QUESTIONS--------------------------------'''

ques = random.choice(name)
ques = ques[:-2]

'''---------------------------IMAGE ACCESSING-----------------------------'''

pname=[0]*9
for i in range(9):
    image_name='C:\\Users\\Satyamskillz\\PycharmProjects\\project1\\100\\{}.png'.format(name[i])
    pname[i]=PhotoImage(file=image_name)

'''--------------------------CHANGING IMAGE--------------------------------'''

def change_image():
    ran_name = random.choice(name)
    path_name = 'C:\\Users\\Satyamskillz\\PycharmProjects\\project1\\100\\{}.png'.format(ran_name)
    newname = PhotoImage(file=path_name)
    return ([newname,ran_name])

'''------------CHANGING BUTTON IMAGE AND STORING CHECKPOINT-----------------'''

save_point=defaultdict(list)
new_point={}
c=0
def appear(index,ename):
    #buttons[index].config(state="disabled")
    global c
    global save_point
    c=c+1
    newname = change_image()
    if(index not in save_point):
        save_point[index].append(ename)
        new_point[index] = (newname[1])
    else:
        save_point[index].append(new_point[index])
        new_point.pop(index)
        new_point[index] = (newname[1])

    buttons[index].config(image=newname[0])
    buttons[index].image = newname[0]

'''------------------------------CHECKPOINT---------------------------------'''
def checkpoint():
    count=0
    #print(save_point)
    for i in save_point:
        for j in save_point[i]:
            if(ques in j):
                count+=1
    if(c!=0):
        if(count/c>=0.5):
            messagebox.showinfo("Welcome Human","You are varified")
        else:
            messagebox.showerror("Welcome Machine", "You are not varified, If you are human then try again")
    else:
        k=0
        for i in name[:9]:
            if(ques in i):
                k+=1
        print(k)
        if(k!=0):
            messagebox.showerror("Welcome Machine", "You are not varified, If you are human then try again")
        else:
            messagebox.showinfo("Welcome Human", "You are varified")

'''--------------------------------FONT-------------------------------------'''

mfont=Font(family="Time New Roman", size=20, weight="bold")

'''-------------------------------TOP FRAME--------------------------------'''

topframe=Frame(root)
l1=Label(root,text="IMAGE BASED CAPTCHA",font=mfont,bg="black",fg="white",width=28).pack()
l2=Label(root,text="Select "+ques.upper(),bg="grey",fg="yellow", width=68).pack()
topframe.pack(side=TOP)

'''--------------------------------MID FRAME--------------------------------'''

midframe=Frame(root,bg="black")
buttons = []

for index in range(9):
    ename = name[index]
    n = pname[index]
    button = Button(midframe, image=n, width=150,bg="black", height=150, relief=GROOVE,
                    command=lambda index=index, ename=ename: appear(index,ename))
    button.grid(padx=2, pady=2, row=index%3, column=index//3)
    buttons.append(button)

midframe.pack()

'''--------------------------------BOTTOM FRAME------------------------------'''

bottomframe = Frame(root)
varify = Button(bottomframe, text="VERIFY", font=mfont,width=28,pady=10, relief="flat", bg="grey",fg="white",command=checkpoint)
varify.pack()
bottomframe.pack()

'''------------------------------------------------------------------------'''

root.geometry("500x610+120+120")
root.mainloop()