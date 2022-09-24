from tkinter import *
from tkinter import messagebox


tela_login = Tk()
tela_login.resizable(width=False, height=False)
bg = PhotoImage(file='fundo.PNG')
canvas1 = Canvas(tela_login, width=450, height=600)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(-50, 100, image=bg)

#------------------------------------ ENTRADAS ----------------------
user = canvas1.create_text(225, 200, text='Usuário', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
user_entry = Entry(tela_login, font=('Tahoma', 20))
user_entry.place(x=50, y=225, height=35, width=350)

password = canvas1.create_text(225, 300, text='Senha', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
password_entry = Entry(tela_login, font=('Tahoma', 20), show='•')
password_entry.place(x=50, y=325, height=35, width=350)


#--------------------- RODAPÉ -----------------------------

rod = canvas1.create_text(225, 550, text='Empresas S/A', fill='#FFFFFF', font=('Tahoma', 15, 'bold'))


tela_login.mainloop()