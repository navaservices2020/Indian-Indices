from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from groww import Current_Holdings_Groww
from paytm import Current_Holdings_Paytm
from zerodha import Current_Holdings_Zerodha

class NavaServices:
    def __init__(self,root):
        self.root=root
        self.root.title("navaservices2020@gmail.com")
        self.root.geometry("1550x800+0+0")

        #=============Title============
        lbl_title=Label(self.root,text="Welcome to Nava Services",font=("times new roman",30,"bold"),bg="white",fg="black",bd=3,relief=RIDGE)
        lbl_title.place(x=0,y=160,width=1550,height=40)

        img1=Image.open(r"C:\Users\navna\Music\Nava Services\top.png")#img1,banking_services,
        img1=img1.resize((1350,160),Image.ANTIALIAS)

        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1350,height=160)
       
        img2=Image.open(r"C:\Users\navna\Music\Nava Services\unnamed.png")#img1,banking_services,
        img2=img2.resize((931,447),Image.ANTIALIAS)

        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=420,y=200,width=931,height=447)

        #=================main frame==================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=200,width=225,height=170)

        #======================menu====================
        lbl_menu=Label(main_frame,text="Follow us on...", font=("times new roman",14,"bold"),bg="white",fg="black",bd=4,relief=RIDGE)#fg="royalblue"
        lbl_menu.place(x=0,y=0,width=220) #Portfolio Summary

        #=====================button frame====================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=30,width=220,height=130)#190

        cust_btn=Button(btn_frame,text="Groww",width=22,command=self.groww_details,font=("times new roman",13,"bold"),bg="white",fg="darkorange",bd=0,cursor="hand1") # royalblue
        cust_btn.grid(row=0,column=0,pady=1)#Groww

        room_btn=Button(btn_frame,text="Paytm",width=22,command=self.paytm_details,font=("times new roman",13,"bold"),bg="white",fg="blue",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)#Paytm

        detail_btn=Button(btn_frame,text="Zerodha",width=22,command=self.zerodha_details,font=("times new roman",13,"bold"),bg="white",fg="green",bd=0,cursor="hand1")
        detail_btn.grid(row=2,column=0,pady=1)#Zerodha

        logout_btn=Button(btn_frame,text="#75th_Independence_Day",command=self.logout,width=22,font=("times new roman",13,"bold"),bg="white",fg="royalblue",bd=0,cursor="hand1")
        logout_btn.grid(row=3,column=0,pady=1) #Logout

        #================logo========================
        img3=Image.open(r"C:\Users\navna\Music\Nava Services\profile_vrt_raw.jpg")#unnamed.webp
        img3=img3.resize((190,180),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=230,y=200,width=190,height=180)

        img4=Image.open(r"C:\Users\navna\Music\Nava Services\flag.jpg")#reception taj
        img4=img4.resize((420,280),Image.ANTIALIAS)#420,300
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(self.root,image=self.photoimg4,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=375,width=420,height=280)

        img5=Image.open(r"C:\Users\navna\Music\Nava Services\yellow line.png")
        img5=img5.resize((1330,42),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(self.root,image=self.photoimg5,bd=0,relief=RIDGE)
        lblimg.place(x=20,y=647,width=1330,height=42)

    def groww_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Current_Holdings_Groww(self.new_window)

    def paytm_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Current_Holdings_Paytm(self.new_window)

    def zerodha_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Current_Holdings_Zerodha(self.new_window)

    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=NavaServices(root)
    root.mainloop()

        