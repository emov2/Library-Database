from tkinter import *
import pymysql
from MainPanels import launch_admin_window, launch_user_window
from PIL import Image, ImageTk

#connect to database

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password = "123123123",
    database="library"
)
cursor = conn.cursor()


#login window

root = Tk()
root.title("Login")
root.minsize(width=350, height=280)
root.maxsize(width=1000, height=600)
root.geometry("600x500")


#bg img
bg_img = Image.open("kutuphane.jpg")
img_resized = bg_img.resize((1000, 600), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(img_resized)

bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#framing
LoginFrame = Frame(root, bd=5, relief='ridge')
LoginFrame.place(anchor="center", relx=0.5, rely=0.5)

#input boxes
memberID = Entry(LoginFrame, width=22, font=('Arial Bold',16), bg="#FFFFFF")
memberID.grid(row=1, column=0,padx=4,pady=4)

password = Entry(LoginFrame, width=22, font=('Arial Bold',16), bg="#FFFFFF")
password.grid(row=3, column=0,padx=4,pady=4)

#labels
idLabel = Label(LoginFrame, text="MemberID", font=('Arial Bold',16))
idLabel.grid(row=0,column=0,padx=4,pady=4)

passwordLabel = Label(LoginFrame, text="Password", font=('Arial Bold',16),justify="left")
passwordLabel.grid(row=2,column=0,padx=4,pady=4)


resultLabel = Label(LoginFrame, text='Enter ID and password for login.', font=('Arial Bold',12), bg="#FFFFFF")
resultLabel.grid(row=5,column=0)

def Login():
    global resultLabel

    try: fid = int(memberID.get())
    except ValueError:
        resultLabel.config(text="MemberID must be numeric", font=('Arial Bold',12))


    fpassword = password.get()


    if(fpassword=="" or fid==""):
        resultLabel.config(text="Member name or password is empty can\'t submit", font=('Arial Bold',12))
        
    else:
        sqlString = "SELECT memberid, memberpassword, isAdmin FROM member"

        cursor.execute(sqlString)
        arr = cursor.fetchall()
        for idx, passwordx, adminity in arr:
            if(fid==idx and fpassword == passwordx):
                resultLabel.config(text="Login successful")
                root.destroy()
                if(adminity):
                    launch_admin_window(fid)
                    return 
                else:
                    launch_user_window(fid)
                    return 
                    

        resultLabel.config(text="user not found!", font=('Arial Bold',12))


    return


loginButton = Button(LoginFrame, text="Login", command=Login, font=('Arial Bold',12), width=15, bg="#FFFFFF")
loginButton.grid(row=4,column=0,padx=4,pady=4)

mainloop()
