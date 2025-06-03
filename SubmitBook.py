import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def load_submit_book_window():
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


    def submitBook():
        sqlString = "INSERT INTO books(BookID, author,title,pagecount,stock,section) VALUES(%s,%s,%s,%s,%s,%s)"
        
        for x in [bookId.get(), author.get(),title.get(),pagecount.get(),stock.get(),section.get()]:
            if x=="":
                messagebox.showerror("Empty Field","All fields must be filled.")
                return


        values = int(bookId.get()), author.get(),title.get(),int(pagecount.get()),int(stock.get()),section.get()

        cursor.execute(sqlString,values)

        bookId.delete(0,'end') 
        author.delete(0,'end')
        title.delete(0,'end')
        pagecount.delete(0,'end')
        stock.delete(0,'end')
        section.delete(0,'end')
        
        messagebox.showinfo("Success","Book submitted succesfuly")


        conn.commit()
        

    submitBookBtn = Button(EntryFrame, text="Submit record", command=submitBook, font=('Arial ',12))
    submitBookBtn.grid(row=6,pady=(8,3),padx=5, columnspan=2)

    mainloop()