from tkinter import *
import sqlite3
from datetime import date
from datetime import datetime
import time
from time import strftime 
import threading
import cadastro as cadastropy
import procurar as procurarpy
import login as loginpy
import cadastro_produtos as cadastro_produtospy
import estoque as estoquepy
import caixa as caixapy
import corte as cortepy
import relatorio as relatoriopy

class Menu():
    def __init__ (self):
        self.MenuWindow = Tk()
        self.MenuWindow.title("Sistema de Barbearia - MENU")
        self.MenuWindow.minsize(width=1200,height=600)
        self.MenuWindow.resizable(False, False)
        self.MenuCanvas = Canvas(self.MenuWindow)
        self.MenuCanvas.pack(expand=1,fill=BOTH)
        self.MenuBackground = PhotoImage(file="image/menuback.png")
        self.MenuCanvas.create_image(0,0,image=self.MenuBackground,anchor=NW)
        self.MenuCanvas.create_line(0,150,1200,150,width=3,fill="white")
        
        #VERIFICANDO O USUARIO QUE ESTA LOGADO
        self.connect = sqlite3.connect("database/config.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT usuario FROM config")
        for name in self.cursor.fetchone():
            self.UsuarioLogado = name
        self.MenuCanvas.create_text(600,50,text="Bem vindo "+str(self.UsuarioLogado),font=("Sawasdee",45,"bold"),fill="white")
        self.MenuCanvas.create_line(350,80,850,80,fill="white")
        
        ################################################################VERIFICANDO DATA E A HORA
        self.data_atual = date.today()
        if self.data_atual.day >=10 :
            self.Data = '{}/{}/{}'.format(self.data_atual.day,self.data_atual.month,self.data_atual.year)
        if self.data_atual.month>=10:
            self.Data = '{}/{}/{}'.format(self.data_atual.day,self.data_atual.month,self.data_atual.year)
        if self.data_atual.day <10 :
            self.Data = '0{}/{}/{}'.format(self.data_atual.day,self.data_atual.month,self.data_atual.year)
        if self.data_atual.month<10:
            self.Data = '{}/0{}/{}'.format(self.data_atual.day,self.data_atual.month,self.data_atual.year)
        if self.data_atual.day >=10 and self.data_atual.month>=10:
            self.Data = '{}/{}/{}'.format(self.data_atual.day,self.data_atual.month,self.data_atual.year)
        if self.data_atual.day <10 and self.data_atual.month<10:
            self.Data = '0{}/0{}/{}'.format(self.data_atual.day,self.data_atual.month,self.data_atual.year)
        self.MenuCanvas.create_text(1000,127,text=str(self.Data),font=("Times New Roman",45,"bold"),fill="white")
        self.Horario = self.MenuCanvas.create_text(600,127,text=strftime('%H:%M:%S'),font=("Times New Roman",45,"bold"),fill="white")
        self.Loop = True
        def Update():
            while self.Loop:
                time.sleep(1)
                self.MenuCanvas.itemconfigure(self.Horario,text=strftime('%H:%M:%S'))
                self.MenuCanvas.update()
        self.UpdateInfo = threading.Thread(target=Update)
        self.UpdateInfo.start()
        self.AtualDate = date.today()
        self.DiasDaSemana = ['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira','Sabádo','Domingo']
        self.NumeroDaSemana = self.AtualDate.weekday()
        self.Semana = self.DiasDaSemana[self.NumeroDaSemana]
        self.Dia = self.MenuCanvas.create_text(200,127,text=str(self.Semana),font=("Times New Roman",45,"bold"),fill="white")
        
        ##COLOCANDO A DATA ATUAL NO CONFIG
        self.cursor.execute("UPDATE config SET data_atual = ? WHERE id =?",(str(self.Data),1,))
        self.connect.commit()
        
        
        
        ######################################################################################
        ######################################################## BOTÕES E SUAS FUNCOES
        self.connect = sqlite3.connect("database/login.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT adm FROM logins WHERE nome =?",(str(self.UsuarioLogado),))
        self.login_active = []
        for active in self.cursor.fetchone():
            self.login_active.insert(0,active)
        self.connect.close()
        print(self.login_active)
        if str(self.login_active[0]) == "sim":
            def Clientes():
                self.Btn_Clientes['command']=""
                self.Btn_Produtos['command']= ""
                self.Btn_Caixa['command'] = ""
                self.Btn_Cortar['command'] = ""
                self.Btn_Relatorio['command'] = ""
                self.Btn_Deslogar['command'] = ""
                self.ClientesCanvas = Canvas(self.MenuCanvas,width=200,height=200,bg="black")
                self.MenuCanvas.create_window(600,350,window=self.ClientesCanvas)
                
                def Cadastro():
                    self.Loop = False
                    self.MenuCanvas.update()
                    self.MenuWindow.destroy()
                    cadastropy.Cadastro.__init__(self)
                self.Btn_Cadastrar = Button(self.MenuCanvas,text="CADASTRAR",font=("Arial Black",10,"bold"),fg="black",bg="blue",activebackground="#00008B",width=10,command=Cadastro)
                self.ClientesCanvas.create_window(100,50,window=self.Btn_Cadastrar)
                
                def Search():
                    self.Loop = False
                    self.MenuCanvas.update()
                    self.MenuWindow.destroy()
                    procurarpy.Search.__init__(self)
                self.Btn_Consultar = Button(self.MenuCanvas,text="CONSULTAR",font=("Arial Black",10,"bold"),fg="black",bg="blue",activebackground="#00008B",width=10,command=Search)
                self.ClientesCanvas.create_window(100,100,window=self.Btn_Consultar)
                
                def Close():
                    self.Btn_Clientes['command']=Clientes
                    self.Btn_Produtos['command']= Produtos
                    self.Btn_Caixa['command'] = Caixa
                    self.Btn_Cortar['command'] = Cortar
                    self.Btn_Relatorio['command'] = Relatorio
                    self.Btn_Deslogar['command'] = Logout
                    self.ClientesCanvas.destroy()
                self.Btn_Close = Button(self.MenuCanvas,text="FECHAR",font=("Arial Black",10,"bold"),fg="black",bg="blue",activebackground="#00008B",width=10,command=Close)
                self.ClientesCanvas.create_window(100,150,window=self.Btn_Close)
                
            self.Btn_Img1 = PhotoImage(file="image/clientes.png")    
            self.Btn_Clientes = Button(self.MenuCanvas,compound = BOTTOM,image=self.Btn_Img1,text="CLIENTES",font=("Arial Black",20,"bold"),fg="black",bg="blue",activebackground="#00008B",command=Clientes)
            self.MenuCanvas.create_window(300,280,window=self.Btn_Clientes,width=250,height=180)
            #####################################
            def Cortar():
                self.Loop = False
                self.MenuCanvas.update()
                self.MenuWindow.destroy()
                cortepy.Corte()
            
            self.Btn_Img2 = PhotoImage(file="image/tesoura.png")
            self.Btn_Cortar = Button(self.MenuCanvas,compound = BOTTOM,image=self.Btn_Img2,text="CORTAR",font=("Arial Black",20,"bold"),fg="black",bg="blue",activebackground="#00008B",command=Cortar)
            self.MenuCanvas.create_window(600,280,window=self.Btn_Cortar,width=250,height=180)
            #####################################
            def Produtos():
                self.Btn_Clientes['command']=""
                self.Btn_Produtos['command']= ""
                self.Btn_Caixa['command'] = ""
                self.Btn_Cortar['command'] = ""
                self.Btn_Relatorio['command'] = ""
                self.Btn_Deslogar['command'] = ""
                self.ProdutosCanvas = Canvas(self.MenuCanvas,width=200,height=200,bg="black")
                self.MenuCanvas.create_window(600,350,window=self.ProdutosCanvas)
                
                def CadastrarProdutos():
                    self.Loop = False
                    self.MenuCanvas.update()
                    self.MenuWindow.destroy()
                    cadastro_produtospy.Cadastro_Produtos.__init__(self)
                self.Btn_Prod_Cad = Button(self.ProdutosCanvas,text="CADASTRAR",font=("Arial Black",10,"bold"),fg="black",bg="blue",activebackground="#00008B",width=10,command=CadastrarProdutos)
                self.ProdutosCanvas.create_window(100,50,window=self.Btn_Prod_Cad)
                
                def Estoque():
                    self.Loop = False
                    self.MenuCanvas.update()
                    self.MenuWindow.destroy()
                    estoquepy.Estoque.__init__(self)
                self.Btn_Prod_Cons = Button(self.ProdutosCanvas,text="ESTOQUE",font=("Arial Black",10,"bold"),fg="black",bg="blue",activebackground="#00008B",width=10,command=Estoque)
                self.ProdutosCanvas.create_window(100,100,window=self.Btn_Prod_Cons)
                
                def CloseProdutos():
                    self.Btn_Clientes['command']=Clientes
                    self.Btn_Produtos['command']= Produtos
                    self.Btn_Caixa['command'] = Caixa
                    self.Btn_Cortar['command'] = Cortar
                    self.Btn_Relatorio['command'] = Relatorio
                    self.Btn_Deslogar['command'] = Logout
                    self.ProdutosCanvas.destroy()
                self.Btn_Prod_Close = Button(self.ProdutosCanvas,text="FECHAR",font=("Arial Black",10,"bold"),fg="black",bg="blue",activebackground="#00008B",width=10,command=CloseProdutos)
                self.ProdutosCanvas.create_window(100,150,window=self.Btn_Prod_Close)
                
            
            self.Btn_Img3 = PhotoImage(file="image/produtos.png")
            self.Btn_Produtos = Button(self.MenuCanvas,compound = BOTTOM,image=self.Btn_Img3,text="PRODUTOS",font=("Arial Black",20,"bold"),fg="black",bg="blue",activebackground="#00008B",command=Produtos)
            self.MenuCanvas.create_window(900,280,window=self.Btn_Produtos,width=250,height=180)
            ####################################
            def Caixa():
                self.Loop = False
                self.MenuCanvas.update()
                self.MenuWindow.destroy()
                caixapy.Caixa.__init__(self)
            
            self.Btn_Img4 = PhotoImage(file="image/caixa.png")
            self.Btn_Caixa = Button(self.MenuCanvas,compound = BOTTOM,image=self.Btn_Img4,text="CAIXA",font=("Arial Black",20,"bold"),fg="black",bg="blue",activebackground="#00008B",command=Caixa)
            self.MenuCanvas.create_window(300,480,window=self.Btn_Caixa,width=250,height=180)
            ####################################
            def Relatorio():
                self.Loop = False
                self.MenuCanvas.update()
                self.MenuWindow.destroy()
                relatoriopy.Relatorio.__init__(self)
                
            
            self.Btn_Img5 = PhotoImage(file="image/relatorio.png")
            self.Btn_Relatorio = Button(self.MenuCanvas,compound = BOTTOM,image=self.Btn_Img5,text="RELATÓRIO",font=("Arial Black",20,"bold"),fg="black",bg="blue",activebackground="#00008B",command=Relatorio)
            self.MenuCanvas.create_window(600,480,window=self.Btn_Relatorio,width=250,height=180)
            ####################################
            def Logout():
                self.Loop = False
                self.MenuCanvas.update()
                self.MenuWindow.destroy()
                loginpy.Login.__init__(self)
                
            self.Btn_Img6 = PhotoImage(file="image/logout.png")
            self.Btn_Deslogar = Button(self.MenuCanvas,compound = BOTTOM,image=self.Btn_Img6,text="DESLOGAR",font=("Arial Black",20,"bold"),fg="black",bg="blue",activebackground="#00008B",command=Logout)
            self.MenuCanvas.create_window(900,480,window=self.Btn_Deslogar,width=250,height=180)
        else:
            def Cortar():
                self.Loop = False
                self.MenuCanvas.update()
                self.MenuWindow.destroy()
                cortepy.Corte.__init__(self)
            
            self.Btn_Img2 = PhotoImage(file="image/tesoura.png")
            self.Btn_Cortar = Button(self.MenuCanvas,compound = BOTTOM,image=self.Btn_Img2,text="CORTAR",font=("Arial Black",20,"bold"),fg="black",bg="blue",activebackground="#00008B",command=Cortar)
            self.MenuCanvas.create_window(600,280,window=self.Btn_Cortar,width=250,height=180)
            def Logout():
                self.Loop = False
                self.MenuCanvas.update()
                self.MenuWindow.destroy()
                loginpy.Login.__init__(self)
                
            self.Btn_Img6 = PhotoImage(file="image/logout.png")
            self.Btn_Deslogar = Button(self.MenuCanvas,compound = BOTTOM,image=self.Btn_Img6,text="DESLOGAR",font=("Arial Black",20,"bold"),fg="black",bg="blue",activebackground="#00008B",command=Logout)
            self.MenuCanvas.create_window(600,480,window=self.Btn_Deslogar,width=250,height=180)
        
        
                
        
        self.MenuWindow.mainloop()
#Menu()