from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql



root=Tk()

class login:
    def login_open():
        global portal_screen
        portal_screen = Toplevel(self.root)
        portal_screen.title("Register")
        portal_screen.geometry("1199x600+100+50")
        portal_screen.configure(bg='purple')
        

        open_bg=PhotoImage(file="d:/css/welcome.png")
        open_bg_image=Label(portal_screen,image=open_bg)
        open_bg_image.place(x=250,y=100)

    def login_validate(self):
        if self.txt_user.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="student"
                    )

                cur = con.cursor()
                cur.execute("select * from signup_detail where email=%s and Password=%s",(self.txt_user.get(), self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("Welcome","Login Succesful",parent=self.root)
                    


                    
                #print(row)
            except Exception as es:
                 messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)

   
            

    def signup_user(self):
        global register_screen
        self.register_screen = Toplevel(self.root)
        self.register_screen.title("Register")
        self.register_screen.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        

        self.signup_bg=PhotoImage(file="d:/css/red.png")
        self.signup_bg_image=Label(self.register_screen,image=self.signup_bg)
        self.signup_bg_image.place(x=0,y=0)

        frame1=Frame(self.register_screen,bg="white")
        frame1.place(x=480,y=0,width=700,height=900)
        title=Label(frame1,text="Signup Here",font=("Times new roman",20,"bold"),bg="white",fg="#008080")
        title.place(x=50,y=20)
        #-----------------r1
         
        username=Label(frame1,text="Username",font=("Times new roman",15,"bold"),bg="white",fg="gray")
        username.place(x=50,y=100)

        self.txt_un=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_un.place(x=50,y=130,width=250)

        email=Label(frame1,text="Email",font=("Times new roman",15,"bold"),bg="white",fg="gray")
        email.place(x=370,y=100)

        self.txt_em=Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_em.place(x=370,y=130,width=250)
        #----------r2
        contact=Label(frame1,text="Contact No.",font=("Times new roman",15,"bold"),bg="white",fg="gray")
        contact.place(x=50,y=170)

        self.txt_cn=Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_cn.place(x=50,y=200,width=250)

        city=Label(frame1,text="City",font=("Times new roman",15,"bold"),bg="white",fg="gray")
        city.place(x=370,y=170)

        self.txt_ct=Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_ct.place(x=370,y=200,width=250)

        #-----------------------r3

        question=Label(frame1,text="Security Question",font=("Times new roman",15,"bold"),bg="white",fg="gray")
        question.place(x=50,y=240)

        self.txt_q=Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_q.place(x=50,y=270,width=250)

        self.cmb_ques=ttk.Combobox(frame1, font=("times new roman",13))
        self.cmb_ques['values']=("Select", "Your First Pet Name","Your Birth Place","Your best Friend")
        self.cmb_ques.place(x=50,y=270,width=250)
        self.cmb_ques.current(0)
        
        answer=Label(frame1,text="Answer",font=("Times new roman",15,"bold"),bg="white",fg="gray")
        answer.place(x=370,y=240)

        self.txt_ans=Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_ans.place(x=370,y=270,width=250)

         #----------r4
        password=Label(frame1,text="Password",font=("Times new roman",15,"bold"),bg="white",fg="gray")
        password.place(x=50,y=310)

        self.txt_pas=Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_pas.place(x=50,y=340,width=250)

        con_pasw=Label(frame1,text="Conform Password",font=("Times new roman",15,"bold"),bg="white",fg="gray")
        con_pasw.place(x=370,y=310)

        self.txt_conpasw=Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_conpasw.place(x=370,y=340,width=250)

        #--------------------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Condition",variable=self.var_chk,onvalue=1,offvalue=0, bg="white",font=("Times new roman",12))
        chk.place(x=50,y=380)

        register_btn=Button(frame1, command=self.register_data,cursor="hand2",bd=0,text="Submit",bg="red",fg="white",font=("Times new roman",20,"bold"))
        register_btn.place(x=50,y=420)
        
    def register_data(self):
        if self.txt_un.get()==""or self.txt_em.get()=="" or self.txt_cn.get()=="" or  self.txt_ct.get()=="" or self.txt_ans.get()=="" or self.cmb_ques.get()=="select" or self.txt_pas.get()=="" or self.txt_conpasw.get()=="":
            messagebox.showerror("Error", "All Fields Are Required",parent=self.register_screen)
        elif self.txt_pas.get()!=self.txt_conpasw.get():
            messagebox.showerror("Error", "Password & Conform Password should be same",parent=self.register_screen)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please Agree Our Term & Condition",parent=self.register_screen)

        else:
            try:
                con = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="student"
                )

                cur = con.cursor()
                cur.execute("insert into signup_detail(username,email,contact,city,question,answer,password) values (%s,%s,%s,%s,%s,%s,%s)",
                       (self.txt_un.get(),
                        self.txt_em.get(),
                        self.txt_cn.get(),
                        self.txt_ct.get(),
                        self.txt_ans.get(),
                        self.cmb_ques.get(),
                        self.txt_pas.get()
                        

                       ))
                
                
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Signup Completed",parent=self.register_screen)


            except Exception as es:
                    messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.register_screen)

                


        
        
        


        
    def __init__(self,root):
        self.root=root
        self.root.title("login system")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        
        self.bg=PhotoImage(file="d:/css/myuy.png")
        self.bg_image=Label(self.root,image=self.bg)
        self.bg_image.place(x=0,y=0)

        Frame_login=Frame(self.root,bg="#e75480")
        Frame_login.place(x=150,y=150,height=340,width=500)

        title=Label(Frame_login,text="Login",font=("Impact",35,"bold"),fg="white",bg="#e75480")
        title.place(x=90,y=30)

        desc=Label(Frame_login,text="Student Login Here",font=("Goudy old style",15,"bold"),fg="white",bg="#e75480")
        desc.place(x=90,y=100)

        lbl_user=Label(Frame_login,text="Email Address",font=("Goudy old style",15,"bold"),fg="blue",bg="#e75480")
        lbl_user.place(x=90,y=140)

        self.txt_user=Entry(Frame_login, font=("times new roman",15),bg="white")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="blue",bg="#e75480")
        lbl_pass.place(x=90,y=210)

        self.txt_pass=Entry(Frame_login, font=("times new roman",15),bg="white")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget=Button(Frame_login,text="Forget Password?",cursor="hand2",bg="#e75480",bd=0,fg="blue",font=("Times new roman",12))
        forget.place(x=90,y=280)

        Login_btn=Button(self.root,command=self.login_validate,cursor="hand2",text="Login",bg="#e75480",fg="white",font=("Times new roman",20,"bold"))
        Login_btn.place(x=200,y=470,width=180,height=40)

        Signup_btn=Button(self.root,command=self.signup_user,cursor="hand2",text="Signup",bg="#e75480",fg="white",font=("Times new roman",20,"bold"))
        Signup_btn.place(x=400,y=470,width=180,height=40)

   

obj=login(root)
root.mainloop()
