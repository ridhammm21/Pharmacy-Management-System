from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class Pharmacy:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        lbltitle=Label(self.root,text="Pharmacy  Management  System",bd=15,relief=RIDGE,bg="white",fg="darkgreen",font=("Arial",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)


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

        # Label and Entrt Data Frame - LeftSide
        lblrefno=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Reference No.",fg="black",padx=2,pady=6)
        lblrefno.grid(row=0,column=0,sticky=W)
        refcombo=ttk.Combobox(DataFrameLeft,width=20,font=("Arial",12,"bold"),state="readonly")
        refcombo["values"]=("Reference","Medcine Name","Lot Size")
        refcombo.grid(row=0,column=1)
        refcombo.current(0)

        lblcom=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Company Name :",fg="black",padx=2,pady=6)
        lblcom.grid(row=1,column=0,sticky=W)
        txtcom=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtcom.grid(row=1,column=1)
        
        lbltype=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Type of Medicine",fg="black",padx=2,pady=6)
        lbltype.grid(row=2,column=0,sticky=W)
        typecombo=ttk.Combobox(DataFrameLeft,width=20,font=("Arial",12,"bold"),state="readonly")
        typecombo["values"]=("Tablet","Liquid","Capsules","Topical","Drops","Injection")
        typecombo.grid(row=2,column=1)
        typecombo.current(0)
        
        lblmed=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Medicine Name",fg="black",padx=2,pady=6)
        lblmed.grid(row=3,column=0,sticky=W)
        medcombo=ttk.Combobox(DataFrameLeft,width=20,font=("Arial",12,"bold"),state="readonly")
        medcombo["values"]=("nice","best","nice")
        medcombo.grid(row=3,column=1)
        medcombo.current(0)
        
        lbllot=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Lot No. :",fg="black",padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        txtlot=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtlot.grid(row=4,column=1)
        
        lblissue=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Issue Date :",fg="black",padx=2,pady=6)
        lblissue.grid(row=5,column=0,sticky=W)
        txtissue=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtissue.grid(row=5,column=1)
        
        lblexp=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Expiry Date :",fg="black",padx=2,pady=6)
        lblexp.grid(row=6,column=0,sticky=W)
        txtexp=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtexp.grid(row=6,column=1)
        
        lbluses=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Uses :",fg="black",padx=2,pady=6)
        lbluses.grid(row=7,column=0,sticky=W)
        txtuses=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtuses.grid(row=7,column=1)
        
        lblside=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Side Effects :",fg="black",padx=2,pady=6)
        lblside.grid(row=8,column=0,sticky=W)
        txtside=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtside.grid(row=8,column=1)

        lblpre=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Precautions & Warning :",fg="black",padx=15,pady=6)
        lblpre.grid(row=0,column=3,sticky=W)
        txtpre=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtpre.grid(row=0,column=4)

        lbldos=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Dosage :",fg="black",padx=15,pady=6)
        lbldos.grid(row=1,column=3,sticky=W)
        txtdos=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtdos.grid(row=1,column=4)

        lblpri=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Price :",fg="black",padx=15,pady=6)
        lblpri.grid(row=2,column=3,sticky=W)
        txtpri=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
        txtpri.grid(row=2,column=4)

        lblpro=Label(DataFrameLeft,font=("Arial",12,"bold"),text="Product :",fg="black",padx=15,pady=6)
        lblpro.grid(row=3,column=3,sticky=W)
        txtpro=Entry(DataFrameLeft,bd=3,relief=RIDGE,width=21,font=("Arial",12,"bold"))
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
        textrf=Entry(DataFrameRight,font=("Arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=21)
        textrf.place(x=150,y=80)

        lblmedn=Label(DataFrameRight,font=("Arial",12,"bold"),text="Medicine Name :",pady=6)
        lblmedn.place(x=0,y=110)
        textmedn=Entry(DataFrameRight,font=("Arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=21)
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


        #Medicine add buttons
        downframe=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="black")
        downframe.place(x=350,y=150,width=136,height=160)
        btnAddmed=Button(downframe,text="ADD",font=("Arial",12,"bold"),fg="white",bg="darkgreen",width=12,pady=4)
        btnAddmed.grid(row=0,column=0)
        btnUpmed=Button(downframe,text="UPDATE",font=("Arial",12,"bold"),fg="white",bg="blue",width=12,pady=4)
        btnUpmed.grid(row=1,column=0)
        btnDelmed=Button(downframe,text="DELETE",font=("Arial",12,"bold"),fg="white",bg="red",width=12,pady=4)
        btnDelmed.grid(row=2,column=0)
        btnClearmed=Button(downframe,text="CLEAR",font=("Arial",12,"bold"),fg="white",bg="orange",width=12,pady=4)
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


        #----------------------------------
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)

        btnAddData=Button(ButtonFrame,text="Medicine ADD",font=("Arial",12,"bold"),fg="darkgreen",bg="white",width=14)
        btnAddData.grid(row=0,column=0)
        btnUpdateData=Button(ButtonFrame,text="UPDATE",font=("Arial",12,"bold"),fg="darkgreen",bg="white",width=14)
        btnUpdateData.grid(row=0,column=1)
        btnDeleteData=Button(ButtonFrame,text="DELETE",font=("Arial",12,"bold"),fg="red",bg="white",width=14)
        btnDeleteData.grid(row=0,column=2)
        btnRestData=Button(ButtonFrame,text="RESET",font=("Arial",12,"bold"),fg="darkgreen",bg="white",width=14)
        btnRestData.grid(row=0,column=3)
        btnExitData=Button(ButtonFrame,text="EXIT",font=("Arial",12,"bold"),fg="darkgreen",bg="white",width=14)
        btnExitData.grid(row=0,column=4)

        lblSearch=Label(ButtonFrame,font=("Arial",12,"bold"),text="Search",padx=2,bg="white",fg="red",width=14)
        lblSearch.grid(row=0,column=5,sticky=W)

        searchcombo=ttk.Combobox(ButtonFrame,width=13,font=("Arial",12,"bold"))
        searchcombo["values"]=("Reference","Medcine Name","Lot Size")
        searchcombo.grid(row=0,column=6)
        searchcombo.current(0)

        txtSearch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=12,font=("Arial",12,"bold"))
        txtSearch.grid(row=0,column=7)

        searchbtn=Button(ButtonFrame,text="SEARCH",font=("Arial",12,"bold"),fg="darkgreen",bg="white",width=14)
        searchbtn.grid(row=0,column=8)
        showAll=Button(ButtonFrame,text="SHOW ALL",font=("Arial",12,"bold"),fg="darkgreen",bg="white",width=14)
        showAll.grid(row=0,column=9)


        


if __name__ == "__main__":
    root=Tk()
    obj=Pharmacy(root)
    root.mainloop()