from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from Nifty_50 import Current_Stats_Nifty50
from Bank_Nifty import Current_Stats_Bank_Nifty
from Sensex import Current_Stats_Sensex
from Overview import Current_Stats_Overview

class IndianIndices:
    def __init__(self,root):
        self.root=root
        self.root.title("Indian Indices")
        self.root.geometry("1550x800+0+0")

        #=============Title============
        lbl_title=Label(self.root,text="Navnath Bhoskar Data Science Intern",font=("Times New Roman",20,"bold"),bg="white",fg="black",bd=3,relief=RIDGE)
        lbl_title.place(x=0,y=100,width=1550,height=40)

        img1=Image.open(r"C:\Users\navna\Music\Nava Services\top.png")#img1,banking_services,
        img1=img1.resize((1350,100),Image.ANTIALIAS)

        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1350,height=100) 
       
        img2=Image.open(r"C:\Users\navna\Music\Nava Services\banking_services.jpg")#img1,banking_services,
        img2=img2.resize((980,510),Image.ANTIALIAS)

        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=380,y=140,width=980,height=510)

        #=================main frame==================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=140,width=200,height=200)

        #======================menu====================
        lbl_menu=Label(main_frame,text="Mahindra Group", font=("times new roman",14,"bold"),bg="white",fg="black",bd=4,relief=RIDGE)#fg="royalblue"
        lbl_menu.place(x=0,y=0,width=195) #Portfolio Summary

        #=====================button frame====================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=1,y=30,width=190,height=160)#190

        cust_btn=Button(btn_frame,text="Nifty 50",width=22,command=self.nifty50_details,font=("times new roman",13,"bold"),bg="white",fg="darkorange",bd=0,cursor="hand1") # royalblue
        cust_btn.grid(row=0,column=0,pady=1)#Nifty50  command=self.nifty50_details

        room_btn=Button(btn_frame,text="Bank Nifty",width=22,command=self.bank_nifty_details,font=("times new roman",13,"bold"),bg="white",fg="blue",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)#command=self.bank_nifty_details

        detail_btn=Button(btn_frame,text="Sensex",width=22,command=self.sensex_details,font=("times new roman",13,"bold"),bg="white",fg="green",bd=0,cursor="hand1")
        detail_btn.grid(row=2,column=0,pady=1)#command=self.sensex_details,

        detail_btn=Button(btn_frame,text="Overview",width=22,command=self.overview_details,font=("times new roman",13,"bold"),bg="white",fg="black",bd=0,cursor="hand1")
        detail_btn.grid(row=3,column=0,pady=1)#command=self.sensex_details,

        logout_btn=Button(btn_frame,text="#Exit",command=self.logout,width=22,font=("times new roman",13,"bold"),bg="white",fg="red",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1) #Logout

        #================logo========================
        img3=Image.open(r"C:\Users\navna\Music\Nava Services\profile_vrt_raw.jpg")#unnamed.webp
        img3=img3.resize((175,175),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=200,y=160,width=175,height=175)

        img4=Image.open(r"C:\Users\navna\Music\Nava Services\flag.jpg")#reception taj
        img4=img4.resize((380,270),Image.ANTIALIAS)#420,300
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(self.root,image=self.photoimg4,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=365,width=380,height=270)

        img5=Image.open(r"C:\Users\navna\Music\Nava Services\yellow line.png")
        img5=img5.resize((1330,42),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(self.root,image=self.photoimg5,bd=0,relief=RIDGE)
        lblimg.place(x=20,y=647,width=1330,height=42)

    def nifty50_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Current_Stats_Nifty50(self.new_window)

    def bank_nifty_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Current_Stats_Bank_Nifty(self.new_window)

    def sensex_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Current_Stats_Sensex(self.new_window)

    def overview_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Current_Stats_Overview(self.new_window)

    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=IndianIndices(root)
    root.mainloop()