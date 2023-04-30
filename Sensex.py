from optparse import Values
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Current_Stats_Sensex:
    def __init__(self,root):
        self.root=root
        self.root.title("Sensex")
        self.root.geometry("1550x800+0+0")#1100x420+425+230

        #================Variables==================
       
        self.var_serial_id=IntVar()
        self.var_date=StringVar() 
        self.var_day_name=StringVar() 
        self.var_open_price=DoubleVar()
        self.var_high_price=DoubleVar() 
        self.var_low_price=DoubleVar() 
        self.var_close_price=DoubleVar() 
        self.var_change_points=DoubleVar() 
        self.var_change_prct=DoubleVar() 
        self.var_volume=IntVar()

        #=================Title======================
        lbl_title=Label(self.root,text="BSE Sensex Historical Data", font=("times new roman",16,"bold"),bg="white",fg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1550,height=40) # width=1295

        #================lebel frame=================== 
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Overview Details",font=("times new roman",12,"bold"),padx=2) 
        labelframeleft.place(x=5,y=40,width=380,height=380)#width=400 y=35 height=440 
        
        #===============lables and entries================= #
        #serial_id No 
        lbl_serial_id_ref=Label(labelframeleft,text="Serial ID:-",font=("arial",11),padx=2,pady=6) 
        lbl_serial_id_ref.grid(row=0,column=0,sticky=W) 
        txtref=ttk.Entry(labelframeleft,width=25,textvariable=self.var_serial_id,font=("arial",11,"bold")) 
        txtref.grid(row=0,column=1) 
        
        #Date 
        lbl_date_ref=Label(labelframeleft,text="Date:-",font=("arial",11),padx=2,pady=6) 
        lbl_date_ref.grid(row=1,column=0,sticky=W) 
        
        txtname=ttk.Entry(labelframeleft,width=25,textvariable=self.var_date,font=("arial",11,"bold")) 
        txtname.grid(row=1,column=1) 
        
        #Day Name 
        lbl_day_ref=Label(labelframeleft,text="Day:-",font=("arial",11),padx=2,pady=6) 
        lbl_day_ref.grid(row=2,column=0,sticky=W) 
        
        combo_day_name=ttk.Combobox(labelframeleft,textvariable=self.var_day_name,font=("arial",11),width=23,state="readonly") #("arial",12,"bold") 
        combo_day_name["value"]=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday") # textvariable=self.var_batsman_name, 
        combo_day_name.current(0) 
        combo_day_name.grid(row=2,column=1) 
        
        #Open Price 
        lbl_oprice_ref=Label(labelframeleft,text="Open Price:-",font=("arial",11),padx=2,pady=6) 
        lbl_oprice_ref.grid(row=3,column=0,sticky=W) 
        
        txtop=ttk.Entry(labelframeleft,width=25,textvariable=self.var_open_price,font=("arial",11,"bold")) 
        txtop.grid(row=3,column=1)#textvariable=self.var_mobile, 
        
        #Today's High 
        lbl_hprice_ref=Label(labelframeleft,text="Today's High:-",font=("arial",11),padx=2,pady=6) 
        lbl_hprice_ref.grid(row=4,column=0,sticky=W) 

        txthp=ttk.Entry(labelframeleft,width=25,textvariable=self.var_high_price,font=("arial",11,"bold")) 
        txthp.grid(row=4,column=1) 
      
        #Today's Low 
        lbl_lprice_ref=Label(labelframeleft,text="Today's Low:-",font=("arial",11),padx=2,pady=6) 
        lbl_lprice_ref.grid(row=5,column=0,sticky=W) 
        
        txtlp=ttk.Entry(labelframeleft,width=25,textvariable=self.var_low_price,font=("arial",11,"bold")) 
        txtlp.grid(row=5,column=1) 
        
        #Close Price 
        lbl_cprice_ref=Label(labelframeleft,text="Close Price:-",font=("arial",11),padx=2,pady=6) 
        lbl_cprice_ref.grid(row=6,column=0,sticky=W) 

        txtcp=ttk.Entry(labelframeleft,width=25,textvariable=self.var_close_price,font=("arial",11,"bold")) 
        txtcp.grid(row=6,column=1,sticky=W) 
        
        #Day Change 
        lbl_day_change=Label(labelframeleft,text="Day Change:-",font=("arial",11),padx=2,pady=6) 
        lbl_day_change.grid(row=7,column=0,sticky=W) 

        txt_day_change=ttk.Entry(labelframeleft,width=25,textvariable=self.var_change_points,font=("arial",11,"bold")) 
        txt_day_change.grid(row=7,column=1,sticky=W) 
        
        #Change Percentage 
        lbl_change_percent=Label(labelframeleft,text="Change %:-",font=("arial",11),padx=2,pady=6) 
        lbl_change_percent.grid(row=8,column=0,sticky=W)

        txt_change_percent=ttk.Entry(labelframeleft,width=25,textvariable=self.var_change_prct,font=("arial",11,"bold")) 
        txt_change_percent.grid(row=8,column=1,sticky=W)

        #=====================btn==============================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=30,y=310,width=290,height=40) #height=25

        btn_add=Button(btn_frame,text="Insert",command=self.insert_records,font=("arial",11),bg="green",fg="white",width=9) #,"bold"
        btn_add.grid(row=0,column=0,padx=1)#command=self.add_stocks,

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",11),bg="royalblue",fg="white",width=9) #,"bold"
        btn_update.grid(row=0,column=1,padx=1)#command=self.update,

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11),bg="dark orange",fg="white",width=9) #,"bold"
        btn_reset.grid(row=0,column=2,padx=1)#command=self.reset,

        #====================right side img=============================
        img1=Image.open(r"C:\Users\navna\Music\Nava Services\fedral.jpg")
        img1=img1.resize((770,431),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lblimg.place(x=390,y=320,width=770,height=431)

        img2=Image.open(r"C:\Users\navna\Music\Nava Services\profile_vrt_raw.jpg")
        img2=img2.resize((190,190),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=420,width=190,height=190)

        img3=Image.open(r"C:\Users\navna\Music\Nava Services\securitycheck.png")
        img3=img3.resize((96,96),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=190,y=420,width=96,height=96)
        
        #=================holdings table frame============================

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Sensex Historical Data And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_frame.place(x=390,y=40,width=960,height=280) 

        labelSearchBy=Label(Table_frame,text="Search By:",bg="royalblue",fg="black",font=("arial",10,"bold"))
        labelSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",10,"bold"),width=15,state="readonly")
        combo_search["value"]=("Date","Day")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_frame,width=35,textvariable=self.txt_search,font=("arial",10,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)#textvariable=self.txt_search,

        btn_search=Button(Table_frame,text="Search",command=self.search,font=("arial",10,"bold"),bg="green",fg="white",width=20)
        btn_search.grid(row=0,column=3,padx=1)#command=self.search,

        btn_Showall=Button(Table_frame,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),bg="dark orange",fg="white",width=20)
        btn_Showall.grid(row=0,column=4,padx=1)#command=self.fetch_data,

        btn_Showall=Button(Table_frame,text="Total Investment",command=self.total,font=("arial",10,"bold"),bg="royalblue",fg="white",width=18)
        btn_Showall.grid(row=0,column=5,padx=1)#command=self.total,

        
        #=================show data table=============== 
        detail_table=Frame(Table_frame,bd=2,relief=RIDGE) 
        detail_table.place(x=0,y=30,width=950,height=230) #width=860 

        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL) 
        
        self.Record_Details_Table=ttk.Treeview(detail_table,column=("serial_id","date","day","open","high","low","close","day_change","change_prct"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        
        scroll_x.pack(side=BOTTOM,fill=X) 
        scroll_y.pack(side=RIGHT,fill=Y) 

        scroll_x.config(command=self.Record_Details_Table.xview) 
        scroll_y.config(command=self.Record_Details_Table.yview) 
        
        self.Record_Details_Table.heading("serial_id",text="Serial No") 
        self.Record_Details_Table.heading("date",text="Date") 
        self.Record_Details_Table.heading("day",text="Day") 
        self.Record_Details_Table.heading("open",text="Open") 
        self.Record_Details_Table.heading("high",text="High") 
        self.Record_Details_Table.heading("low",text="Low") 
        self.Record_Details_Table.heading("close",text="Close") 
        self.Record_Details_Table.heading("day_change",text="Change") 
        self.Record_Details_Table.heading("change_prct",text="Change Percentage") 
      
        
        self.Record_Details_Table["show"]="headings" 
        
        self.Record_Details_Table.column("serial_id",width=80) 
        self.Record_Details_Table.column("date",width=80) 
        self.Record_Details_Table.column("day",width=80) 
        self.Record_Details_Table.column("open",width=80) 
        self.Record_Details_Table.column("high",width=80) 
        self.Record_Details_Table.column("low",width=80) 
        self.Record_Details_Table.column("close",width=80) 
        self.Record_Details_Table.column("day_change",width=80) 
        self.Record_Details_Table.column("change_prct",width=80) 
        self.Record_Details_Table.pack(fill=BOTH,expand=1) 
        self.Record_Details_Table.bind("<ButtonRelease-1>",self.get_cursor) 
        
        self.fetch_data()

######
    def insert_records(self): #self.insert_records 
        if self.var_date.get()=="" or self.var_day_name.get()=="": 
            messagebox.showerror("Error","All fields are required",parent=self.root) 
            
        else: 
            try: 
                conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="Indian_Indices") 
                my_cursor=conn.cursor() 
                my_cursor.execute("insert into sensex(date, day, open, high, low, close, day_change, change_prct) values(%s,%s,%s,%s,%s,%s,%s,%s)",( 
                    self.var_date.get(), 
                    self.var_day_name.get(), 
                    self.var_open_price.get(), 
                    self.var_high_price.get(), 
                    self.var_low_price.get(), 
                    self.var_close_price.get(), 
                    self.var_change_points.get(), 
                    self.var_change_prct.get() 
                    ) ) 

                conn.commit() 
                self.fetch_data() 
                conn.close() 
                messagebox.showinfo("Success","Record has been added",parent=self.root) 
                
            except Exception as es: messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="Indian_Indices")
        my_cursor=conn.cursor()
        my_cursor.execute("select Sensex_id,Date,Day,Open,High,Low,Close,Day_Change,Change_Prct from sensex")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Record_Details_Table.delete(*self.Record_Details_Table.get_children())
            for i in rows:
                self.Record_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Record_Details_Table.focus()
        content=self.Record_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_serial_id.set(row[0]),
        self.var_date.set(row[1]),
        self.var_day_name.set(row[2]),
        self.var_open_price.set(row[3]),
        self.var_high_price.set(row[4]),
        self.var_low_price.set(row[5]),
        self.var_close_price.set(row[6]),
        self.var_change_points.set(row[7]),
        self.var_change_prct.set(row[8])


    def update(self):
        if self.var_serial_id.get()=="":
            messagebox.showerror("Error","Please enter serial number",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="Indian_Indices")
            my_cursor=conn.cursor()
            my_cursor.execute("update sensex set Sensex_id=%s,Day=%s where Date=%s",(
                                                                                                                    self.var_serial_id.get(),
                                                                                                                    self.var_day_name.get(),
                                                                                                                    self.var_date.get()
                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Holding details has been updated successfully",parent=self.root)

    def Sell(self):
        Sell=messagebox.askyesno("navaservices2020@gmail.com","Do you want sell this stock",parent=self.root)
        if Sell>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="Indian_Indices")
            my_cursor=conn.cursor()
            query="delete from nifty_50 where Serial=%s"
            value=(self.var_serial_no.get(),)
            my_cursor.execute(query,value)
        else:
            if not Sell:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    
    def reset(self):
        self.var_serial_id.set(""),
        self.var_date.set(""),
        self.var_day_name.set(""),
        self.var_open_price.set(""),
        self.var_high_price.set("")
        self.var_low_price.set("")
        self.var_close_price.set(""),
        self.var_change_points.set(""),
        self.var_change_prct.set("")
    
    

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="Indian_Indices")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from sensex where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Record_Details_Table.delete(*self.Record_Details_Table.get_children())
            for i in rows:
                self.Record_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def total(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="MySQL$2022",database="Indian_Indices")
        my_cursor=conn.cursor()
        my_cursor.execute("select round(SUM(Investment),2) from groww")
        row=my_cursor.fetchone()
        self.var_total_investment.set(row)
        #(round(sum(column)),2)


if __name__ == "__main__":
    root=Tk()
    obj=Current_Stats_Sensex(root)
    root.mainloop()