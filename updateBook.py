import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def load_update_book_window(id):
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
    # input boxes

    bookId = Entry(EntryFrame, width=30, font=('Arial ',12))
    bookId.grid(row=0, column=1,padx=3,pady=3)

    author = Entry(EntryFrame, width=30, font=('Arial ',12))
    author.grid(row=1, column=1,padx=3,pady=3)

    title = Entry(EntryFrame, width=30, font=('Arial ',12))
    title.grid(row=2, column=1,padx=3,pady=3)

    pagecount = Entry(EntryFrame, width=30, font=('Arial ',12))
    pagecount.grid(row=3, column=1,padx=3,pady=3)

    stock = Entry(EntryFrame, width=30, font=('Arial ',12))
    stock.grid(row=4, column=1,padx=3,pady=3)

    section = Entry(EntryFrame, width=30, font=('Arial ',12))
    section.grid(row=5, column=1,padx=3,pady=3)


    # labels

    bookIDLabel = Label(EntryFrame, text="Book ID", font=('Arial ',12))
    bookIDLabel.grid(row=0, column=0,padx=3,pady=3)

    authorLabel = Label(EntryFrame, text="Author", font=('Arial ',12))
    authorLabel.grid(row=1, column=0,padx=3,pady=3)

    titleLabel = Label(EntryFrame, text="Title", font=('Arial ',12))
    titleLabel.grid(row=2, column=0,padx=3,pady=3)

    pagecountLabel = Label(EntryFrame, text="Page Count", font=('Arial ',12))
    pagecountLabel.grid(row=3, column=0,padx=3,pady=3)

    stockLabel = Label(EntryFrame, text="Stock Count", font=('Arial ',12))
    stockLabel.grid(row=4, column=0,padx=3,pady=3)

    sectionLabel = Label(EntryFrame, text="Section", font=('Arial ',12))
    sectionLabel.grid(row=5, column=0,padx=3,pady=3)

    sqlStr="SELECT * FROM Books WHERE Bookid = %s"
    cursor.execute(sqlStr,(id,))

    res = cursor.fetchone()

    bookId.insert(0,res[0])

    author.insert(0, res[1])

    title.insert(0, res[2])

    pagecount.insert(0, res[3])

    stock.insert(0, res[4])

    section.insert(0, res[5])



    def updateBook(id):
        sqlString = "UPDATE books SET bookId= %s, author= %s, title=%s, pagecount=%s,stock=%s,section=%s where bookid=%s"
        
        for x in [bookId.get(), author.get(),title.get(),pagecount.get(),stock.get(),section.get()]:
            if x=="":
                messagebox.showerror("Empty Field","All fields must be filled.")
                return


        values = int(bookId.get()), author.get(),title.get(),int(pagecount.get()),int(stock.get()),section.get(),id

        cursor.execute(sqlString,values)
        conn.commit()


        root.destroy()
        messagebox.showinfo("Success","Book updated succesfuly")
        
    updateBookBtn = Button(EntryFrame, text="Update record", font=('Arial ',12), command=lambda:updateBook(id))
    updateBookBtn.grid(row=6,pady=(8,3),padx=5, columnspan=2)


    mainloop()