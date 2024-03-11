import sqlite3
from tkinter import Label,ttk
from tkinter import *
import tkinter as tk
from tkinter import messagebox

class cadastro1:
    def tela_cadastro(self):
        self.cads = tk.Toplevel(self.janela_principal)
        self.cads.title("Cadastro...")
        width = 500
        height = 600
        self.cads.bind("<Return>",lambda event:self.pa.focus())
        self.cads.iconbitmap('ImageTk\cadastro.ico')

        self.cads.config(bg="blue")
        tela_largura = self.cads.winfo_screenwidth()
        tela_altura = self.cads.winfo_screenheight()
        x = (tela_largura / 2 ) - (width /2 )
        y = (tela_altura / 2 ) - (height /2 )
        self.cads.geometry("%dx%d+%d+%d" % (width,height,x,y))
        self.cads.resizable(0,0)
        self.objetos_cads()


    def objetos_cads(self):
        self.userdados = StringVar(value="Nome do Usuario")
        self.passdados = StringVar(value="Senha do Usuario")
        self.cadswframe=LabelFrame(self.cads,bg="black",height=400,width=300)
        self.cadswframe.place(x=103,y=95)
        self.toplabel=Label(self.cadswframe,fg="white",bg="black",anchor="center",text="Cadastro",font="arial 40")
        self.toplabel.place(x=35,y=25)
        self.us_cads=ttk.Entry(self.cadswframe,textvariable=self.userdados, width=20,font="arial 14")
        self.us_cads.bind('<KeyPress>',lambda event:self.onclickus_())
        self.us_cads.bind("<Return>",lambda event:self.pa.focus())
        self.us_cads.place(x=35,y=145,height=40)
        self.pa=ttk.Entry(self.cadswframe,textvariable=self.passdados, width=20,font="arial 14")
        self.pa.bind('<KeyPress>',lambda event:self.onclickpa_())
        self.pa.bind('<Return>',lambda event:self.checkuser_cads())
        self.pa.select_range(0,'end')
        self.pa.place(x=35,y=185,height=40)

        self.signin_cadastrar = Button(self.cadswframe,width=20,text="Cadastrar",bg="darkorange",command=self.checkuser_cads,fg="dimgray",font="arial 14",foreground="white",bd="0")
        self.signin_cadastrar.place(x=35,y=310)
        
        self.cont_pa_cads=0
        self.cont_us_cads=0
    def checkuser_cads(self):
        s=self.us_cads.get()
        s1=self.pa.get()
        try:
            self.conn = sqlite3.connect("banco.db")
            self.cur = self.conn.cursor()
            self.cur.execute("SELECT * FROM users WHERE username=? AND password=?", (s, s1))
            self.rows = self.cur.fetchall()
            if len(self.rows)>0:
                messagebox.showinfo("Ja existe","USUARIO JA CADASTRADO")
                self.cads.quit()
                self.cadswframe.quit()
            else:
                self.cur.execute("INSERT INTO users VALUES (?, ?)", (s, s1))
                self.conn.commit()
                messagebox.showinfo("Cadastrado","USUARIO CADASTRADO COM SUCESSO!")
                self.cads.destroy()
                
        except:
            self.conn.close()
            self.cads.destroy()

    def onclickus_(self):
        if self.cont_us_cads == 0:
            self.us_cads.delete(0,END)
            self.cont_us_cads= self.cont_us_cads+1

    def onclickpa_(self):
        if self.cont_pa_cads == 0:
            self.pa.config(show="*")
            self.pa.delete(0,END)
            self.cont_pa_cads=self.cont_pa_cads + 1