from tkinter import *
import pymysql
from PIL import Image, ImageTk
from tkinter import messagebox
from updateBook import load_update_book_window


def list_all_book():
    root = Toplevel()
    root.geometry("1000x600")
    root.minsize(width=600, height=300)
    root.maxsize(width=1000, height=600)
    
    #bg img
    bg_img = Image.open("kutuphane.jpg")
    img_resized = bg_img.resize((1000, 600), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(img_resized)

    bg_label = Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    #frame
    showFrame = Frame(root, bd=3, relief='ridge')
    showFrame.place(relx=0.5, rely=0.5,anchor='center')
        
    
    #stay on top
    root.attributes('-topmost', True)
    
    
    #connect to database
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password = "123123123",
        database="library"
    )
    cursor = conn.cursor()

    sqlStr = "SELECT * FROM Books"
    cursor.execute(sqlStr)

    arr = cursor.fetchall()
        
    delLabel = Label(showFrame, text="Delete", font=('Arial ',12), borderwidth=1, relief="solid")
    delLabel.grid(row=0, column=0,padx=3,pady=3, sticky='nsew')
    
    
    editLabel = Label(showFrame, text="Edit", font=('Arial ',12), borderwidth=1, relief="solid")
    editLabel.grid(row=0, column=1,padx=3,pady=3, sticky='nsew')
    
    bookIDLabel = Label(showFrame, text="Book ID", font=('Arial ',12), borderwidth=1, relief="solid")
    bookIDLabel.grid(row=0, column=2,padx=3,pady=3, sticky='nsew')

    authorLabel = Label(showFrame, text="Author", font=('Arial ',12), borderwidth=1, relief="solid")
    authorLabel.grid(row=0, column=3,padx=3,pady=3, sticky='nsew')

    titleLabel = Label(showFrame, text="Title", font=('Arial ',12), borderwidth=1, relief="solid")
    titleLabel.grid(row=0, column=4,padx=3,pady=3, sticky='nsew')

    pagecountLabel = Label(showFrame, text="Page Count", font=('Arial ',12), borderwidth=1, relief="solid")
    pagecountLabel.grid(row=0, column=5,padx=3,pady=3, sticky='nsew')

    stockLabel = Label(showFrame, text="Stock Count", font=('Arial ',12), borderwidth=1, relief="solid")
    stockLabel.grid(row=0, column=6,padx=3,pady=3, sticky='nsew')

    sectionLabel = Label(showFrame, text="Section", font=('Arial ',12), borderwidth=1, relief="solid")
    sectionLabel.grid(row=0, column=7,padx=3,pady=3, sticky='nsew')


    def deleteBook(Bookid):
        sqlStr="DELETE FROM BOOKS WHERE Bookid = %s"
        cursor.execute(sqlStr,(Bookid,))
        conn.commit()
        root.destroy()
        messagebox.showinfo("Success","Book successfully deleted.")




    l = len(arr)
    a=1
    b=0
    for x in arr:
        id = x[0]
        del_button = Button(showFrame, font=('Arial ',12), text="Delete "+str(id), command=lambda id=id:deleteBook(id))
        del_button.grid(column=b,row=a)

        edit_button = Button(showFrame, font=('Arial ',12), text="Edit "+str(id), command=lambda id=id:load_update_book_window(id))
        edit_button.grid(column=b+1,row=a)

        for y in x:
            Label(showFrame, text=y,font=('Arial ',12), borderwidth=1, relief="solid").grid(sticky='nsew',row=a, column=b+2,padx=3,pady=3)
            b+=1
        a+=1
        b=0

    mainloop()

