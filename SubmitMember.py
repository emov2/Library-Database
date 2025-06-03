from tkinter import *
from tkinter import messagebox
import datetime
import pymysql
from PIL import Image, ImageTk

def load_submit_member_window():
    #connect to database

    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123123123",
        database="library"
    )
    cursor = conn.cursor()


    #admin panel

    root = Toplevel()
    root.minsize(width=400,height=300)
    root.maxsize(width=400,height=300)
    
    #stay on top
    root.attributes('-topmost', True)

    #bg img 
    bg_img = Image.open("kutuphane.jpg")
    img_resized = bg_img.resize((1000, 600), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(img_resized)

    bg_label = Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    #framing
    EntryFrame = Frame(root)
    EntryFrame.place(anchor="center", relx=0.5, rely=0.5)

    # Entry boxes
    MemberName = Entry(EntryFrame, width=30, font=('Arial ',12))
    MemberName.grid(row=1,column=0,padx=3,pady=3)

    MemberPassword = Entry(EntryFrame, width=30, font=('Arial ',12))
    MemberPassword.grid(row=3,column=0,padx=3,pady=3)

    # Labels for entry boxes
    MemberName_label = Label(EntryFrame, text="Member Name", font=('Arial ',12))
    MemberName_label.grid(row=0, column=0,  padx=5, pady=1, sticky="w") 

    MemberPassword_label = Label(EntryFrame, text="Member Password", font=('Arial ',12))
    MemberPassword_label.grid(row=2, column=0,  padx=5, pady=1, sticky="w") 

    # Button for adding entries
    
    def submitMember():
        sqlString = "INSERT INTO MEMBER (MemberName, MemberPassword, Dateofmembership) VALUES (%s,%s,%s)"
        values = MemberName.get(), MemberPassword.get(), datetime.date.today()
        

        
        if( MemberName.get()=="" or MemberPassword.get()==""):
            messagebox.showerror("Empty fields!","Member name or password is empty can\'t submit")

        else:
            cursor.execute(sqlString,values)
            conn.commit()

            MemberName.delete(0,END)
            MemberPassword.delete(0,END)
            messagebox.showinfo("Success!","New member is submitted.")

        return

    submit_btn = Button(EntryFrame, text="Submit Record", command=submitMember, font=('Arial ',12))
    submit_btn.grid(row=5, pady=(8,3),padx=5)

    mainloop()

