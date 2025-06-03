import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def load_update_borrow_window(id):
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


    # entry boxes
    BorrowerID = Entry(EntryFrame, width=20, font=('Arial',12))
    BorrowerID.grid(row=1, column=0, padx=5, pady=(5,15))

    BookID = Entry(EntryFrame, width=20, font=('Arial ',12))
    BookID.grid(row=3, column=0, padx=5, pady=5)

    # labels for entry box
    BorrowerIDLabel = Label(EntryFrame, text="BorrowerID", font=('Arial ',12))
    BorrowerIDLabel.grid(row=0, column=0, padx=5, pady=1, sticky="w")    

    BookIDLabel = Label(EntryFrame, text="BookID", font=('Arial ',12))
    BookIDLabel.grid(row=2, column=0,  padx=5, pady=1, sticky="w")

    sqlStr="SELECT * FROM borrowedbooks WHERE borrowerid = %s"
    cursor.execute(sqlStr,(id,))

    res = cursor.fetchone()

    BorrowerID.insert(0,res[1])

    BookID.insert(0, res[2])

    def updateBorrow(id):
        sqlString = "UPDATE borrowedbooks SET borrowerid= %s, bookid= %s where borrowerid= %s"
        
        for x in [BorrowerID.get(), BookID.get()]:
            if x=="":
                messagebox.showerror("Empty Field","All fields must be filled.")
                return


        values = BorrowerID.get(), BookID.get(),id

        cursor.execute(sqlString,values)
        conn.commit()


        root.destroy()
        messagebox.showinfo("Success","Borrow record updated succesfuly")
        
    updateMemberBtn = Button(EntryFrame, text="Update record", font=('Arial ',12), command=lambda:updateBorrow(id))
    updateMemberBtn.grid(row=6,pady=(8,3),padx=5, columnspan=2)


    mainloop()