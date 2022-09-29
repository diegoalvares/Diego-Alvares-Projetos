from tkinter import *
from tkinter import messagebox

#------------ TELA CADASTRO --------------------
tela_login = Tk()
tela_login.resizable(width=False, height=False)
bg = PhotoImage(file='fundo.PNG')
canvas1 = Canvas(tela_login, width=1000, height=800)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(100, 280, image=bg)

nome = canvas1.create_text(500, 50, text='Cadastro de Novo Cliente', fill='#FFFFFF', font=('Tahoma', 35, 'bold'))


#------------------------------------ ENTRADAS ----------------------
nome = canvas1.create_text(90, 120, text='Nome', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
nome_entry = Entry(tela_login, font=('Tahoma', 20))
nome_entry.place(x=40, y=145, height=35, width=550)

tel = canvas1.create_text(110, 240, text='Telefone', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
tel_entry = Entry(tela_login, font=('Tahoma', 20))
tel_entry.place(x=40, y=270, height=35, width=550)

email = canvas1.create_text(90, 360, text='E-mail', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
email_entry = Entry(tela_login, font=('Tahoma', 20))
email_entry.place(x=40, y=385, height=35, width=550)

end = canvas1.create_text(115, 480, text='Endereço', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
end_entry = Entry(tela_login, font=('Tahoma', 20))
end_entry.place(x=40, y=505, height=35, width=550)

#--------------------- Botões -----------------------------

bt1 = Button(tela_login, text='Salvar', font=('Tahoma', 18, 'bold'), background='#191970', foreground='#FFFFFF', command='')
bt1.place(x=130, y=580, width=110, height=45)

bt2 = Button(tela_login, text='Sair', font=('Tahoma', 18, 'bold'), background='#191970', foreground='#FFFFFF', command=tela_login.destroy)
bt2.place(x=270, y=580, width=110, height=45)
#--------------------- RODAPÉ -----------------------------

rod = canvas1.create_text(240, 730, text='Empresas S/A', fill='#FFFFFF', font=('Tahoma', 15, 'bold'))


tela_login.mainloop()