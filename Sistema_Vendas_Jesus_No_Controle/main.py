import sqlite3
from tkinter import ttk
from tkinter import *
from Login import *
import tkinter as tk


class Main_Principal(Login):
    def __init__(self):
        self.janela1()

    buttons = []
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='users';"
    )
    table_exists = cursor.fetchone()
    if not table_exists:
        conn.execute("""CREATE TABLE users (username, password);""")

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='Estoque';" 
    )
    table_exists = cursor.fetchone()

    if not table_exists:
        conn.execute(
            "CREATE TABLE Estoque (Codigo INTEGER,PRODUTO integer NOT NULL,PREÇO integer NOT NULL,custo INTEGER,QTDE integer NOT NULL)"
        )
        conn.execute(
            "INSERT INTO Estoque (Codigo,PRODUTO,PREÇO,custo,QTDE) VALUES (?,?,?,?,?)",
            (
                1,
                1,
                1,
                1,
                1,
            ),
        )
        conn.commit()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='Venda';"
    )
    table_exists = cursor.fetchone()
    if not table_exists:
        conn.execute(
            "CREATE TABLE Venda (Id INTEGER PRIMARY KEY AUTOINCREMENT,Cliente integer ,Valor integer ,Status integer,deb INTEGER,cre INTEGER,pix INTEGER,dim INTEGER,troco INTEGER,desc INTEGER)"
        )
        Status = "Aberto"
        conn.execute(
            "INSERT INTO Venda (Cliente, Status,deb,cre,dim,pix,Desc) VALUES (?, ?, ?, ?,?, ?,?)",
            (0, Status, 0, 0, 0, 0,0),
        )
        conn.commit()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='vendas_dados';"
    )
    table_exists = cursor.fetchone()
    if not table_exists:
        conn.execute(
            "CREATE TABLE vendas_dados (Id_item INTEGER PRIMARY KEY AUTOINCREMENT,Id_venda Integer Not Null,Cdg INTEGER, PRODUTO integer , Quantidade INTEGER,PREÇO integer,Preco_quant INTEGER)"
        )
        conn.commit()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='Pessoas';"
    )
    table_exists = cursor.fetchone()
    if not table_exists:
        conn.execute(
            "CREATE TABLE Pessoas (Codigo_pessoa INTEGER PRIMARY KEY AUTOINCREMENT,nome INTEGER,tell INTEGER,gmail INTEGER,nome_fake INTEGER,cpf INTEGER,rg INTEGER,cnpj INTEGER,bairro INTEGER,rua INTEGER,n_cs,complemento INTEGER)"
        )
        conn.commit()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='whatts_nome';"
    )
    table_exists = cursor.fetchone()
    if not table_exists:
        conn.execute(
            "CREATE TABLE whatts_nome (Cdg_pessoa INTEGER PRIMARY KEY AUTOINCREMENT,Nome INTEGER, Numero INTEGER)"
        )
        conn.execute(
            "INSERT INTO whatts_nome (Nome,Numero) VALUES (?, ?)",
            ("(voc",0)
        )
        conn.commit()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='whatts_Frases';"
    )
    table_exists = cursor.fetchone()
    if not table_exists:
        conn.execute(
            "CREATE TABLE whatts_Frases (Cdg_frase INTEGER PRIMARY KEY AUTOINCREMENT,frase INTERGE)"
        )
        conn.commit()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='ponto';"
    )
    table_exists = cursor.fetchone()
    if not table_exists:
        conn.execute(
            "CREATE TABLE ponto (funcionario INTERGE,data INTERGE,entri_manha INTERGE,sai_manha INTERGE,dia_semana INTERGE,entri_tarde INTERGE,sai_tarde INTERGE,salario INTERGE,hora INTERGE)"
        )
        conn.commit()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='empresa';"
    )
    table_exists = cursor.fetchone()
    if not table_exists:
        conn.execute("""CREATE TABLE empresa (nome TEXT,gmail TEXT,cell TEXT,cnpj TEXT,iee TEXT,pix TEXT,endereco TEXT,nu_endereco TEXT,bairro TEXT,complemento TEXT,estado TEXT,cidade TEXT,cep TEXT);""")


    conn.close()



Main_Principal()
