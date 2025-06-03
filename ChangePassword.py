from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk

def change_password_window(memberid):
    root = Toplevel()
    root.minsize(width=550, height=300)
    root.maxsize(width=1000, height=600)
    
    #stay on top
    root.attributes('-topmost', True)
    
    #bg img
    bg_img = Image.open("kutuphane.jpg")
    img_resized = bg_img.resize((1000, 600), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(img_resized)

    bg_label = Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    #frame
    showFrame = Frame(root, bd=3, relief='ridge')
    showFrame.place(relx=0.5, rely=0.5,anchor='center')
        


    
    #connect to database
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password = "123123123",
        database="library"
    )
    cursor = conn.cursor()



    cursor.execute("SELECT memberpassword FROM MEMBER WHERE MEMBERID=%s",memberid)
    res = cursor.fetchone()
    currPass = res[0]

    #entry boxes


    currentPass = Entry(showFrame, font=('Arial',12)) 
    currentPass.grid(row=1,column=1, padx=10, pady=5)
    
    newPass1 = Entry(showFrame, font=('Arial',12)) 
    newPass1.grid(row=2,column=1, padx=10, pady=5)
    
    newPass2 = Entry(showFrame, font=('Arial',12)) 
    newPass2.grid(row=3,column=1, padx=10, pady=5)

    #labels

    currLabel = Label(showFrame, text="Enter current password", font=('Arial',12))
    currLabel.grid(row=1, padx=10, pady=5, sticky='w')

    newLabel1 = Label(showFrame, text="Enter new password", font=('Arial',12))
    newLabel1.grid(row=2, padx=10, pady=5, sticky='w')

    newLabel2 = Label(showFrame, text="New password again", font=('Arial',12))
    newLabel2.grid(row=3, padx=10, pady=5, sticky='w')


    submt = Button(showFrame, text="Change password", font=('Arial',12), command=lambda:change_password(currPass,memberid))
    submt.grid(row=4, padx=10, pady=5, columnspan=2)

    def change_password(currPass,memberid):
        c = currentPass.get()
        n1 = newPass1.get()
        n2 = newPass2.get()

        if(c =='' or n1=='' or n2==''):
            messagebox.showerror("INVALID VALUE", "All fields mandatory!")


        elif(currPass== n1 and currPass==n2):
            messagebox.showerror("ERROR","New password can't be same with old password")


        elif(str(c)==str(currPass) and n1==n2):
            cursor.execute("UPDATE `library`.`member` SET memberpassword = %s WHERE MEMBERID = %s;",(n1,memberid,))
            messagebox.showinfo("SUCCESS","Password successfully changed.")
            conn.commit()
            root.destroy()

        else:
            messagebox.showerror("ERROR","Password wrong or new password fields are not same")

        return


    mainloop()

