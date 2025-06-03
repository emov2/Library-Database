from tkinter import *
from PIL import Image, ImageTk
import pymysql

from SubmitBook import load_submit_book_window
from SubmitBorrow import load_submit_borrow_window
from SubmitMember import load_submit_member_window
from ListBook import list_all_book
from ListMember import list_all_member
from ListBorrow import list_all_borrows
from ChangePassword import change_password_window
#connect to database




def launch_admin_window(memberid):
    conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password = "123123123",
    database="library"
    )
    cursor = conn.cursor()
    
    root = Tk()
    root.title("Admin Panel")
    root.minsize(width=1000, height=600)
    root.maxsize(width=1000, height=600)
    
    #setting bg img

    bg_img = Image.open("kutuphane.jpg")
    img_resized = bg_img.resize((1000, 600), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(img_resized)
    
    bg_label = Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)


    #select userinfo 
    sqlStr = "SELECT * FROM member WHERE memberid = " + str(memberid)
    cursor.execute(sqlStr)
    currentinfo = cursor.fetchall()
    
    root.attributes('-topmost', False)

    #framing


    toolFrame = Frame(root, bg="#FFFFFF", bd=5, relief='ridge')
    toolFrame.place(relx=0.5, rely=0.4, anchor="center")

    #intro special to every user
    introLabel = Label(toolFrame, text=f"Welcome to X library {currentinfo[0][1]}", font=('Arial ',12),bg="#FFFFFF")
    introLabel.grid(columnspan=2,padx=10,pady=10)


    #buttons for submit windows
    SubmitMemberButton = Button(toolFrame, text="Add new member record", command=load_submit_member_window, font=('Arial ',12), width=30)
    SubmitMemberButton.grid(row=1, column=1, sticky='e', padx=(10,4), pady=5)

    SubmitBookButton = Button(toolFrame, text="Add new book record", command=load_submit_book_window, font=('Arial ',12), width=30)
    SubmitBookButton.grid(row=2,column=1,sticky='e', padx=(10,4), pady=5)

    SubmitBorrowButton = Button(toolFrame, text="Add new borrow record", command=load_submit_borrow_window, font=('Arial ',12), width=30)
    SubmitBorrowButton.grid(row=3,column=1,sticky='e', padx=(10,4), pady=5)


    #buttons for listing
    
    ListMemberButton = Button(toolFrame, text="List member records", command=list_all_member, font=('Arial ',12), width=30)
    ListMemberButton.grid(row=1,column=0,sticky='w', padx=5, pady=5)

    ListBookButton = Button(toolFrame, text="List book records", command=list_all_book, font=('Arial ',12), width=30)
    ListBookButton.grid(row=2,column=0,sticky='w', padx=5, pady=5)

    ListBorrowButton = Button(toolFrame, text="List borrow records", command=lambda:list_all_borrows(currentinfo[0][0]), font=('Arial ',12), width=30)
    ListBorrowButton.grid(row=3,column=0,sticky='w', padx=5, pady=5)

    root.mainloop()

def launch_user_window(memberid):
    conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password = "123123123",
    database="library"
    )
    cursor = conn.cursor()
    
    root = Tk()
    root.title("User Panel")
    root.minsize(width=1000, height=600)
    root.maxsize(width=1000, height=600)

    #setting bg img

    bg_img = Image.open("kutuphane.jpg")
    img_resized = bg_img.resize((1000, 600), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(img_resized)
    
    bg_label = Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    #framing
    toolFrame = Frame(root)
    toolFrame.place(relx=0.5, rely=0.3, anchor="center")

    #select userinfo 
    sqlStr = "SELECT * FROM member WHERE memberid = " + str(memberid)
    cursor.execute(sqlStr)
    currentinfo = cursor.fetchall()

    for test in currentinfo:
        print(test)

    #intro special to every user
    introLabel = Label(toolFrame, text=f"Welcome to X library {currentinfo[0][1]}", font=('Arial ',12))
    introLabel.grid(padx=10,pady=10)

    ListBorrowButton = Button(toolFrame, text="List your borrow records", command=lambda:list_all_borrows(currentinfo[0][0]), font=('Arial ',12), width=30, bg="#FFFFFF")
    ListBorrowButton.grid(row=3,column=0,sticky='w', padx=10, pady=10)

    ListBorrowButton = Button(toolFrame, text="Change your password", command=lambda:change_password_window(currentinfo[0][0]), font=('Arial ',12), width=30, bg="#FFFFFF")
    ListBorrowButton.grid(row=4,column=0,sticky='w', padx=10, pady=10)


    root.mainloop()


# launch_admin_window()