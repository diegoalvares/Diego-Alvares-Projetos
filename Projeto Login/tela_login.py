from tkinter import *
from tkinter import messagebox

#---------------- USER E PASSWORD --------------------

user_name = 'diego'
password_login = '123456'

#------------ TELA LOGIN --------------------
tela_login = Tk()
tela_login.resizable(width=False, height=False)
bg = PhotoImage(file='fundo.PNG')
canvas1 = Canvas(tela_login, width=450, height=600)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(-50, 100, image=bg)

img1 = PhotoImage(file='Snapshot_5.PNG')
canvas1.create_image(230, 90, image= img1)


#------------------------------------ ENTRADAS ----------------------
user = canvas1.create_text(255, 200, text='Usuário', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
user_img = canvas1.create_text(165, 195, text='👤', fill='#FFFFFF', font=('Tahoma', 30, 'bold'))
user_entry = Entry(tela_login, font=('Tahoma', 20))
user_entry.place(x=50, y=225, height=35, width=350)

password = canvas1.create_text(250, 300, text='Senha', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
password_img = canvas1.create_text(165, 295, text='🔐', fill='#FFFFFF', font=('Tahoma', 30, 'bold'))
password_entry = Entry(tela_login, font=('Tahoma', 20), show='•')
password_entry.place(x=50, y=330, height=35, width=350)

#-------------- FUNÇÃO LOGIN ------------------------

def login():
    if user_entry.get().lower().strip() == user_name and password_entry.get() == password_login:
        messagebox.showinfo(title='Aviso!', message='Login efetuado com sucesso!')
    elif user_entry.get().lower().strip() != user_name or password_entry.get() != password_login:
        messagebox.showerror(title='ERROR', message='Usuário ou senha incorreta!')

#--------------------- Botões -----------------------------

bt1 = Button(tela_login, text='Entrar', font=('Tahoma', 15, 'bold'), background='#191970', foreground='#FFFFFF', command=login)
bt1.place(x=120, y=400, width=90, height=35)

bt2 = Button(tela_login, text='Sair', font=('Tahoma', 15, 'bold'), background='#191970', foreground='#FFFFFF', command=tela_login.destroy)
bt2.place(x=250, y=400, width=90, height=35)
#--------------------- RODAPÉ -----------------------------

rod = canvas1.create_text(225, 580, text='Empresas S/A', fill='#FFFFFF', font=('Tahoma', 15, 'bold'))


tela_login.mainloop()