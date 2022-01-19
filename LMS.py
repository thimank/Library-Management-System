from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox

cn=sqlite3.connect("Library.db")
cur=cn.cursor()

global r	
r=Tk()
#r.attributes('-fullscreen',True) 
r.title("Library Management System")
r.geometry('1080x1920')


###########ADDING BOOKS#################
def AB():
	window= Toplevel(r)
	window.title("ADD BOOKS")
	window.geometry('1600x1080')
	
	ai=PhotoImage(file="/sdcard/Project/pictures/gb.png")
	
	head=Label(window,height=50,width=900,text="ADD BOOKS",image=ai,bg='red',compound=LEFT,font=("Times New Roman", 12, "bold"))
	head.pack(pady=(40,30))
	
	af=Frame(window,height=1000,bg='lightpink')
	af.pack(fill=X,padx=20)
	
	al1=Label(af,text='BOOK NAME:',font=("Times New Roman", 7))
	al1.place(x=180,y=70)
	al2=Label(af,text='AUTHOR:',font=("Times New Roman", 7))
	al2.place(x=180,y=210)
	al3=Label(af,text='PAGE:',font=("Times New Roman", 7))
	al3.place(x=180,y=350)
	al4=Label(af,text='LANGUAGE:',font=("Times New Roman", 7))
	al4.place(x=180,y=500)
	
	global ae1
	ae1=Entry(af,width=25)
	ae1.place(x=550,y=70)
	ae1.insert(0, "   Enter book name")
	global ae2
	ae2=Entry(af,width=25)
	ae2.place(x=550,y=210)
	ae2.insert(0, "   Enter author's name")
	global ae3
	ae3=Entry(af,width=25)
	ae3.place(x=550,y=350)
	ae3.insert(0, "   Enter pages")
	global ae4
	ae4=Entry(af,width=25)
	ae4.place(x=550,y=500)
	ae4.insert(0, "   Enter language")
	
	ab=Button(af,text='Submit',command=addbook,height=20,width=30)
	ab.place(x=700,y=640)
	
	window.mainloop()
###########################################

		
#########ADD BOOKS TO DB#################
def addbook():
	n=ae1.get()
	a=ae2.get()
	s=ae3.get()
	l=ae4.get()
	if n and a and s and l !="":
		query="insert into 'books'(book_name,book_auth,book_page,book_lang) VALUES(?,?,?,?)"
		cur.execute(query,(n,a,s,l))
		cn.commit()
		messagebox.showinfo('Success','Inserted Successfully')
	else:
			messagebox.showinfo('Error','Check ur code')
			
	displaybook()
	STATS()													
#########################################


############ADDING MEMBERS#############
def AM():
	window1=Toplevel(r) 
	window1.title("ADD which MEMBER")
	window1.geometry('1400x745')
	window1.attributes('-fullscreen',False)
	
	ui=PhotoImage(file="/sdcard/Project/pictures/au.png")
	
	uhead=Label(window1,height=90,width=600,text="ADD MEMBER",image=ui,bg='cyan',compound=LEFT,font=("Times New Roman", 12, "bold"))
	uhead.pack(pady=(40,30))
	
	uf=Frame(window1,height=1000,bg='lightpink')
	uf.pack(fill=X,padx=20)
	
	ul1=Label(uf,text='NAME:',font=("Times New Roman", 7))
	ul1.place(x=180,y=100)
	ul2=Label(uf,text='CONTACT NO.:',font=("Times New Roman", 7))
	ul2.place(x=180,y=240)
	
	global ue1
	ue1=Entry(uf,width=25)
	ue1.place(x=550,y=100)
	ue1.insert(0, "   Enter user name")
	global ue2
	ue2=Entry(uf,width=25)
	ue2.place(x=550,y=240)
	ue2.insert(0, "   Enter Phone no.")
	
	ub=Button(uf,text='Submit',command=addmember)
	ub.place(x=600,y=370)
	
	window1.mainloop()
#########################################


#########ADD MEMBERS TO DB#############
def addmember():
	nm=ue1.get()
	ph=ue2.get()
	if nm and ph!="":
		query="insert into 'members'(member_name,member_phone) VALUES(?,?)"
		cur.execute(query,(nm,ph))
		cn.commit()
		messagebox.showinfo('Success','Added  Successfully')
	else:
			messagebox.showinfo('Error','Check ur Input')
#########################################


###########GIVING BOOKS(event)###########

	
def GB1(e):
	query="select * from books where book_id=?"
	bl=cur.execute(query,(id,)).fetchall()
	print(bl[0][5])

	if (bl[0][5]==0):
		window2=Toplevel(r)
		window2.title("GIVE BOOK")
		window2.geometry('1400x745')
		window2.attributes('-fullscreen',False)
		
		gi=PhotoImage(file="/sdcard/Project/pictures/ab.png")
		ghead=Label(window2,height=90,width=600,text="ISSUE BOOKS",image=gi,bg='cyan',compound=LEFT,font=("Times New Roman", 12, "bold"))
		
		ghead.pack(pady=(40,30))
		gf=Frame(window2,height=1000,bg='lightpink')
		gf.pack(fill=X,padx=20)
		
		gl1=Label(gf,text='BOOK NAME:',font=("Times New Roman", 7))
		gl1.place(x=180,y=100)
		gl2=Label(gf,text='MEMBER NAME:',font=("Times New Roman", 7))
		gl2.place(x=180,y=240)
		
		query1=cur.execute("select * from books").fetchall()
		booklist=[]
		for b in query1:
			booklist.append(str(b[0])+'-'+str(b[1]))
		print(booklist)
		
		global bookbox
		bookbox=ttk.Combobox(gf)
		bookbox['value']=booklist
		
		val1=lb1.get(lb1.curselection())
		vid=val1.split("-")[0]
		print(vid)
		bookbox.current(int(vid)-1)	
		bookbox.place(x=550,y=100)
		
		query2=cur.execute("select * from members").fetchall()
		memlist=[]
		for m in query2:
			memlist.append(str(m[0])+'-'+str(m[1]))
		print(memlist)
		
		global membox
		membox=ttk.Combobox(gf)
		membox['value']=memlist
		membox.place(x=550,y=240)
		
		gb=Button(gf,text='Submit yo yo',command=issuebook1)
		gb.place(x=600,y=370)
		
		window2.mainloop()
		
	elif(bl[0][5]==1):
		messagebox.showinfo("Error",'Book Unavailable')
	
#########################################

#########ISSUE BOOKS(DB(event))###########
def issuebook1():
	name=bookbox.get()
	member=membox.get()
	
	if name and member!=0:
		query="insert into borrow(bbook_id,bmem_id) values(?,?)"
		cur.execute(query,(name,member))
		cn.commit()
		messagebox.showinfo("Success","Book Issued")
		cur.execute("update books set book_status=? where book_id =?",(1,id))
		cn.commit()
	
	else:
		messagebox.showinfo("Failed!","Check Your Input")
		
	displaybook()
	STATS()				
#########################################


###########GIVING BOOK(btn)##############
def GB2():
	window3=Toplevel(r)
	window3.title("GIVE BOOK")
	window3.geometry('1400x745')
	
	gi=PhotoImage(file="/sdcard/Project/pictures/au.png")
	
	ghead=Label(window3,height=90,width=600,text="ISSUE BOOKS",image=gi,bg='cyan',compound=LEFT,font=("Times New Roman", 12, "bold"))
	ghead.pack(pady=(40,30))
	
	gf=Frame(window3,height=1000,bg='lightpink')
	gf.pack(fill=X,padx=20)
	
	gl1=Label(gf,text='BOOK NAME:',font=("Times New Roman", 7))
	gl1.place(x=180,y=100)
	gl2=Label(gf,text='MEMBER NAME:',font=("Times New Roman", 7))
	gl2.place(x=180,y=240)
	
	query1=cur.execute("select * from books where book_status=0").fetchall()
		
	booklist=[]
	for b in query1:
		booklist.append(str(b[0])+'-'+str(b[1]))
	print(booklist)
			
	global bookbox1
	bookbox1=ttk.Combobox(gf)
	bookbox1['value']=booklist
	bookbox1.place(x=550,y=100)
			
	query2=cur.execute("select * from members").fetchall()
			
	memlist=[]
	for m in query2:
		memlist.append(str(m[0])+'-'+str(m[1]))
	print(memlist)
		
	global membox1
	membox1=ttk.Combobox(gf)
	membox1['value']=memlist
	membox1.place(x=550,y=240)
		
	gb=Button(gf,text='Submit',command=issuebook2)
	gb.place(x=600,y=370)
	
	window3.mainloop()
#########################################

##########ISSUE BOOKS(DB(btn))###########
def issuebook2():
	name=bookbox1.get()
	member=membox1.get()
	
	print(name)
	id1=name.split("-")[0]
	print(id1)
	
	if name and member!=0:
		query="insert into borrow(bbook_id,bmem_id) values(?,?)"
		cur.execute(query,(name,member))
		cn.commit()
		messagebox.showinfo("Success","Book Issued")
		cur.execute("update books set book_status=? where book_id =?",(1,id1))
		cn.commit()
	
	else:
		messagebox.showinfo("Failed!","Check Your Input")
		
	displaybook()
	STATS()				
#########################################

##########RETURN BOOK(window)###########
def RB():
	window4=Toplevel(r)
	window4.title("GIVE BOOK")
	window4.geometry('1400x745')
	window4.attributes('-fullscreen',False)
	
	ri=PhotoImage(file="/sdcard/Project/pictures/rb.png")
	
	rhead=Label(window4,height=90,width=600,text=" RETURN BOOKS ",image=ri,bg='cyan',compound=LEFT,font=("Times New Roman", 12, "bold"))
	rhead.pack(pady=(40,30))
	
	rf=Frame(window4,height=1000,bg='lightpink')
	rf.pack(fill=X,padx=20)
	
	rl1=Label(rf,text='BOOK NAME:',font=("Times New Roman", 7))
	rl1.place(x=180,y=100)
	rl2=Label(rf,text='MEMBER NAME:',font=("Times New Roman", 7))
	rl2.place(x=180,y=240)
	
	query1=cur.execute("select * from books where book_status=1").fetchall()
	booklist=[]
	for b in query1:
		booklist.append(str(b[0])+'-'+str(b[1]))
	print(booklist)
	
	global bid
	global bookbox2
	bookbox2=ttk.Combobox(rf)
	bookbox2['value']=booklist
	bookbox2.place(x=550,y=100)
	
	def find(event):
		bid=bookbox2.get()
		print(bid)
		
		query2="select bmem_id from borrow where bbook_id=?"
		memb=cur.execute(query2,(bid,)).fetchall()
		
		global membox2
		memlist=[]
		memlist.append(memb[0][0])
		membox2=ttk.Combobox(rf)
		membox2['value']=memlist
		membox2.current(0)
		membox2.place(x=550,y=240)
	
	rb=Button(rf,text='Return',command=Return,width=10)
	rb.place(x=650,y=370)

	
	bookbox2.bind("<<ComboboxSelected>>", find)
	window4.mainloop()

#########################################


#############RETURN BOOK(DB)############
def Return():
	bk=bookbox2.get()
	mem=membox2.get()
	print(bk)
	id2=bk.split("-")[0]
	print(id2)
	
	if bk and mem!=0:
		query="delete from borrow where bbook_id=? "
		cur.execute(query,(bk,))
		cn.commit()
		cur.execute("update books set book_status=? where book_id =?",(0,id2))
		cn.commit()
		messagebox.showinfo("Success","Book Returned")
	
	else:
		messagebox.showinfo("Failed!","Check Your Input")
		
	displaybook()
	STATS()				
#########################################


#############DISPLAYING BOOKS##########
def displaybook():
	lb1.delete(0,'end')
	lb2.delete(0,'end')
	query='select * from books'
	count=0
	books= cur.execute(query).fetchall()
	for i in books:
	 	lb1.insert(count,str(i[0])+ '-'+str(i[1]))
	 	count+=1
##########################################

##########BOOK INFORMATION###########
def bookinfo(event):
	lb2.delete(0,'end')
	value=lb1.get(lb1.curselection())
	print(value)
	global id
	id=value.split("-")[0]
	print(id)
	query="select * from books where book_id=?"
	booklist=cur.execute(query,(id,)).fetchall()
	for b in booklist:
		lb2.insert(0, "Book Name : " +str(b[1]))
		lb2.insert(1, "Author : " +str(b[2]))
		lb2.insert(2, "Page : " +str(b[3]))
		lb2.insert(3, "Language : " +str(b[4]))
		
		if (b[5]==0):
			lb2.insert(4,"Status : Available")
		else:
			lb2.insert(4,"Status : Unavailable")
				
########################################


f=Frame(r,height=50,width=100,bg="lightblue",relief=SUNKEN,bd=5)
f.place(x=5,y=5)

i1=PhotoImage(file="D:/Work/Vscode/gb.png")
i2=PhotoImage(file="D:/Work/Vscode/ab.png")
i3=PhotoImage(file="D:/Work/Vscode/au.png")
i4=PhotoImage(file="D:/Work/Vscode/clr.png")
s=PhotoImage(file="D:/Work/Vscode/s.png")


b1=Button(f,text="GIVE BOOK",bd=5,relief=RAISED,image=i1,compound=LEFT,command=GB2)
b2=Button(f,text="ADD BOOK",bd=5,relief=RAISED,image=i2,compound=LEFT,command=AB)
b3=Button(f,text="ADD MEMBER",bd=5,relief=RAISED,image=i3,compound=LEFT,command=AM)
b4=Button(f,text="RETURN ",bd=5,image=i4,compound=LEFT,relief=RAISED,command=RB)

b1.pack(side=LEFT,pady=10,padx=3)
b2.pack(side=LEFT,pady=10,padx=3)
b3.pack(side=LEFT,padx=3)
b4.pack(side=LEFT,padx=(3,50),pady=10)


cf=LabelFrame(r,width=1440,height=815,bg="lightpink",bd=5)
cf.place(x=11,y=160)


tab=ttk.Notebook(cf)

lbm=Frame(tab)
stat=Frame(tab)
tab.add(lbm,text="Library")
tab.add(stat,text='Statistics')
tab.pack()

lb1=Listbox(lbm,width=24,height=13,bd=7,relief=SUNKEN,bg='#ffdde2',exportselection=False)
lb1.pack(side=LEFT)
sb=Scrollbar(lbm,orient=VERTICAL,command=lb1.yview)
sb.pack(side=LEFT,fill=Y)
lb1.config(yscrollcommand=sb.set)
lb2=Listbox(lbm,width=28,height=13,bd=7,relief=SUNKEN)
lb2.pack(side=LEFT)

l=LabelFrame(r,text="Search Box",bg="lightyellow",height=900,width=400,bd=10,relief=RAISED)
l.place(x=1460,y=150)

e1=Entry(l,bd=4,relief=SUNKEN,width=13)
e1.place(x=8,y=8)

############SEARCHING BOOKS#############
def search():
	lb1.delete(0,'end')
	lb2.delete(0,'end')
	count=0
	svalue=e1.get()
	query='select * from books where book_name like ?'
	sbooks=cur.execute(query,('%'+svalue+'%',)).fetchall()
	for s in sbooks:
		lb1.insert(count,str(s[0])+'-'+str(s[1]))
		count+=1
	e1.delete(0,'end')
##########################################


sb=Button(l,image=s,command=search)
sb.place(x=364,y=3)

l1=LabelFrame(l,text="Sort By:",bg="lightgreen",height=300,width=430)
l1.pack(side=LEFT,padx=3,pady=(83,3))


##############LISTING BOOKS###############
def listbook():
	sbook=one.get()
	query='select * from books where book_status=?'
	count=0
	if sbook==1:
		displaybook()
	elif sbook==2:
		lb1.delete(0,'end')
		lb2.delete(0,'end')
		library=cur.execute(query,(0,)).fetchall()
		for l in library:
			lb1.insert(count,str(l[0])+'-'+str(l[1]))
			count+=1
	else:
		lb1.delete(0,'end')
		borr=cur.execute(query,(1,)).fetchall()
		for b in borr:
			lb1.insert(count,str(b[0])+'-'+str(b[1]))
			count+=1		
##########################################

###############STATISTICS#################
bkcount=Label(stat,text='ALL BOOKS COUNT:')
bkcount.place(x=200,y=170)
lcount=Label(stat,text='ALL LIBRARY COUNT:')
lcount.place(x=200,y=260)
brcount=Label(stat,text='ALL BORROWED COUNT:')
brcount.place(x=200,y=350) 

def STATS():
	bk=cur.execute("select count(book_id) from books").fetchall()
	lib=cur.execute("select count(book_id) from books where book_status = 0").fetchall()
	brr=cur.execute("select count(book_id) from books where book_status = 1").fetchall()
	
	print(bk[0][0])
	print(lib[0][0])
	print(brr[0][0])
	bkcount.config(text='ALL BOOKS COUNT : '+str(bk[0][0]))
	lcount.config(text='ALL LIBRARY COUNT : '+str(lib[0][0]))
	brcount.config(text='ALL BORROWED COUNT : '+str(brr[0][0]))

STATS()
#########################################

one=IntVar()
r1=Radiobutton(l1,text="All Books",bg="lightgreen",var=one,value=1)
r2=Radiobutton(l1,text="In Library",bg="lightgreen",var=one,value=2)
r3=Radiobutton(l1,text="Borrowed",bg="lightgreen",var=one,value=3)
r1.place(y=11)
r2.place(y=69)
r3.place(y=130)

sort=Button(l1,text="sort",command=listbook)
sort.pack(pady=(200,5))

img=ImageTk.PhotoImage(Image.open("D:/Work/Vscode/lib.jpg"))
ll=Label(l1,height=300,width=430,text='मोर लाइब्रेरी',image=img,compound=BOTTOM)
ll.pack(pady=(20,5))


lb1.bind('<Double-Button-1>',GB1)
lb1.bind('<<ListboxSelect>>',bookinfo)
displaybook()
r.mainloop()