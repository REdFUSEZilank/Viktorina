from tkinter import *
from    tkinter import  messagebox
import pickle


root=Tk()
root.geometry("300x500")
root.title ("Войти в систему")
def registration():
    text = Label(text="Для входа в систему зарегайтесь")
    text_log = Label (text="Введите ваш логин:")
    registr_lodin = Entry()
    text_password1 = Label(text="Введите пароль:")
    registr_password1 = Entry ()
    text_password2 = Label(text = "Еще раз пароль:")
    registr_password2 = Entry (show="*")
    button_registr = Button (text="Зарегаться", command=lambda :save())
    text.pack()
    text_log.pack()
    registr_lodin.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()

    def save():
        login_pass_save = {}
        login_pass_save [registr_lodin.get()] = registr_password1.get()
        f = open ("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close ()
        login()
def login():
    text_log = Label(text="Dойти в систему")
    text_enter_login = Label(text="Введите ваш логин")
    enter_login = Entry()
    text_enter_password = Label (text="Введите логин")
    enter_password = Entry (show="*")
    button_enter = Button (text="Войти", command=lambda : log_proverka())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_password.pack()
    enter_password.pack()
    button_enter.pack()

    def log_proverka():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() ==a[enter_login.get()]:
                messagebox.showinfo("Вы успешно зарегались", "Добрый день")

            else:
                messagebox.showerror("Ошибка", "Вы ввели неверный логин и пароль")
        else:
            messagebox.showerror("Ошибка", "Неверный логин")
        button_start = Button(text="Начать викторину")
        button_start.pack()


registration()


root.mainloop()