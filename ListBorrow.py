from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from updateBorrow import load_update_borrow_window
import datetime
from datetime import date
import pymysql

def list_all_borrows(memberid): #to check admin
    root = Toplevel()

    root.geometry("1000x600")
    root.minsize(width=550, height=300)
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
    

    
    #connect to database
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password = "123123123",
        database="library"
    )
    cursor = conn.cursor()


    #get records for one member or all
    cursor.execute("SELECT isadmin FROM MEMBER where memberid = %s", (memberid))
    result = cursor.fetchone()
    flag = result[0]

    if(flag):
        sqlStr = "SELECT BorrowerID,b.BookID,Title,BorrowDate,ReturnDate,IsReturned FROM borrowedbooks JOIN books b on borrowedbooks.bookid=b.bookid"
        cursor.execute(sqlStr)
    
    else:
        sqlStr = "SELECT BorrowerID,b.BookID,Title,BorrowDate,ReturnDate,IsReturned FROM borrowedbooks JOIN books b on borrowedbooks.bookid=b.bookid WHERE borrowerid = %s"
        cursor.execute(sqlStr,(memberid))

    arr = cursor.fetchall()
    
    #labels
    if(flag):
        delLabel = Label(showFrame, text="Delete", font=('Arial ',12), borderwidth=1, relief="solid")
        delLabel.grid(row=0, column=0,padx=3,pady=3, sticky='nsew')
        
        editLabel = Label(showFrame, text="Edit", font=('Arial ',12), borderwidth=1, relief="solid")
        editLabel.grid(row=0, column=1,padx=3,pady=3, sticky='nsew')


    BorrowerIDLabel = Label(showFrame, text="Borrower ID", font=('Arial ',12), borderwidth=1, relief="solid")
    BorrowerIDLabel.grid(row=0, column=2,padx=3,pady=3, sticky='nsew')
   
    BookIDLabel = Label(showFrame, text="Book ID", font=('Arial ',12), borderwidth=1, relief="solid")
    BookIDLabel.grid(row=0, column=3,padx=3,pady=3, sticky='nsew')

    BookNameLabel = Label(showFrame, text="Book Name", font=('Arial ',12), borderwidth=1, relief="solid")
    BookNameLabel.grid(row=0, column=4,padx=3,pady=3, sticky='nsew')

    BorrowDateLabel = Label(showFrame, text="Borrow Date", font=('Arial ',12), borderwidth=1, relief="solid")
    BorrowDateLabel.grid(row=0, column=5,padx=3,pady=3, sticky='nsew')

    ReturnDateLabel = Label(showFrame, text="Return Date", font=('Arial ',12), borderwidth=1, relief="solid")
    ReturnDateLabel.grid(row=0, column=6,padx=3,pady=3, sticky='nsew')

    ReturnedLabel = Label(showFrame, text="Returned", font=('Arial ',12), borderwidth=1, relief="solid")
    ReturnedLabel.grid(row=0, column=7,padx=3,pady=3, sticky='nsew')

    if(flag):
        ReturnLabel = Label(showFrame, text="Return?", font=('Arial ',12), borderwidth=1, relief="solid")
        ReturnLabel.grid(row=0, column=7,padx=3,pady=3, sticky='nsew')


    def deleteBorrow(Borrowid):
        sqlStr="DELETE FROM Borrowedbooks WHERE Borrowerid = %s"
        cursor.execute(sqlStr,(Borrowid,))
        conn.commit()
        root.destroy()
        messagebox.showinfo("Success","Borrow record successfully deleted.")


 
    #variable for checkbox 
    checkbox_vars = []


    def toggleReturn(id):
        x = returnedVar.get()

        if(x):
            messageAnswer = messagebox.askokcancel("ARE YOU SURE", "Is the book returned?")

            if(messageAnswer):
                today = datetime.date.today()

                funcSql = "UPDATE borrowedbooks SET returndate= %s, isReturned=%s WHERE BORROWERID = %s"
                cursor.execute(funcSql,(today, x, id))
                
                conn.commit()

                messagebox.showinfo("SUCCESS", "Book is successfully returned.")

            else:
                return
            
        else:
            messageAnswer = messagebox.askokcancel("ARE YOU SURE", "Undo return status?")
            if(messageAnswer):
                    funcSql = "UPDATE borrowedbooks SET returndate = NULL, isReturned = %s WHERE BORROWERID = %s"
                    cursor.execute(funcSql, (0, id))
                    conn.commit()
                    messagebox.showinfo("SUCCESS", "Return is undone.")
                    return

    a=1
    b=0
    for x in arr:
        id = x[0]
        if(flag):
            del_button = Button(showFrame, font=('Arial ',12), text="Delete "+str(id), command=lambda id=id:deleteBorrow(id))
            del_button.grid(column=b,row=a)

            del_button = Button(showFrame, font=('Arial ',12), text="Edit "+str(id), command=lambda id=id:load_update_borrow_window(id))
            del_button.grid(column=b+1,row=a)
        
        
        for y in x:
            Label(showFrame, text=y, font=('Arial ',12), borderwidth=1, relief="solid").grid(row=a, column=b+2, sticky='nsew')
            b+=1

        if(flag):
            returnedVar = IntVar()
            returnedVar.set(x[5])
            checkbox_vars.append((id, returnedVar)) 
            checkBox = Checkbutton(showFrame, variable=returnedVar, command=lambda id=id: toggleReturn(id))
            checkBox.grid(column=b+1,row=a)

        a+=1
        b=0 

    mainloop()
