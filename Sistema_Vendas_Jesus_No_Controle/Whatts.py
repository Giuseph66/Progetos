from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class bomb():
    def tela_zap(self):
        self.zap=tk.Tk()
        self.zap.geometry("1000x600+100+100")
        self.zap.resizable(0,0)
        self.zap.title("Interação por WhatsApp")
        self.zap.iconbitmap("ImageTk/whatsapp.ico")
        self.fundo=Frame(self.zap,width=999,height=599,bg="#616161", bd=3, borderwidth=3, highlightbackground="green")
        self.fundo.place(x=0,y=0)

        self.stat=Button(self.fundo,text="Iniciar Conexão",font="arial 12 bold",bg="green",fg="white",bd=3,command=self.inicia,highlightbackground="#33eb26")
        self.stat.place(x=790,y=5,width=200)

        self.comeca=Button(self.fundo,text="Mandar mensagens",font="arial 12 bold",bg="green",fg="white",bd=3,command=self.salva,highlightbackground="#33eb26")
        self.comeca.place(x=790,y=550,width=200)

        self.text_msm=Label(self.fundo,text="Messagem que vai ser enviada:",font="arial 12 bold",bg="#616161",width=30)
        self.text_msm.place(x=5,y=5)
        self.msm=Entry(self.fundo,bg="white",width=80,font="Arial 12 bold",bd=3,highlightbackground="green")
        self.msm.place(x=5,y=35)
        
        self.text_contato=Label(self.fundo,text="Nome do Contato:",font="arial 12 bold",bg="#616161",width=15)
        self.text_contato.place(x=5,y=65)
        self.text_contato=Label(self.fundo,text="Numero do Contato:",font="arial 12 bold",bg="#616161",width=15)
        self.text_contato.place(x=250,y=65)
        self.botao_contato=Button(self.fundo,text="Adicionar contato",font="arial 12 bold",command=self.adiciona_ctt,bg="white",width=20)
        self.botao_contato.place(x=500,y=85)
        self.botao_contato_deleta=Button(self.fundo,text="Deletar contato",font="arial 12 bold",bg="red",command=self.dell_ctt,fg="black",width=20)
        self.botao_contato_deleta.place(x=750,y=85)
        self.contato_nome=Entry(self.fundo,bg="white",width=20,font="Arial 12 bold",bd=3,highlightbackground="green")
        self.contato_nome.bind("<Return>", lambda event:self.contato_numero.focus())
        self.contato_nome.place(x=5,y=95)
        self.contato_numero=Entry(self.fundo,bg="white",width=20,font="Arial 12 bold",bd=3,highlightbackground="green")
        self.contato_numero.place(x=250,y=95)
        self.text_contato=Label(self.fundo,text="Contatos salvos:",font="arial 12 bold",bg="#616161",width=15)
        self.text_contato.place(x=5,y=125)
        self.text_contato=Label(self.fundo,text="Mensagens salvas:",font="arial 12 bold",bg="#616161",width=15)
        self.text_contato.place(x=250,y=125)
        self.adicionar_combobox()
        self.msm.focus_force()
    def adicionar_combobox(self):
        self.conexão = sqlite3.connect('banco.db')
        self.cursor = self.conexão.cursor()
        self.cursor.execute("SELECT Nome FROM whatts_nome")
        self.dados = self.cursor.fetchall()
        self.combobox_ctts = ttk.Combobox(self.fundo,height=20,font="arial 12 bold")
        self.combobox_ctts["values"] = [row[0] for row in self.dados]
        self.combobox_ctts.bind("<<ComboboxSelected>>",self.seleciona_ctt)
        self.combobox_ctts.place(x=5, y=155)
        self.cursor.execute("SELECT frase FROM whatts_Frases")
        dados = self.cursor.fetchall()
        self.combobox_frases = ttk.Combobox(self.fundo,height=20,width=70,font="arial 12 bold")
        self.combobox_frases["values"] = [row[0] for row in dados]
        self.combobox_frases.bind("<<ComboboxSelected>>",self.seleciona_frase)
        self.combobox_frases.place(x=250, y=155)
    def seleciona_ctt(self,event):
        self.limpa_whatts()
        selecioneni = self.combobox_ctts.get()
        self.cursor.execute("SELECT * FROM whatts_nome WHERE Nome = ?", (selecioneni,))
        valor = self.cursor.fetchall()
        for _ in valor:
            cdg,nome,numero=_
        self.contato_nome.insert(0,nome)
        self.contato_numero.insert(0,numero)
        self.combobox_ctts.destroy()
        self.adicionar_combobox()
    def seleciona_frase(self,event):
        self.msm.delete(0,END)
        selecioneni = self.combobox_frases.get()
        self.msm.insert(0,selecioneni)
    def adiciona_ctt(self):
        self.nome_procurado=self.contato_nome.get()
        self.numero_procurado=self.contato_numero.get()
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()
        if self.nome_procurado and self.numero_procurado not in "":
            b.execute("SELECT * FROM whatts_nome WHERE Numero = ?", (self.numero_procurado,))
            acho=b.fetchone()
            if acho is not None:
                if messagebox.askyesno("Numero existente","Esse Numero ja exite!\n Deseja atualizar?"):
                    b.execute("UPDATE whatts_nome SET Nome = ? WHERE Numero = ?", (self.nome_procurado, self.numero_procurado))
                    self.limpa_whatts()
                    self.contato_nome.focus_force()
                else:
                    self.limpa_whatts()
                    self.contato_nome.focus_force()
                    return
            else:
                b.execute("INSERT INTO whatts_nome (Nome,Numero) VALUES (?,?);",(self.nome_procurado,self.numero_procurado,))
                self.limpa_whatts()
                messagebox.showinfo("Sucesso!!!","Numero Adicionado com sucesso!")
                self.contato_nome.focus_force()
            Banco.commit()     
            Banco.close()
        else:
            messagebox.showinfo("Erro", "Preencha os campos...")
            self.contato_nome.focus_force()
    def dell_ctt(self):
        self.nome_procurado=self.contato_nome.get()
        self.numero_procurado=self.contato_numero.get()
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()
        if self.nome_procurado and self.numero_procurado not in "":
            b.execute("SELECT * FROM whatts_nome WHERE Numero = ?", (self.numero_procurado,))
            acho=b.fetchone()
            if acho is not None:
                b.execute("DELETE FROM whatts_nome WHERE Numero = ?", (self.numero_procurado,))
                self.limpa_whatts()
                messagebox.showinfo("Sucesso!!!","Numero Apagado com sucesso!")
                self.contato_nome.focus_force()
                
            else:
                messagebox.showerror("Erro","Esse Numero Nao está salvo!")
                self.limpa_whatts()
                self.contato_nome.focus_force()

            Banco.commit()   
        else:
            self.contato_nome.focus_force()
            messagebox.showinfo("Erro", "Preencha os campos...")
        Banco.commit()
        Banco.close()
    def limpa_whatts(self):
        self.contato_nome.delete(0,END)
        self.contato_numero.delete(0,END)
    def salva(self):
        self.message=self.msm.get()
        Banco = sqlite3.connect("banco.db")
        b = Banco.cursor()
        if self.message not in "":
            b.execute("SELECT * FROM whatts_Frases WHERE frase = ?", (self.message,))
            acho=b.fetchone()
            if acho is not None:
                self.continua_whatts()
            else:
                b.execute("INSERT INTO whatts_Frases (frase) VALUES (?);",(self.message,))
                self.continua_whatts()
        
        else:
            messagebox.showinfo("Erro", "Preencha os campos...")
        Banco.commit()   
        Banco.close()
        self.msm.delete(0,END)
    def inicia(self):
        self.Serv= Service(ChromeDriverManager().install())
        self.nav=webdriver.Chrome(service=self.Serv)
        self.nav.get("https://web.whatsapp.com")

    def continua_whatts(self):
        self.lista_ctt=self.dados
        qntd_cnts=len(self.lista_ctt)
        if qntd_cnts % 5 ==0:
            qntd_blocos=qntd_cnts//5

        else:
            qntd_blocos = qntd_cnts//5+1
        for i in range(qntd_blocos):
            iinicio=i*5
            ifinal=(i+1)*5
            lista_enviar=self.lista_ctt[iinicio:ifinal]  
            for nome in lista_enviar:    
                self.nav.find_element('xpath','//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
                self.nav.find_element('xpath','//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(nome)
                self.nav.find_element('xpath','//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
                time.sleep(1)
                self.nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(self.message)
                self.nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
                time.sleep(2)
            time.sleep(2)
bomb()