import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from cadastro import cadastro1
from Usuario_menu import Acesso_Usuario
from Admin_menu import *
from Whatts import *
from cx import *

class Login(cadastro1,Acesso_Usuario,Admin,caixa,bomb):
    def janela1(self):
        self.janela_principal=Tk()
        self.largura=1500
        self.altura=800
        self.janela_principal.geometry("1500x800+0+0")
        self.janela_principal.title("Sistema :)")
        #self.janela_principal.resizable(1, 1)
        self.janela_principal.attributes('-fullscreen', True)
        self.objetos_login()
        self.janela_principal.mainloop()      
        
    def get_usu(self):
        self.loginwframe.pack_forget()
        self.loginwframe.destroy()
        self.frame_eu.destroy()
        self.logo.destroy()
        self.usuario_mainwmenu(8,8)

    def get_adm(self):
        self.loginwframe.pack_forget()
        self.loginwframe.destroy()
        self.frame_eu.destroy()
        self.logo.destroy()
        self.Admin_mainmenu(8,8)
        
    def alternar_visibilidade(self):
        if self.signin_login.winfo_ismapped():
            self.signin_login.place_forget()
            self.janela_principal.after(500, self.alternar_visibilidade)
        else:
            self.signin_login.place(x=35,y=270)
            self.janela_principal.after(500, self.alternar_visibilidade)

    def __login_del__(self):
        if messagebox.askyesno("Sair","Deseja realmente sair?"):
            self.janela_principal.destroy()
            exit(0)

    def objetos_login(self):
        self.loginwframe=Canvas(self.janela_principal,bg="black",height=400,width=300)
        self.loginwframe.place(x=(self.largura/2)-150,y=300)
        self.janela_principal.title("Login...")
        self.janela_principal.config(bg="#616161")
        self.janela_principal.iconbitmap('ImageTk/logo.ico')
        self.janela_principal.protocol('WM_DELETE_WINDOW',self.__login_del__)
        self.usuname = StringVar(value="Nome do Usuario")
        self.passaword = StringVar(value="Senha do Usuario")
        self.toplabel=Label(self.loginwframe,fg="white",bg="black",anchor="center",text="Login",font="arial 40")
        self.toplabel.place(x=75,y=25)
        self.us_usu=ttk.Entry(self.loginwframe,textvariable=self.usuname, width=20,font="arial 14")
        self.us_usu.bind("<Return>",lambda event:self.pa_usu.focus())
        self.us_usu.bind("<KeyPress-x>",lambda event:self.get_usu())
        self.us_usu.bind("<KeyPress-a>",lambda event:self.get_adm())
        self.us_usu.bind("<KeyPress-w>",lambda event:self.tela_zap())
        self.us_usu.bind('<KeyPress>',lambda event:self.onclickus())
        self.pa_usu=ttk.Entry(self.loginwframe,textvariable=self.passaword, width=20,font="arial 14")
        self.pa_usu.bind("<Return>",lambda event:self.checkuser())
        self.pa_usu.bind('<KeyPress>',lambda event:self.onclickpa())
        self.us_usu.place(x=35,y=145,height=40)
        self.pa_usu.place(x=35,y=185,height=40)
        self.us_usu.select_range(0,'end')
        self.pa_usu.select_range(0,'end')
        
        
        self.signin_login = Button(self.loginwframe,width=20,text="Login",bg="salmon",fg="dimgray",command=self.checkuser,font="arial 14",foreground="black",bd="0")
        self.signin_login.place(x=35,y=270)
        
        self.signin_cadastrar = Button(self.loginwframe,width=20,text="Cadastrar",bg="darkorange",command=self.cadastrar0,fg="dimgray",font="arial 14",foreground="white",bd="0")
        self.signin_cadastrar.place(x=35,y=310)

        self.atalho_admin= Button(self.loginwframe,width=1,bg="black",command=self.adm,fg="dimgray",bd="0")
        self.atalho_admin.place(x=150,y=20)
        
        self.atalho_usu= Button(self.loginwframe,width=1,bg="black",command=self.get_usu,fg="dimgray",bd="0")
        self.atalho_usu.place(x=180,y=20)
        
        self.whatts_butao=Button(self.loginwframe,bg="green",text="WhatsApp",highlightbackground="#33eb26",command=self.tela_zap,width=10,fg="white",bd="2")
        self.whatts_butao.place(x=215,y=370)

        self.us_usu.focus()
        self.cont_pa=0
        self.cont_us=0
        self.info_eu()
        self.alternar_visibilidade()
    def info_eu(self):
        self.frame_eu = Canvas(self.janela_principal, bg="black", height=300, width=800)
        self.frame_eu.place(x=(self.largura / 2) - 400, y=0)
        self.nome_fone = Label(self.frame_eu, bg="black", fg="white", text="Criador: Giuseph Giangareli                    Telefone:(66)9 9908-6599",bd=0, font="Arial 15 bold", width=500)
        self.nome_fone.place(x=(self.frame_eu.winfo_reqwidth() - self.nome_fone.winfo_reqwidth()) // 2, y=5)
        self.gmail = Label(self.frame_eu, bg="black", fg="white", text="Gmail:Giusephgangareli@gmail.com",bd=0, font="Arial 15 bold", width=500)
        self.gmail.place(x=(self.frame_eu.winfo_reqwidth() - self.gmail.winfo_reqwidth()) // 2, y=45)
        self.forma = Label(self.frame_eu, bg="black", fg="white", text="Cursando Eng. de Computação",bd=0, font="Arial 15 bold", width=500)
        self.forma.place(x=(self.frame_eu.winfo_reqwidth() - self.forma.winfo_reqwidth()) // 2, y=80)
        self.forma = Label(self.frame_eu, bg="black", fg="red", text="Sistema Em Desenvolvimento...",bd=0, font="Arial 20 bold", width=500)
        self.forma.place(x=(self.frame_eu.winfo_reqwidth() - self.forma.winfo_reqwidth()) // 2, y=120)
        self.insta = Label(self.frame_eu, bg="black", fg="white", text="@Giuseph_gian",bd=0, font="Arial 13 bold")
        self.insta.place(relx=1, rely=1, anchor="se", width=150)
        self.versao = Label(self.frame_eu, bg="black", fg="white", text="Versao:0.1.0",bd=0, font="Arial 13 bold")
        self.versao.place(x=0, rely=1, anchor="sw", width=120)
        
        self.logo = Canvas(self.janela_principal, bg="#616161",bd=0,highlightthickness=0, width=50, height=700)
        self.logo.place(x=self.janela_principal.winfo_width() - 10, y=self.janela_principal.winfo_height() // 2, anchor="e")

        texto_vertical = " VENDAS=JESUS NO CONTROLE"
        for i, char in enumerate(texto_vertical):
            self.logo.create_text(10, i * 25, text=char, font=("Arial", 22), anchor="w", angle=0)
        for _ in range(random.randint(100,1000)):
            x = random.randint(0, 1800)
            y = random.randint(0, 1000)
            tamanho = random.uniform(0.5, 3)
            self.frame_eu.create_oval(x, y, x + tamanho, y + tamanho, fill='white', outline='white')
            self.loginwframe.create_oval(x, y, x + tamanho, y + tamanho, fill='white', outline='white')
    def cadastrar0(self):
        self.tela_cadastro()
        self.cads.focus_set()

    def adm(self):
        s=self.us_usu.get()
        s1=self.pa_usu.get()

        if s=="ADMIN" and s1=="ADMIN":
                messagebox.showinfo("ADMIN","BEM VINDO JESUS")
                self.get_adm()
    def checkuser(self,*args,**wrargs):
        s=self.us_usu.get()
        s1=self.pa_usu.get()
        try:
            if s=="" or s1=="":
                messagebox.showinfo("VAZIO","Erro, Preencha todos os campos")
                self.us_usu.focus()

            else:
                self.conn = sqlite3.connect("banco.db")
                self.cur = self.conn.cursor()
                self.cur.execute("SELECT * FROM users WHERE username=? AND password=?", (s, s1))
                self.rows = self.cur.fetchall()
                if len(self.rows)>=1:
                    messagebox.showinfo(s,"BEM VINDO")
                    self.get_usu()
                else:
                    messagebox.showinfo("Error","SENHA OU USUARIO INCORRETO!")
                    self.us_usu.focus()
                    self.cur.close()
                    self.conn.close()       
        except:
            self.conn.close()
            self.janela_principal.mainloop()

    def onclickus(self):
        if self.cont_us == 0:
            self.us_usu.delete(0,END)
            self.cont_us= self.cont_us+1

    def onclickpa(self):
        if self.cont_pa == 0:
            self.pa_usu.config(show="*")
            self.pa_usu.delete(0,END)
            self.cont_pa=self.cont_pa + 1

    def fechar_login(self):
        self.janela_principal.mainloop()
    
