
from tkinter import * 

root = Tk()

root.geometry("1000x600")

root.title("Flames")

Tops = Frame(root, width = 1600, relief = SUNKEN) 
Tops.pack(side = TOP) 

f1 = Frame(root, width = 800, height = 700, relief = SUNKEN) 
f1.pack(side = TOP)

f2 = Frame(root, width = 800, height = 700, relief = SUNKEN) 
f2.pack(side = TOP) 

f3 = Frame(root, width = 800, height = 700, relief = SUNKEN) 
f3.pack(side = TOP) 

lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'), 
		text = "FLAMES", fg = "Black", bd = 10, anchor='w')

lblInfo.grid(row = 0, column = 0)

firstperson = StringVar()
secondperson = StringVar()
relation = StringVar()

def find():
    a=[i.lower() for i in firstperson.get() if i!=" "]
    b=[j.lower() for j in secondperson.get() if j!=" "]
    x=a[:]
    y=b[:]
    for i in x:
        for j in y:
            if i==j and i in a and j in b:
                a.remove(i)
                b.remove(j)
                break
    
    count=len(a)+len(b)
    flames=["Friendship","Love","Affection","Marriage","Enemies","Siblings"]
    while(len(flames)!=1):
        i=count%len(flames)
        if i==0:
            i=len(flames)
        flames=flames[i:]+flames[:(i-1)]    
    
    relation.set(flames[0])
    

def end():
    root.destroy()

def reset():
    firstperson.set("")
    secondperson.set("")
    relation.set("Click on Show Relation")
    

label1 = Label(f1, font = ('arial', 16, 'bold'), 
				text = "Name of First Person:", bd = 16, anchor = "w") 
				
label1.grid(row = 0, column = 0) 

entry1 = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = firstperson, bd = 10, insertwidth = 4, 
						bg = "powder blue")

entry1.grid(row = 0, column = 1)

label2 = Label(f1, font = ('arial', 16, 'bold'), 
				text = "Name of Second Person:", bd = 16, anchor = "w") 
				
label2.grid(row = 1, column = 0) 

entry2 = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = secondperson, bd = 10, insertwidth = 4, bg = "powder blue") 

entry2.grid(row = 1,column = 1)

btnrel = Button(f2, padx = 16, pady = 8, bd = 16, fg = "black", 
				font = ('arial', 16, 'bold'), width = 10, 
					text = "Show Relation", bg = "blue", 
						command = find).pack()

label3 = Label(f1, font = ('arial', 16, 'bold'), 
				text = "Relation is:", bd = 16, anchor = "w")

relation.set("Click on Show Relation")

label3.grid(row = 2, column=0)

entry3 = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = relation, bd = 10,
                              insertwidth = 4, bg = "powder blue")

entry3.grid(row = 2, column=1)
    
btnReset = Button(f3, padx = 16, pady = 8, bd = 16, 
				fg = "black", font = ('arial', 16, 'bold'), 
					width = 10, text = "Reset", bg = "green", 
				              command = reset).grid(row = 7, column = 0) 

btnExit = Button(f3, padx = 16, pady = 8, bd = 16, 
				fg = "black", font = ('arial', 16, 'bold'), 
					width = 10, text = "Exit", bg = "red", 
				                command = end).grid(row = 7, column = 1) 



