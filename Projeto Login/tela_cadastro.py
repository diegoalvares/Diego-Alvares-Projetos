from tkinter import *
from tkinter import messagebox

#------------ TELA CADASTRO --------------------
tela_login = Tk()
tela_login.resizable(width=False, height=False)
bg = PhotoImage(file='fundo.PNG')
canvas1 = Canvas(tela_login, width=1000, height=800)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(100, 280, image=bg)


#------------------------------------ ENTRADAS ----------------------
nome = canvas1.create_text(90, 120, text='Nome', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
nome_entry = Entry(tela_login, font=('Tahoma', 20))
nome_entry.place(x=40, y=145, height=35, width=550)

tel = canvas1.create_text(110, 240, text='Telefone', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
tel_entry = Entry(tela_login, font=('Tahoma', 20))
tel_entry.place(x=40, y=270, height=35, width=550)

end = canvas1.create_text(110, 240, text='Telefone', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
end_entry = Entry(tela_login, font=('Tahoma', 20))
end_entry.place(x=40, y=270, height=35, width=550)



#-------------- FUNÇÃO LOGIN ------------------------

def login():
    if user_entry.get().lower().strip() == user_name and password_entry.get() == password_login:
        messagebox.showinfo(title='Aviso!', message='Login efetuado com sucesso!')
    elif user_entry.get().lower().strip() != user_name or password_entry.get() != password_login:
        messagebox.showerror(title='ERROR', message='Usuário ou senha incorreta!')

#--------------------- Botões -----------------------------

bt1 = Button(tela_login, text='Salvar', font=('Tahoma', 15, 'bold'), background='#191970', foreground='#FFFFFF', command=login)
bt1.place(x=120, y=400, width=90, height=35)

bt2 = Button(tela_login, text='Sair', font=('Tahoma', 15, 'bold'), background='#191970', foreground='#FFFFFF', command=tela_login.destroy)
bt2.place(x=250, y=400, width=90, height=35)
#--------------------- RODAPÉ -----------------------------

rod = canvas1.create_text(225, 580, text='Empresas S/A', fill='#FFFFFF', font=('Tahoma', 15, 'bold'))


tela_login.mainloop()