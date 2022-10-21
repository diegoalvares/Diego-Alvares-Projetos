from tkinter import *
from tkinter import messagebox


def tela_cadastro():
    #------------ TELA CADASTRO --------------------
    tela_cadastro = Toplevel()
    tela_cadastro.resizable(width=False, height=False)
    bg = PhotoImage(file='fundo.PNG')
    canvas1 = Canvas(tela_cadastro, width=1000, height=800)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(100, 280, image=bg)

    #----------------------------CABEÇALHO E LOGOMARCA ----------------------

    text = canvas1.create_text(500, 50, text='Cadastro de Novo Cliente', fill='#FFFFFF', font=('Tahoma', 35, 'bold'))
    logo = LabelFrame(tela_cadastro, text='LOGOMARCA', font=(40))
    logo.place(x=700, y=200, width=250, height=200)

    #------------------------------------ ENTRADAS ----------------------

    nome = canvas1.create_text(90, 120, text='Nome', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
    nome_entry = Entry(tela_cadastro, font=('Tahoma', 20))
    nome_entry.place(x=40, y=145, height=35, width=550)

    tel = canvas1.create_text(110, 240, text='Telefone', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
    tel_entry = Entry(tela_cadastro, font=('Tahoma', 20))
    tel_entry.place(x=40, y=270, height=35, width=550)

    email = canvas1.create_text(90, 360, text='E-mail', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
    email_entry = Entry(tela_cadastro, font=('Tahoma', 20))
    email_entry.place(x=40, y=385, height=35, width=550)

    end = canvas1.create_text(115, 480, text='Endereço', fill='#FFFFFF', font=('Tahoma', 25, 'bold'))
    end_entry = Entry(tela_cadastro, font=('Tahoma', 20))
    end_entry.place(x=40, y=505, height=35, width=550)

    #--------------------- FUNÇÃO SALVAR -----------------------------

    def salvar():
        nome_entry.get()
        tel_entry.get()
        email_entry.get()
        end_entry.get()

        if nome_entry.get().strip() == '':
            messagebox.showerror(title= 'ERRO!', message='O preenchimento do nome é obrigatório!')

        elif nome_entry.get().strip() != '' and tel_entry.get().strip() == '' or email_entry.get().strip() == '' or end_entry.get().strip() == '':
            aviso = messagebox.askyesno(title='Aviso!', message='Existem campos vazios! Deseja salvar mesmo assim?')
            if aviso == True:
                messagebox.showinfo(title='Aviso!', message='Cadastro efetuado com sucesso!')
                nome_entry.delete(0, END)
                tel_entry.delete(0, END)
                email_entry.delete(0, END)
                end_entry.delete(0, END)

        elif nome_entry.get() != '' and tel_entry.get() and email_entry.get() and end_entry.get() != '':
            aviso = messagebox.askyesno(title='Aviso!', message='Deseja salvar?')
            if aviso == True:
                messagebox.showinfo(title= 'Aviso!', message='Cadastro efetuado com sucesso!')
                nome_entry.delete(0, END)
                tel_entry.delete(0, END)
                email_entry.delete(0, END)
                end_entry.delete(0, END)


    #--------------------- BOTÕES -----------------------------

    bt1 = Button(tela_cadastro, text='Salvar', font=('Tahoma', 18, 'bold'), background='#191970', foreground='#FFFFFF', command=salvar)
    bt1.place(x=130, y=580, width=110, height=45)

    bt2 = Button(tela_cadastro, text='Sair', font=('Tahoma', 18, 'bold'), background='#191970', foreground='#FFFFFF', command=tela_cadastro.destroy)
    bt2.place(x=270, y=580, width=110, height=45)

    #--------------------- RODAPÉ -----------------------------

    rod = canvas1.create_text(240, 730, text='Empresas S/A', fill='#FFFFFF', font=('Tahoma', 15, 'bold'))


    tela_cadastro.mainloop()