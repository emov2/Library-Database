from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk
from updateMember import load_update_member_window

def list_all_member():
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

    sqlStr = "SELECT * FROM member"
    cursor.execute(sqlStr)

    arr = cursor.fetchall()
    
    delLabel = Label(showFrame, text="Delete", font=('Arial ',12), borderwidth=1, relief="solid")
    delLabel.grid(row=0, column=0,padx=3,pady=3, sticky='nsew')
    
    editLabel = Label(showFrame, text="Edit", font=('Arial ',12), borderwidth=1, relief="solid")
    editLabel.grid(row=0, column=1,padx=3,pady=3, sticky='nsew')

    
    memberIDLabel = Label(showFrame, text="Member ID", font=('Arial ',12), borderwidth=1, relief="solid")
    memberIDLabel.grid(row=0, column=2,padx=3,pady=3, sticky='nsew')

    memberNameLabel = Label(showFrame, text="Member Name", font=('Arial ',12), borderwidth=1, relief="solid")
    memberNameLabel.grid(row=0, column=3,padx=3,pady=3, sticky='nsew')

    memberPasswordLabel = Label(showFrame, text="Member Password", font=('Arial ',12), borderwidth=1, relief="solid")
    memberPasswordLabel.grid(row=0, column=4,padx=3,pady=3, sticky='nsew')

    memberDateLabel = Label(showFrame, text="Membership Date", font=('Arial ',12), borderwidth=1, relief="solid")
    memberDateLabel.grid(row=0, column=5,padx=3,pady=3, sticky='nsew')

    memberAdmin = Label(showFrame, text="Admin", font=('Arial ',12), borderwidth=1, relief="solid")
    memberAdmin.grid(row=0, column=6,padx=3,pady=3, sticky='nsew')



    def deleteMember(memberId):
        sqlStr="DELETE FROM member WHERE memberId = %s"
        cursor.execute(sqlStr,(memberId,))
        conn.commit()
        root.destroy()
        messagebox.showinfo("Success","Member record successfully deleted.")




    l = len(arr)
    a=1
    b=0

    for x in arr:

        id = x[0]
        del_button = Button(showFrame, font=('Arial ',12), text="Delete "+str(id), command=lambda id=id: deleteMember(id))
        del_button.grid(column=b,row=a)

        del_button = Button(showFrame, font=('Arial ',12), text="Edit "+str(id), command=lambda id=id: load_update_member_window(id))
        del_button.grid(column=b+1,row=a)
        
        for y in x:
            Label(showFrame, text=y, font=('Arial ',12), borderwidth=1, relief="solid").grid(row=a, column=b+2, sticky='nsew')
            b+=1
        a+=1
        b=0

    mainloop()
