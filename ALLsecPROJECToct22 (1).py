from tkinter import *
from tkinter import messagebox
import ast
import pymysql

m=Tk()
m.title("ALLSECCOMPANYPORTAL")
m.geometry("925x500")
m.configure(bg="lightskyblue")
p1=PhotoImage(file="ALLSEC1.png")
m.iconphoto(False,p1)


def signin():
    username=user.get()
    password=code.get()

    connection = pymysql.connect(host="localhost", user="root", passwd="hari1308", database="hari")
    cursor = connection.cursor()

    query = "SELECT * FROM portal WHERE username=%s AND password=%s"

    cursor.execute(query, (username, password))

    result = cursor.fetchall()

    if result:
        messagebox.showinfo("Success", "Login completed")
        screen=Toplevel(m)
        screen.title("ALLSECCOMPANYPORTAL")
        screen.geometry('925x500')
        screen.config(bg="lightskyblue")
        p1=PhotoImage(file="ALLSEC1.png")
        screen.iconphoto(False,p1)

        Label(screen,text='Welcome HARI!!!',font=('arial',70)).pack(expand=True)

        screen.mainloop()
    else:
        messagebox.showerror("Authentication failed", "Login Failed")



######################################################
def signup_command():
    window=Toplevel(m)
    window.title("ALLSECCOMPANYPORTAL")
    window.geometry('925x500')
    window.configure(bg='lightskyblue')
    p1=PhotoImage(file="ALLSEC1.png")
    window.iconphoto(False,p1)

    
    def signup():
        username=user.get()
        password=code.get()
        confirm_password=confirm_code.get()

        connection = pymysql.connect(host="localhost", user="root", passwd="hari1308", database="hari")
        cursor = connection.cursor()

        query = "INSERT INTO portal(username, password) VALUES (%s,%s)"

        result = cursor.execute(query, (username, password))

        connection.commit()

        if result:
            messagebox.showinfo("Success", "signup Successfully completed!")
        else:
            messagebox.showerror("Failed", "signup Failed")




    def sign():
        window.destroy()

    img = PhotoImage(file="loginimage.png")
    Label(window,image=img,bg='blue').place(x=50,y=50)

    frame=Frame(window,width=350,height=350,bg='white')
    frame.place(x=600,y=70)


    heading=Label(frame,text='SIGN UP',fg='blue',bg='white',font=('arial',25))
    heading.place(x=100,y=5)
    ######################
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0,'password')


    code = Entry(frame,width=25,fg='skyblue',border=0,bg='white',font=('arial',18))
    code.place(x=30,y=150)
    code.insert(0,'password')
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
##    ####################################
    def on_enter(e):
        confirm_code.delete(0,'end')
    def on_leave(e):
        if confirm_code.get()=='':
            confirm_code.insert(0,'password confrimed')


    confirm_code = Entry(frame,width=25,fg='skyblue',border=0,bg='white',font=('bold',18))
    confirm_code.place(x=30,y=220)
    confirm_code.insert(0,'Reenter password')
    confirm_code.bind("<FocusIn>",on_enter)
    confirm_code.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
#####################

    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'username')


    user = Entry(frame,width=25,fg='skyblue',border=0,bg='white',font=('arial',18))
    user.place(x=30,y=80)
    user.insert(0,'username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    ########################################
    Button(frame,width=39,pady=7,text='sign up',bg='blue',fg='white',border=0,command=signup).place(x=35,y=267)
    label=Label(frame,text='already have an account',fg='black',bg='white',font=('arial',10))
    label.place(x=75,y=315)

    signin=Button(frame,width=6,text='sign in',border=0,bg='white',fg='skyblue',command=sign)
    signin.place(x=215,y=315)

    window.mainloop()

##
#############################################################
####        
img=PhotoImage(file="loginimage.png")
Label(m,image=img,bg='blue').place(x=50,y=50)

frame=Frame(m,width=350,height=350,bg="white")
frame.place(x=600,y=70)
heading=Label(frame,text='SIGN IN',fg='blue',bg='white',font=('arial',20))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')

user=Entry(frame,width=30,fg='skyblue',border=0,bg="white",font=('arial',15))
user.place(x=30,y=80)
user.insert(0,'username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
##
##
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'password')

code=Entry(frame,width=30,fg='skyblue',border=0,bg="white",font=('arial',15))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
##
Button(frame,width=39,pady=7,text='SIGN IN',bg='blue',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('arial',10))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='sign up',border=0,bg='white',fg='skyblue',command=signup_command)
sign_up.place(x=215,y=270)

##
##
##
m.mainloop()
