from tkinter import *
from tkinter import ttk
import menu as menupy
import sqlite3

class Search():
    def __init__ (self):
        self.LocalizarWindow = Tk()
        self.LocalizarWindow.title("Sistema de Barbearia - LOCALIZAR CLIENTES")
        self.LocalizarWindow.minsize(width=1200,height=600)
        self.LocalizarWindow.resizable(False,False)
        self.LocalizarCanvas = Canvas(self.LocalizarWindow)
        self.LocalizarCanvas.pack(expand=1,fill=BOTH)
        self.Background = PhotoImage(file="image/menuback.png")
        self.LocalizarCanvas.create_image(0,0,image=self.Background,anchor=NW)
        ## TITULO
        self.Localizartitle = self.LocalizarCanvas.create_text(600,70,text="LOCALIZAR CLIENTES",font=("Times New Roman",48,"bold"),fill="white")
        self.LocalizarCanvas.create_line(0,100,1200,100,width=3,fill="white")
        
        
        
        ## AREA DE BUSCA
        self.BuscaTxt = self.LocalizarCanvas.create_text(390,140,text="NOME DO CLIENTE:",font=("Times New Roman",12,"bold"),fill="white")
        self.BuscaCampo = ttk.Combobox(self.LocalizarCanvas,width=30,values=[''])
        self.LocalizarCanvas.create_window(610,140,window=self.BuscaCampo)
        
        ## BANCO DE DADOS
        self.connect = sqlite3.connect("database/clientes.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT id FROM clientes")
        self.Ids = self.cursor.fetchall()
        self.connect.close()                      
        self.connect = sqlite3.connect("database/clientes.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT nome FROM clientes")
        self.ClientesLista = []
        self.IdsUsers = 0
        while self.IdsUsers<len(self.Ids):
            for cliente in self.cursor.fetchone():
                self.ClientesLista.append(cliente)
                self.IdsUsers +=1        
        self.ClientesLista.sort()
        self.BuscaCampo['values'] = self.ClientesLista
            
        self.connect.close()
            
        def ClienteBusca():
            self.connect = sqlite3.connect("database/clientes.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT * FROM clientes WHERE nome = ?",(self.BuscaCampo.get(),))
            self.SearchResult = []
            for i in self.cursor.fetchone():
                self.SearchResult.append(i)
                print(self.SearchResult)
            self.connect.close()
            self.NomeLabel['text'] = self.SearchResult[1]
            self.TelefoneLabel['text'] = str(self.SearchResult[2])
            self.NascimentoLabel['text'] = str(self.SearchResult[3])+" - "+self.SearchResult[4]+" - "+str(self.SearchResult[5])
            self.ServicoLabel['text'] = self.SearchResult[6]
            self.CorteLabel['text'] = str(self.SearchResult[8])
            self.LocalizarCanvas.update()
                

            
            
        self.Button_Search = Button(self.LocalizarCanvas,text="BUSCAR",width=10,bg="blue",fg="white",activebackground="#00008B",command=ClienteBusca)
        self.LocalizarCanvas.create_window(810,140,window=self.Button_Search)
        
        #RETORNO DA BUSCA
        self.NomeTxt = self.LocalizarCanvas.create_text(430,200,text="NOME:",font=("Times New Roman",12,"bold"),fill="white")
        self.NomeLabel = ttk.Label(self.LocalizarCanvas,width=30,text="",anchor="center")
        self.LocalizarCanvas.create_window(614,200,window=self.NomeLabel)
        self.TelefoneTxt = self.LocalizarCanvas.create_text(410,250,text="TELEFONE:",font=("Times New Roman",12,"bold"),fill="white")
        self.TelefoneLabel = ttk.Label(self.LocalizarCanvas,width=30,text="",anchor="center")
        self.LocalizarCanvas.create_window(614,250,window=self.TelefoneLabel)
        self.NascimentoTxt = self.LocalizarCanvas.create_text(400,300,text="NASCIMENTO:",font=("Times New Roman",12,"bold"),fill="white")
        self.NascimentoLabel = ttk.Label(self.LocalizarCanvas,width=30,text="",anchor="center")
        self.LocalizarCanvas.create_window(614,300,window=self.NascimentoLabel)
        self.ServicoTxt = self.LocalizarCanvas.create_text(413,350,text="SERVIÇO:",font=("Times New Roman",12,"bold"),fill="white")
        self.ServicoLabel = ttk.Label(self.LocalizarCanvas,width=30,text="",anchor="center")
        self.LocalizarCanvas.create_window(614,350,window=self.ServicoLabel)
        self.CorteTxt = self.LocalizarCanvas.create_text(390,400,text="CORTES FEITOS:",font=("Times New Roman",12,"bold"),fill="white")
        self.CorteLabel = ttk.Label(self.LocalizarCanvas,width=30,text="",anchor="center")
        self.LocalizarCanvas.create_window(614,400,window=self.CorteLabel)
        self.UltimoCorteTxt = self.LocalizarCanvas.create_text(390,450,text="ULTIMO CORTE:",font=("Times New Roman",12,"bold"),fill="white")
        self.UltimoCorteLabel = ttk.Label(self.LocalizarCanvas,width=30,text="",anchor="center")
        self.LocalizarCanvas.create_window(614,450,window=self.UltimoCorteLabel)
        
        #BOTOES E FUNCOES
        def Editar():
            ttk.Label.destroy(self.NascimentoLabel)
            ttk.Label.destroy(self.CorteLabel)
            ttk.Label.destroy(self.UltimoCorteLabel)
            self.NomeLabel = Entry(self.LocalizarCanvas,width=30)
            self.LocalizarCanvas.create_window(614,200,window=self.NomeLabel)
            self.TelefoneLabel = Entry(self.LocalizarCanvas,width=30)
            self.LocalizarCanvas.create_window(614,250,window=self.TelefoneLabel)
            self.NascimentoDiaLabel = Entry(self.LocalizarCanvas,width=5)
            self.LocalizarCanvas.create_window(510,300,window=self.NascimentoDiaLabel)
            self.NascimentoMesLabel = Entry(self.LocalizarCanvas,width=10)
            self.LocalizarCanvas.create_window(600,300,window=self.NascimentoMesLabel)
            self.NascimentoAnoLabel = Entry(self.LocalizarCanvas,width=10)
            self.LocalizarCanvas.create_window(700,300,window=self.NascimentoAnoLabel)
            self.ServicoLabel = Entry(self.LocalizarCanvas,width=30)
            self.LocalizarCanvas.create_window(614,350,window=self.ServicoLabel)
            def Salvar():
                self.connect = sqlite3.connect("database/clientes.db")
                self.cursor = self.connect.cursor()
                self.cursor.execute("UPDATE clientes SET nome=?, telefone=?, dia=?, mes=?, ano=?, servico=? WHERE nome=?",(self.NomeLabel.get(),self.TelefoneLabel.get(),self.NascimentoDiaLabel.get(),self.NascimentoMesLabel.get(),self.NascimentoAnoLabel.get(),self.ServicoLabel.get(),self.BuscaCampo.get(),))
                self.connect.commit()
                self.connect.close()                                  
                self.ButtonEdit['command'] = ""
                self.ButtonDelete['command'] = ""
                self.ButtonVoltar['command'] = ""
                self.Button_Search['command'] = ""
                self.Salvo = Canvas(self.LocalizarCanvas,width=300,height=300)
                self.LocalizarCanvas.create_window(600,300,window=self.Salvo)
                self.Salvo.create_text(150,100,text="SALVO COM SUCESSO!",font=("Arial",16,"bold"),fill="red")
                def OK():
                    self.LocalizarWindow.destroy()
                    Search()         
                self.ButtonOK = Button(self.Salvo,text="OK",width=10,command=OK)
                self.Salvo.create_window(150,200,window=self.ButtonOK)
            self.ButtonSave = Button(self.LocalizarCanvas,text="SALVAR",width=10,bg="blue",fg="white",activebackground="#00008B",command=Salvar)
            self.LocalizarCanvas.create_window(1000,300,window=self.ButtonSave)
        
        def Deletar():
            self.connect = sqlite3.connect("database/clientes.db")
            self.cursor = self.connect.cursor()
            self.connect.execute("DELETE FROM clientes WHERE nome = ?",(self.BuscaCampo.get(),))
            self.connect.commit()
            self.connect.close()
            self.Salvo = Canvas(self.LocalizarCanvas,width=300,height=300)
            self.LocalizarCanvas.create_window(600,300,window=self.Salvo)
            self.Salvo.create_text(150,100,text="DELETADO COM SUCESSO!",font=("Arial",16,"bold"),fill="red")
            def OK():
                self.LocalizarWindow.destroy()
                Search()         
            self.ButtonOK = Button(self.Salvo,text="OK",width=10,command=OK)
            self.Salvo.create_window(150,200,window=self.ButtonOK)
        
        def Voltar():
            self.LocalizarWindow.destroy()
            menupy.Menu.__init__(self)

        self.ButtonEdit = Button(self.LocalizarCanvas,text="EDITAR",width=10,bg="blue",fg="white",activebackground="#00008B",command=Editar)
        self.LocalizarCanvas.create_window(450,550,window=self.ButtonEdit)
        self.ButtonDelete = Button(self.LocalizarCanvas,text="DELETAR",width=10,bg="blue",fg="white",activebackground="#00008B",command=Deletar)
        self.LocalizarCanvas.create_window(600,550,window=self.ButtonDelete)
        self.ButtonVoltar = Button(self.LocalizarCanvas,text="VOLTAR",width=10,bg="blue",fg="white",activebackground="#00008B",command=Voltar)
        self.LocalizarCanvas.create_window(750,550,window=self.ButtonVoltar)
  
        
        
        
        self.LocalizarWindow.mainloop()
#Search()