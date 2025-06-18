from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self. root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.var_user=StringVar()
        self.var_pass=StringVar()


        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Ridham Jasani\Documents\ridmy\Login\1.jpg")
        lbbg = Label(self.root,image=self.bg1)
        lbbg.place(x=0,y=0,relwidth=1,relheight=1)
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\Login\user.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbimg1= Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("Arial",21,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        username=lbl=Label(frame,text="Username",font=("Arial",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        self.txtuser=ttk.Entry(frame,textvariable=self.var_user,font=("Arial",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("Arial",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        self.txtpass=ttk.Entry(frame,textvariable=self.var_pass,font=("Arial",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        img2=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\Login\user.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbimg2 = Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\Login\lock.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbimg3 = Label(image=self.photoimage3,bg="black",borderwidth=0)
        lbimg3.place(x=650,y=393,width=25,height=25)

        lgnbtn = Button(frame,command=self.login,text="Login",font=("Arial",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        lgnbtn.place(x=110,y=300,width=120,height=35)

        regbtn = Button(frame,text="New User Register",command=self.registerwindow,font=("Arial",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        regbtn.place(x=15,y=350,width=160)  

        forbtn = Button(frame,text="Forgot Password",command=self.forgotwindow,font=("Arial",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forbtn.place(x=10,y=370,width=160)

    def registerwindow(self):
        self.newwindow=Toplevel(self.root)
        self.app=Register(self.newwindow)

    def pharwindow(self):
        self.newwindow=Toplevel(self.root)
        self.app=Pharmacy(self.newwindow)
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","ALL Field Required")
        elif self.txtuser.get()=="ridham" and self.txtpass.get()=="password":
            messagebox.showinfo("Success","Welcome Ridham")
            self.pharwindow()
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
            mycursor=conn.cursor()
            value=(self.var_user.get(),self.var_pass.get())
            mycursor.execute("select * from register where email=%s and password=%s",value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showinfo("Invalid","Invalid Username and Password")
            else:
                openmain=messagebox.askyesno("YesNo","Access only admin")
                if openmain>0:
                    self.pharwindow()
                else:
                    if not openmain:
                        return
            conn.commit()
            conn.close

    def resetpass(self):
        if self.combo.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.secans.get()=="":
            messagebox.showerror("Error","Please Enter Answer",parent=self.root2)
        elif self.newpass.get()=="":
            messagebox.showerror("Error","Please New Password",parent=self.root2)
        else :
            conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
            mycursor=conn.cursor()
            que=("select * from register where email=%s and securityQ=%s and securityA=%s")
            val=(self.txtuser.get(),self.combo.get(),self.secans.get(),)
            mycursor.execute(que,val)
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter correct Answer",parent=self.root2)
            else : 
                qury=("update register set password=%s where email=%s")
                vale=(self.newpass.get(),self.txtuser.get())
                mycursor.execute(qury,vale)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password has been Reset.",parent=self.root2)

    def forgotwindow(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)
            if row!=None:
                messagebox.showerror("Error","Please Enter Valid Username.")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("Arial",15,"bold"),fg="red",bg="white")
                l.place(x=0,y=20,relwidth=1) 

                security=Label(self.root2,text="Select Security Questions",font=("Arial",15,"bold"),fg="black",bg="white")
                security.place(x=50,y=80)
                self.combo=ttk.Combobox(self.root2,text="Contact",font=("Arial",15,"bold"),state="readonly")
                self.combo["values"]=("Select","Birth Place","Mother Name","Father Name")
                self.combo.place(x=50,y=120,width=250)
                self.combo.current(0)

                secans=Label(self.root2,text="Security Answer",font=("Arial",15,"bold"),fg="black",bg="white")
                secans.place(x=50,y=180)
                self.secans=ttk.Entry(self.root2,font=("Arial",15,"bold"))
                self.secans.place(x=50,y=220,width=250)

                newpass=Label(self.root2,text="New Password",font=("Arial",15,"bold"),fg="black",bg="white")
                newpass.place(x=50,y=260)
                self.newpass=ttk.Entry(self.root2,font=("Arial",15,"bold"))
                self.newpass.place(x=50,y=300,width=250)

                bt=Button(self.root2,text="Reset",command=self.resetpass,font=("Arial",15,"bold"),fg="white",bg="green")
                bt.place(x=140,y=360)


             




class Register:
    def __init__(self,root):
        self.root=root
        self. root.title("Register")
        self.root.geometry("1600x800+0+0")


        
        self.varfname=StringVar()
        self.varlname=StringVar()
        self.varcontact=StringVar()
        self.varemail=StringVar()
        self.varsecurity=StringVar()
        self.varsecurityans=StringVar()
        self.varpass=StringVar()
        self.varconpass=StringVar()
        

        self.bg2=ImageTk.PhotoImage(file=r"C:\Users\Ridham Jasani\Documents\ridmy\register\bg.jpg")
        lbbg1 = Label(self.root,image=self.bg2)
        lbbg1.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg3=ImageTk.PhotoImage(file=r"C:\Users\Ridham Jasani\Documents\ridmy\register\back.jpeg")
        lbbg2 = Label(self.root,image=self.bg3)
        lbbg2.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        registerlbl=Label(frame,text="Register Here",font=("Arial",20,"bold"),fg="darkgreen",bg="white")
        registerlbl.place(x=20,y=20)
       

        fname=Label(frame,text="First Name",font=("Arial",15,"bold"),fg="black",bg="white")
        fname.place(x=50,y=100)
        self.fnameentry=ttk.Entry(frame,textvariable=self.varfname,font=("Arial",15,"bold"))
        self.fnameentry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("Arial",15,"bold"),fg="black",bg="white")
        lname.place(x=370,y=100)
        self.lnameentry=ttk.Entry(frame,textvariable=self.varlname,font=("Arial",15,"bold"))
        self.lnameentry.place(x=370,y=130,width=250)
        
        contact=Label(frame,text="Contact",font=("Arial",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=180)
        self.contact=ttk.Entry(frame,textvariable=self.varcontact,font=("Arial",15,"bold"))
        self.contact.place(x=50,y=210,width=250)

        email=Label(frame,text="Email",font=("Arial",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=180)
        self.email=ttk.Entry(frame,textvariable=self.varemail,font=("Arial",15,"bold"))
        self.email.place(x=370,y=210,width=250)

        security=Label(frame,text="Select Security Questions",font=("Arial",15,"bold"),fg="black",bg="white")
        security.place(x=50,y=260)
        self.combo=ttk.Combobox(frame,text="Contact",textvariable=self.varsecurity,font=("Arial",15,"bold"),state="readonly")
        self.combo["values"]=("Select","Birth Place","Mother Name","Father Name")
        self.combo.place(x=50,y=290,width=250)
        self.combo.current(0)

        secans=Label(frame,text="Security Answer",font=("Arial",15,"bold"),fg="black",bg="white")
        secans.place(x=370,y=260)
        self.secans=ttk.Entry(frame,textvariable=self.varsecurityans,font=("Arial",15,"bold"))
        self.secans.place(x=370,y=290,width=250)

        password=Label(frame,text="Password",font=("Arial",15,"bold"),fg="black",bg="white")
        password.place(x=50,y=340)
        self.password=ttk.Entry(frame,textvariable=self.varpass,font=("Arial",15,"bold"))
        self.password.place(x=50,y=370,width=250)

        conpassword=Label(frame,text="Confirm Password",font=("Arial",15,"bold"),fg="black",bg="white")
        conpassword.place(x=370,y=340)
        self.conpassword=ttk.Entry(frame,textvariable=self.varconpass,font=("Arial",15,"bold"))
        self.conpassword.place(x=370,y=370,width=250)

        self.varcheck=IntVar()
        chkbtn = Checkbutton(frame,variable=self.varcheck,text="I agree terms & conditions",font=("Arial",11,"bold"),onvalue=1,offvalue=0)
        chkbtn.place(x=50,y=420)

        img4=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\register\register.jpg")
        img4=img4.resize((150,50),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        b1=Button(frame,image=self.photoimage4,command=self.regdata,borderwidth=0,cursor="hand2",font=("Arial",15,"bold"))
        b1.place(x=90,y=470,width=150,height=50)

        img5=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\register\login.jpeg")
        img5=img5.resize((150,50),Image.ANTIALIAS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        b2=Button(frame,image=self.photoimage5,borderwidth=0,cursor="hand2",font=("Arial",15,"bold"))
        b2.place(x=410,y=460,width=150,height=50)

    def regdata(self):
        if self.varfname.get()=="" or self.varemail.get()=="" or self.varsecurity.get()=="Select":
            messagebox.showerror("Error","All fields required.")
        elif self.varpass.get() != self.varconpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same.")
        elif self.varcheck.get() == 0 :
            messagebox.showerror("Error","Please agree our terms & conditions.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
            mycursor=conn.cursor()
            query=("select * from register where email =%s")
            value=(self.varemail.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Registered, please try another email.")
            else : 
                mycursor.execute("insert into register values (%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.varfname.get(),
                                                                                        self.varlname.get(),
                                                                                        self.varcontact.get(),
                                                                                        self.varemail.get(),
                                                                                        self.varsecurity.get(),
                                                                                        self.varsecurityans.get(),
                                                                                        self.varpass.get(),
                                                                                      ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully.")






class Pharmacy:

    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        lbltitle=Label(self.root,text="Pharmacy  Management  System",bd=15,relief=RIDGE,bg="white",fg="darkgreen",font=("Arial",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)

#--------------addMed Varibale
        self.ref_var=StringVar()
        self.addmed_var=StringVar()

#------------Main variable
        self.refren_var=StringVar()
        self.com_var=StringVar()
        self.type_var=StringVar()
        self.medname_var=StringVar()
        self.lot_var=StringVar()
        self.issue_var=StringVar()
        self.exp_var=StringVar()
        self.uses_var=StringVar()
        self.side_var=StringVar()
        self.warn_var=StringVar()
        self.dos_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()


        #Pharmacy Logo
        img6=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\pharma\pharmacy.jpg")
        img6=img6.resize((80,80),Image.ANTIALIAS)
        self.photoimage6=ImageTk.PhotoImage(img6)
        b6=Button(self.root,image=self.photoimage6,borderwidth=0)
        b6.place(x=70,y=21)


        # The data frame
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)


        # Left side frame - Medicine Info
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=21,text="Medicine Information",fg="darkgreen",font=("Arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        # Label and Entry Data Frame - LeftSide
        lblrefno=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Reference No.",fg="black",padx=2,pady=6)
        lblrefno.grid(row=0,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("select ref from pharmacy")
        row=mycursor.fetchall()
        
        

        refcombo=ttk.Combobox(DataFrameLeft,textvariable=self.refren_var,width=20,font=("Arial",12,"bold"),state="readonly")
        refcombo["values"]=(row)
        refcombo.grid(row=0,column=1)
        refcombo.current(0)

        lblcom=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Company Name :",fg="black",padx=2,pady=6)
        lblcom.grid(row=1,column=0,sticky=W)
        txtcom=Entry(DataFrameLeft,textvariable=self.com_var,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtcom.grid(row=1,column=1)
        
        lbltype=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Type of Medicine",fg="black",padx=2,pady=6)
        lbltype.grid(row=2,column=0,sticky=W)
        typecombo=ttk.Combobox(DataFrameLeft,textvariable=self.type_var,width=20,font=("Arial",12,"bold"),state="readonly")
        typecombo["values"]=("Tablet","Liquid","Capsules","Topical","Drops","Injection")
        typecombo.grid(row=2,column=1)
        typecombo.current(0)
        
        lblmed=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Medicine Name",fg="black",padx=2,pady=6)
        lblmed.grid(row=3,column=0,sticky=W)
        conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("select medname from pharmacy")
        meda=mycursor.fetchall()
        medcombo=ttk.Combobox(DataFrameLeft,textvariable=self.medname_var,width=20,font=("Arial",12,"bold"),state="readonly")
        medcombo["values"]=(meda)
        medcombo.grid(row=3,column=1)
        medcombo.current(0)
        
        lbllot=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Lot No. :",fg="black",padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        txtlot=Entry(DataFrameLeft,textvariable=self.lot_var,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtlot.grid(row=4,column=1)
        
        lblissue=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Issue Date :",fg="black",padx=2,pady=6)
        lblissue.grid(row=5,column=0,sticky=W)
        txtissue=Entry(DataFrameLeft,textvariable=self.issue_var,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtissue.grid(row=5,column=1)
        
        lblexp=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Expiry Date :",fg="black",padx=2,pady=6)
        lblexp.grid(row=6,column=0,sticky=W)
        txtexp=Entry(DataFrameLeft,textvariable=self.exp_var,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtexp.grid(row=6,column=1)
        
        lbluses=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Uses :",fg="black",padx=2,pady=6)
        lbluses.grid(row=7,column=0,sticky=W)
        txtuses=Entry(DataFrameLeft,textvariable=self.uses_var,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtuses.grid(row=7,column=1)
        
        lblside=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Side Effects :",fg="black",padx=2,pady=6)
        lblside.grid(row=8,column=0,sticky=W)
        txtside=Entry(DataFrameLeft,textvariable=self.side_var,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtside.grid(row=8,column=1)

        lblpre=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Precautions & Warning :",fg="black",padx=15,pady=6)
        lblpre.grid(row=0,column=3,sticky=W)
        txtpre=Entry(DataFrameLeft,textvariable=self.warn_var,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtpre.grid(row=0,column=4)

        lbldos=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Dosage :",fg="black",padx=15,pady=6)
        lbldos.grid(row=1,column=3,sticky=W)
        txtdos=Entry(DataFrameLeft,textvariable=self.dos_var,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtdos.grid(row=1,column=4)

        lblpri=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Price :",fg="black",padx=15,pady=6)
        lblpri.grid(row=2,column=3,sticky=W)
        txtpri=Entry(DataFrameLeft,textvariable=self.price_var,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtpri.grid(row=2,column=4)

        lblpro=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Product :",fg="black",padx=15,pady=6)
        lblpro.grid(row=3,column=3,sticky=W)
        txtpro=Entry(DataFrameLeft,textvariable=self.product_var,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtpro.grid(row=3,column=4)

        lblhome=Label(DataFrameLeft,font=("Arial",15,"bold"),text="Stay Home, Stay Safe",fg="red",padx=15,pady=6,width=36)
        lblhome.place(x=370,y=140)
        img7=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\pharma\capsules.jpeg")
        img7=img7.resize((150,135),Image.ANTIALIAS)
        self.photoimage7=ImageTk.PhotoImage(img7)
        b7=Button(self.root,image=self.photoimage7,borderwidth=0)
        b7.place(x=450,y=330)
        img8=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\pharma\injection.jpeg")
        img8=img8.resize((150,135),Image.ANTIALIAS)
        self.photoimage8=ImageTk.PhotoImage(img8)
        b8=Button(self.root,image=self.photoimage8,borderwidth=0)
        b8.place(x=595,y=330)
        img9=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\pharma\syrup.jpeg")
        img9=img9.resize((150,135),Image.ANTIALIAS)
        self.photoimage9=ImageTk.PhotoImage(img9)
        b9=Button(self.root,image=self.photoimage9,borderwidth=0)
        b9.place(x=745,y=330)
        

        # Rght Side Frame - Medicine ADD
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=21,text="Medicine ADD Department",fg="darkgreen",font=("Arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=550,height=350)

        imge=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\pharma\med.jpg")
        imge=imge.resize((200,75),Image.ANTIALIAS)
        self.photoimagee=ImageTk.PhotoImage(imge)
        be=Button(self.root,image=self.photoimagee,borderwidth=0)
        be.place(x=960,y=160)
        imge1=Image.open(r"C:\Users\Ridham Jasani\Documents\ridmy\pharma\med.jpg")
        imge1=imge1.resize((200,75),Image.ANTIALIAS)
        self.photoimagee1=ImageTk.PhotoImage(imge1)
        be1=Button(self.root,image=self.photoimagee1,borderwidth=0)
        be1.place(x=1160,y=160)

        lblrf=Label(DataFrameRight,font=("Arial",12,"bold"),text="Reference No. : ",pady=6)
        lblrf.place(x=0,y=80)
        textrf=Entry(DataFrameRight,textvariable=self.ref_var,font=("Arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=21)
        textrf.place(x=150,y=80)

        lblmedn=Label(DataFrameRight,font=("Arial",12,"bold"),text="Medicine Name :",pady=6)
        lblmedn.place(x=0,y=110)
        textmedn=Entry(DataFrameRight,textvariable=self.addmed_var,font=("Arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=21)
        textmedn.place(x=150,y=110)

        #Side Frame
        sideframe=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        sideframe.place(x=0,y=150,width=300,height=160)

        sfx=ttk.Scrollbar(sideframe,orient=HORIZONTAL)
        sfx.pack(side=BOTTOM,fill=X)
        sfy=ttk.Scrollbar(sideframe,orient=VERTICAL)
        sfy.pack(side=RIGHT,fill=Y)

        self.medicinetable=ttk.Treeview(sideframe,column=("ref","medname"),xscrollcommand=sfx.set,yscrollcommand=sfy.set)
        sfx.config(command=self.medicinetable.xview)
        sfy.config(command=self.medicinetable.yview)

        self.medicinetable.heading("ref",text="Reference No.")
        self.medicinetable.heading("medname",text="Medicine Name")
        self.medicinetable["show"]="headings"
        self.medicinetable.pack(fill=BOTH,expand=1)
        self.medicinetable.column("ref",width=100)
        self.medicinetable.column("medname",width=100)

        self.medicinetable.bind("<ButtonRelease-1>",self.medgetcursor)


        #Medicine add buttons
        downframe=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="black")
        downframe.place(x=350,y=150,width=136,height=160)
        btnAddmed=Button(downframe,text="ADD",command=self.addmedi,font=("Arial",12,"bold"),fg="white",bg="darkgreen",width=12,pady=4)
        btnAddmed.grid(row=0,column=0)
        btnUpmed=Button(downframe,text="UPDATE",command=self.Updatemed,font=("Arial",12,"bold"),fg="white",bg="blue",width=12,pady=4)
        btnUpmed.grid(row=1,column=0)
        btnDelmed=Button(downframe,text="DELETE",command=self.DeleteMed,font=("Arial",12,"bold"),fg="white",bg="red",width=12,pady=4)
        btnDelmed.grid(row=2,column=0)
        btnClearmed=Button(downframe,text="CLEAR",command=self.Clearmed,font=("Arial",12,"bold"),fg="white",bg="orange",width=12,pady=4)
        btnClearmed.grid(row=3,column=0)


        #framedetails
        # framedetails=Frame(self.root,bd=15,relief=RIDGE,)
        # framedetails.place(x=0,y=580,width=1500,height=210)
        
        #main table
        tableframe=Frame(self.root,bd=15,relief=RIDGE)
        tableframe.place(x=0,y=585,width=1530,height=210)
        
        sfx1=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        sfx1.pack(side=BOTTOM,fill=X)
        sfy1=ttk.Scrollbar(tableframe,orient=VERTICAL)
        sfy1.pack(side=RIGHT,fill=Y)

        self.pharmacytable=ttk.Treeview(tableframe,column=("ref","company","type","tabletname","lot","issuedate","expdate","uses","side","warn","dos","price","product"),xscrollcommand=sfx1.set,yscrollcommand=sfy1.set)
        sfx1.config(command=self.pharmacytable.xview)
        sfy1.config(command=self.pharmacytable.yview)
        self.pharmacytable["show"]="headings"
        self.pharmacytable.heading("ref",text="Reference No.")
        self.pharmacytable.heading("company",text="Company Name")
        self.pharmacytable.heading("type",text="Type of Medicine")
        self.pharmacytable.heading("tabletname",text="Medicine Name")
        self.pharmacytable.heading("lot",text="Lot No.")
        self.pharmacytable.heading("issuedate",text="Issue Date")
        self.pharmacytable.heading("expdate",text="Expiry Date")
        self.pharmacytable.heading("uses",text="Uses")
        self.pharmacytable.heading("side",text="Side Effects")
        self.pharmacytable.heading("warn",text="Warning")
        self.pharmacytable.heading("dos",text="Dosage")
        self.pharmacytable.heading("price",text="Price")
        self.pharmacytable.heading("product",text="Product Qts")
        self.pharmacytable.pack(fill=BOTH,expand=1)
        self.pharmacytable.column("ref",width=100)
        self.pharmacytable.column("company",width=100)
        self.pharmacytable.column("type",width=100)
        self.pharmacytable.column("tabletname",width=100)
        self.pharmacytable.column("lot",width=100)
        self.pharmacytable.column("issuedate",width=100)
        self.pharmacytable.column("expdate",width=100)
        self.pharmacytable.column("uses",width=100)
        self.pharmacytable.column("side",width=100)
        self.pharmacytable.column("warn",width=100)
        self.pharmacytable.column("dos",width=100)
        self.pharmacytable.column("price",width=100)
        self.pharmacytable.column("product",width=100)
        self.fetchmed()
        self.fetch_data()
        self.pharmacytable.bind("<ButtonRelease-1>",self.get_cursor)


        #----------------------------------
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)

        btnAddData=Button(ButtonFrame,command=self.add_data,text="Medicine ADD",font=("Arial",12,"bold"),fg="darkgreen",bg="white",width=14)
        btnAddData.grid(row=0,column=0)
        btnUpdateData=Button(ButtonFrame,command=self.Update_data,text="UPDATE",font=("Arial",12,"bold"),fg="darkgreen",bg="white",width=14)
        btnUpdateData.grid(row=0,column=1)
        btnDeleteData=Button(ButtonFrame,command=self.delete_data,text="DELETE",font=("Arial",12,"bold"),fg="red",bg="white",width=14)
        btnDeleteData.grid(row=0,column=2)
        btnRestData=Button(ButtonFrame,command=self.reset,text="RESET",font=("Arial",12,"bold"),fg="darkgreen",bg="white",width=14)
        btnRestData.grid(row=0,column=3)
        btnExitData=Button(ButtonFrame,text="EXIT",font=("Arial",12,"bold"),fg="darkgreen",bg="white",width=14)
        btnExitData.grid(row=0,column=4)

        lblSearch=Label(ButtonFrame,font=("Arial",12,"bold"),text="Search",padx=2,bg="white",fg="red",width=14)
        lblSearch.grid(row=0,column=5,sticky=W)

        self.search_var=StringVar()
        searchcombo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=13,font=("Arial",12,"bold"))
        searchcombo["values"]=("ref","Medname","lot")
        searchcombo.grid(row=0,column=6)
        searchcombo.current(0)

        self.searchTxt_var=StringVar()

        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("Arial",12,"bold"))
        txtSearch.grid(row=0,column=7)

        searchbtn=Button(ButtonFrame,command=self.search_data,text="SEARCH",font=("Arial",12,"bold"),fg="darkgreen",bg="white",width=14)
        searchbtn.grid(row=0,column=8)
        showAll=Button(ButtonFrame,command=self.fetch_data,text="SHOW ALL",font=("Arial",12,"bold"),fg="darkgreen",bg="white",width=14)
        showAll.grid(row=0,column=9)

   
#------------Add medicine
    def addmedi(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("insert into pharmacy(ref,medname) values (%s,%s)",(self.ref_var.get(),self.addmed_var.get()))
        conn.commit()
        self.fetchmed()
        conn.close()
        messagebox.showinfo("Success","Medicine Added.")

#----------------Fetch Update
    def fetchmed(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("select * from pharmacy")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.medicinetable.delete(*self.medicinetable.get_children())
            for i in rows:
                self.medicinetable.insert("",END,values=i)
            conn.commit()
        conn.close()


#----med get cursor
    def medgetcursor(self,evenet=""):
        cursorrow=self.medicinetable.focus()
        contents=self.medicinetable.item(cursorrow)
        row=contents["values"]
        self.ref_var.set(row[0])
        self.addmed_var.set(row[1])

    def Updatemed(self):
        if self.ref_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All fields are required.")
        else :
            conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
            mycursor=conn.cursor()
            mycursor.execute("update pharmacy set medname=%s where ref=%s;",(self.addmed_var.get(),self.ref_var.get()))
            conn.commit()
            self.fetchmed()
            conn.close()
            messagebox.showinfo("Success","Medicine Updated.")

    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("delete from pharmacy where ref=%s;",(self.ref_var.get(),))
        conn.commit()
        self.fetchmed()
        conn.close()
        messagebox.showinfo("Success","Medicine Deleted")
    
    def Clearmed(self):
        self.ref_var.set("")
        self.addmed_var.set("")


#----------------Main Table
    def add_data(self):
        if self.refren_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields required.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
            mycursor=conn.cursor()
            mycursor.execute("insert into pharma values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(
                                                                                                    self.refren_var.get(),
                                                                                                    self.com_var.get(),
                                                                                                    self.type_var.get(),
                                                                                                    self.medname_var.get(),
                                                                                                    self.lot_var.get(),
                                                                                                    self.issue_var.get(),
                                                                                                    self.exp_var.get(),
                                                                                                    self.uses_var.get(),
                                                                                                    self.side_var.get(),
                                                                                                    self.warn_var.get(),
                                                                                                    self.dos_var.get(),
                                                                                                    self.price_var.get(),
                                                                                                    self.product_var.get()
                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Data has been Inserted.")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("select * from pharma;")
        row=mycursor.fetchall()
        if len(row)!=0:
            self.pharmacytable.delete(*self.pharmacytable.get_children())
            for i in row:
                self.pharmacytable.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,ev=""):
        cursor_row=self.pharmacytable.focus()
        contentss=self.pharmacytable.item(cursor_row)
        row=contentss["values"]
        self.refren_var.set(row[0])
        self.com_var.set(row[1])
        self.type_var.set(row[2])
        self.medname_var.set(row[3])
        self.lot_var.set(row[4])
        self.issue_var.set(row[5])
        self.exp_var.set(row[6])
        self.uses_var.set(row[7])
        self.side_var.set(row[8])
        self.warn_var.set(row[9])
        self.dos_var.set(row[10])
        self.price_var.set(row[11])
        self.product_var.set(row[12])

    def Update_data(self):
        if self.refren_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required.")
        else :
            conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
            mycursor=conn.cursor()
            mycursor.execute("update pharma set com=%s,type=%s,medname=%s,lot=%s,issue=%s,exp=%s,uses=%s,side=%s,warn=%s,dos=%s,price=%s,product=%s where ref=%s",(
                                                                                                                                                                        self.com_var.get(),
                                                                                                                                                                        self.type_var.get(),
                                                                                                                                                                        self.medname_var.get(),
                                                                                                                                                                        self.lot_var.get(),
                                                                                                                                                                        self.issue_var.get(),
                                                                                                                                                                        self.exp_var.get(),
                                                                                                                                                                        self.uses_var.get(),
                                                                                                                                                                        self.side_var.get(),
                                                                                                                                                                        self.warn_var.get(),
                                                                                                                                                                        self.dos_var.get(),
                                                                                                                                                                        self.price_var.get(),
                                                                                                                                                                        self.product_var.get(),
                                                                                                                                                                        self.refren_var.get()
                                                                                                                                                                    ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record Updated.")


    def delete_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("delete from pharma where ref=%s;",(self.refren_var.get(),))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Medicine Deleted")
    

    def reset(self):
        # self.refren_var.set(""),
        self.com_var.set(""),
        # self.type_var.set(""),
        # self.medname_var.set(""),
        self.lot_var.set(""),
        self.issue_var.set(""),
        self.exp_var.set(""),
        self.uses_var.set(""),
        self.side_var.set(""),
        self.warn_var.set(""),
        self.dos_var.set(""),
        self.price_var.set(""),
        self.product_var.set("")

    def search_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="ridham",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("select * from pharma where "+str(self.search_var.get())+" LIKE '"+str(self.searchTxt_var.get())+"%'")

        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.pharmacytable.delete(*self.pharmacytable.get_children())
            for i in rows:
                self.pharmacytable.insert("",END,values=i)
            conn.commit()
        conn.close()






if __name__== "__main__":
    main()
