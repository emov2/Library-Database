import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def load_update_member_window(id):
    #connect to db

    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123123123",
        database="library"
    )
    cursor = conn.cursor()

    #submit book panel

    root = Toplevel()
    root.geometry("1000x600")
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
    MemberId = Entry(EntryFrame, width=30, font=('Arial',12))
    MemberId.grid(row=1,column=0,padx=3,pady=3)

    MemberName = Entry(EntryFrame, width=30, font=('Arial',12))
    MemberName.grid(row=3,column=0,padx=3,pady=3)

    MemberPassword = Entry(EntryFrame, width=30, font=('Arial',12))
    MemberPassword.grid(row=5,column=0,padx=3,pady=3)

    # Labels for entry boxes
    MemberIdlabel = Label(EntryFrame, text="MemberID", font=('Arial',12))
    MemberIdlabel.grid(row=0, column=0,  padx=5, pady=1, sticky="w") 

    MemberName_label = Label(EntryFrame, text="Member Name", font=('Arial',12))
    MemberName_label.grid(row=2, column=0,  padx=5, pady=1, sticky="w") 

    MemberPassword_label = Label(EntryFrame, text="Member Password", font=('Arial',12))
    MemberPassword_label.grid(row=4, column=0,  padx=5, pady=1, sticky="w") 

    sqlStr="SELECT * FROM member WHERE memberid = %s"
    cursor.execute(sqlStr,(id,))

    res = cursor.fetchone()

    MemberId.insert(0,res[0])

    MemberName.insert(0,res[1])

    MemberPassword.insert(0, res[2])

    def updateMember(id):
        sqlString = "UPDATE member SET memberid= %s, MemberName= %s, MemberPassword= %s where memberid= %s"
        
        for x in [MemberName.get(), MemberPassword.get(), MemberId.get()]:
            if x=="":
                messagebox.showerror("Empty Field","All fields must be filled.")
                return


        values = int(MemberId.get()),MemberName.get(), MemberPassword.get(),id

        cursor.execute(sqlString,values)
        conn.commit()


        root.destroy()
        messagebox.showinfo("Success","Member updated succesfuly")
        
    updateMemberBtn = Button(EntryFrame, text="Update record", font=('Arial ',12), command=lambda:updateMember(id))
    updateMemberBtn.grid(row=6,pady=(8,3),padx=5, columnspan=2)


    mainloop()


