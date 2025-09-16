import tkinter as tk
from tkinter import messagebox

# user login data
users = {"admin": "1234", "Ram": "sita!!"}

def check_login():
    userID = user_id.get()
    userPassword=password.get()

    if userID in users and users[userID]==userPassword :
        messagebox.showinfo("Login Success",f"Welcome {userID}!")
        open_homepage(userID)
    else:
        messagebox.showerror("Login Failed","Invalid user id or password")
        # clear the entry
        # Entry.delete(start, end)
        user_id.delete(0,tk.END)
        password.delete(0,tk.END)

    # print("Login sucessfull!",userID,userPassword)

def open_homepage(userName):
    # window.withdraw() → hides the window (you can bring it back with .deiconify()).
    login_window.withdraw()

    # Create home window
    # About tk.Toplevel() :- It creates a new top-level window (a separate window) in your app.
    # Each Toplevel is independent: it has its own title bar, close button, etc.
    home= tk.Toplevel()
    home.title("Home Page")
    home.geometry("300x200")

    tk.Label(home,text=f"Welcome {userName}!").grid(row=1,column=1,padx=10,pady=10)
    tk.Button(home,text="Logout", command=lambda:logout(home)).grid(row=2,column=1,padx=10,pady=10)

def logout(home_window):
    # window.destroy() → permanently closes the window (you can’t bring it back).
    home_window.destroy()
    
    # clear the entry
    user_id.delete(0,tk.END)
    password.delete(0,tk.END)
    
    # window.deiconify() → shows a window that was hidden.
    login_window.deiconify()


    
# Create Login window. This is also main window (tk.Tk())
login_window= tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")

tk.Label(login_window,text="Login ID").grid(row=1,column=1,padx=10,pady=10)
user_id=tk.Entry(login_window)
user_id.grid(row=1,column=2 )

tk.Label(login_window,text="Password").grid(row=2,column=1,padx=10,pady=10)
password= tk.Entry(login_window,show="*")
password.grid(row=2,column=2)

tk.Button(login_window,text="Login",command= check_login).grid(row=3,columnspan=3,padx=10,pady=10)
login_window.mainloop()