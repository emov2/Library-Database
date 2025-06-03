from tkinter import *
from tkinter import messagebox
import pymysql
import datetime
from PIL import Image, ImageTk


def load_submit_borrow_window():
    #connect to db

    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123123123",
        database="library"
    )
    cursor = conn.cursor()


    #create root
    root = Toplevel()
    root.title("Borrow Record Submission")
    root.minsize(height=180, width=300)

    
    #stay on top
    root.attributes('-topmost', True)

    #bg img 
    bg_img = Image.open("kutuphane.jpg")
    img_resized = bg_img.resize((1000, 600), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(img_resized)

    bg_label = Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # framing
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




    #submit button and func

    def SubmitBorrow():
        sqlString = "INSERT INTO BorrowedBooks(BorrowerID, BookID, BorrowDate) VALUES(%s,%s,%s)"
        borr= (BorrowerID.get())
        book=  (BookID.get())

        cursor.execute("SELECT MemberID FROM Member")
        member_ids = [row[0] for row in cursor.fetchall()]


        cursor.execute("SELECT BookID FROM Books")
        book_ids = [row[0] for row in cursor.fetchall()]




        if(BorrowerID.get() == "" or BookID.get()==""):
            messagebox.showerror("INVALID VALUE", "BookID or BorrowerID field can't be empty.")

        elif((int(borr) not in member_ids) or int(book) not in book_ids):
            messagebox.showerror("INVALID VALUE", "Book or Borrower id doesnt exist")

        else:
            values = int(borr), int(book), datetime.date.today()

            cursor.execute(sqlString,values)
            messagebox.showinfo("Success","Record successfully submitted.")

        BorrowerID.delete(0,'end')
        BookID.delete(0,'end')


        conn.commit()

    submt = Button(EntryFrame, text="Submit record", command=SubmitBorrow, font=('Arial ',12))
    submt.grid(pady=(8,3),padx=5)



    mainloop()