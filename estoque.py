from tkinter import *
from tkinter import ttk
import sqlite3
import menu as menupy

class Estoque():
    def __init__(self):
        self.EstoqueWindow = Tk()
        self.EstoqueWindow.title("Sistema de Barbearia - ESTOQUE")
        self.EstoqueWindow.minsize(width=1200,height=600)
        self.EstoqueWindow.resizable(False,False)
        self.EstoqueCanvas = Canvas(self.EstoqueWindow)
        self.EstoqueCanvas.pack(expand=1,fill=BOTH)
        self.Background = PhotoImage(file="image/menuback.png")
        self.EstoqueCanvas.create_image(0,0,image=self.Background,anchor=NW)
        
        ## TITULO
        self.Estoquetitle = self.EstoqueCanvas.create_text(600,125,text="ESTOQUE",font=("Times New Roman",48,"bold"),fill="white")
        self.EstoqueCanvas.create_line(0,150,1200,150,width=3,fill="white")
        self.Estoquetitle2 = self.EstoqueCanvas.create_text(600,230,text="PRODUTOS CADASTRADOS",font=("Times New Roman",18,"bold"),fill="white")
         
        ## BOTOES E LABELS
        self.txt_estoque = self.EstoqueCanvas.create_text(400,180,text="TODOS OS PRODUTOS:",font=("Times New Roman",12,"bold"),fill="white")
        self.select_estoque = ttk.Combobox(self.EstoqueCanvas,values=[],width=20,state='readonly')
        self.EstoqueCanvas.create_window(600,180,window=self.select_estoque)
        
       
        
      
        
        def Voltar():
            self.EstoqueWindow.destroy()
            menupy.Menu.__init__(self)
        
        def Editar():
            self.EditarWindow = Tk()
            self.EditarWindow.title("SISTEMA DE BARBEARIA - EDITAR PRODUTO")
            self.EditarWindow.minsize(width=500, height=500)
            self.EditarWindow.resizable(False,False)
            self.EditarCanvas = Canvas(self.EditarWindow,bg="black")
            self.EditarCanvas.pack(expand=1,fill=BOTH)
            self.selecione_txt = self.EditarCanvas.create_text(250,30,text="SELECIONE O PRODUTO:",font=("Times New Roman",12,"bold"),fill="white")
            self.produto_combobox = ttk.Combobox(self.EditarCanvas,values=[],width=20)
            self.EditarCanvas.create_window(250,60,window=self.produto_combobox)
            self.produto_combobox['values'] = self.produtos
            self.busca_lista = []
            def Buscar():
                self.nome_entry.delete(0,END)
                self.descricao_entry.delete(0,END)
                self.valorv_entry.delete(0,END)
                self.connect = sqlite3.connect("database/produtos.db")
                self.cursor = self.connect.cursor()
                self.cursor.execute("SELECT * FROM produtos WHERE nome=?",(self.produto_combobox.get(),))
                for names in self.cursor.fetchone():
                    self.busca_lista.append(names)
                self.connect.close()
                self.nome_entry.insert(0,str(self.busca_lista[1]))
                self.descricao_entry.insert(0,str(self.busca_lista[2]))
                self.valorv_entry.insert(0,str(self.busca_lista[3]))
               
                self.busca_lista.clear()
            
                
                
            self.btn_buscar = Button(self.EditarCanvas,text="BUSCAR",font=("Impact",10,"bold"),fg="black",bg="red",activebackground="#B22222",width=10,command=Buscar)
            self.EditarCanvas.create_window(250,90,window=self.btn_buscar)
            self.nome_txt = self.EditarCanvas.create_text(250,120,text="NOME:",font=("Times New Roman",12,"bold"),fill="white")
            self.nome_entry = Entry(self.EditarCanvas,width=20,justify="center")
            self.EditarCanvas.create_window(250,150,window=self.nome_entry)
            self.descricao_txt = self.EditarCanvas.create_text(250,180,text="DESCRIÇÃO:",font=("Times New Roman",12,"bold"),fill="white")
            self.descricao_entry = Entry(self.EditarCanvas,width=20,justify="center")
            self.EditarCanvas.create_window(250,210,window=self.descricao_entry)
            self.valorv_txt = self.EditarCanvas.create_text(250,240,text="VALOR DE VENDA:",font=("Times New Roman",12,"bold"),fill="white")
            self.valorv_entry = Entry(self.EditarCanvas,width=20,justify="center")
            self.EditarCanvas.create_window(250,270,window=self.valorv_entry)
            
            def Salvar():
                try:
                    self.connect = sqlite3.connect("database/produtos.db")
                    self.cursor = self.connect.cursor()
                    self.cursor.execute("UPDATE produtos SET nome=?,descricao=?,valor=? WHERE nome=?",
                                        (self.nome_entry.get(),self.descricao_entry.get(),self.valorv_entry.get(),self.produto_combobox.get(),))
                    self.connect.commit()
                    self.connect.close()
                    self.EditarWindow.destroy()
                    self.EstoqueWindow.destroy()
                    Estoque()
                except:
                    self.erro = Tk()
                    self.erro.title("ERRO - TENTE NOVAMENTE")
                    self.erro.minsize(width=300,height=300)
                    self.erro.resizable(False,False)
                    self.erro_canvas = Canvas(self.erro)
                    self.erro_canvas.pack(expand=1,fill=BOTH)
                    self.erro_canvas.create_text(150,150,text="ERRO INESPERADO, TENTE NOVAMENTE!")
                    def OK():
                        self.erro.destroy()
                    self.btn_OK = Button(self.erro_canvas,text="OK")
                    self.erro_canvas.create_window(150,200,window=self.btn_OK,command=OK)
                    self.erro.mainloop()
            def Cancelar():
                self.EditarWindow.destroy()
            self.btn_salvando = Button(self.EditarCanvas,text="SALVAR",font=("Impact",10,"bold"),fg="black",bg="red",activebackground="#B22222",width=10,command=Salvar)
            self.EditarCanvas.create_window(180,450,window=self.btn_salvando)
            self.btn_cancelar = Button(self.EditarCanvas,text="CANCELAR",font=("Impact",10,"bold"),fg="black",bg="red",activebackground="#B22222",width=10,command=Cancelar)
            self.EditarCanvas.create_window(320,450,window=self.btn_cancelar)
            self.EditarWindow.mainloop()
                
        self.voltar = Button(self.EstoqueCanvas,text="VOLTAR",font=("Arial Black",10,"bold"),fg="black",bg="blue",activebackground="#00008B",width=10,command=Voltar)
        self.EstoqueCanvas.create_window(1100,550,window=self.voltar)
        self.editar = Button(self.EstoqueCanvas,text="EDITAR",font=("Arial Black",10,"bold"),fg="black",bg="blue",activebackground="#00008B",width=10,command=Editar)
        self.EstoqueCanvas.create_window(1100,500,window=self.editar)
        
        

        ## BANCO DE DADOS
        self.connect = sqlite3.connect("database/produtos.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT id FROM produtos")
        self.Ids = []
        for i in self.cursor.fetchall():
            self.Ids.append(i)
            
        self.cursor.execute("SELECT nome FROM produtos")
        self.loop = 0
        self.produtos = []
        while self.loop<len(self.Ids):
            for j in self.cursor.fetchone():
                self.produtos.append(j)
                self.loop += 1
        self.select_estoque['values'] = self.produtos
        
        
        ##SCROLL DA AREA DE REGISTROS
        self.scroll = Scrollbar(self.EstoqueCanvas,bg="black")
        self.EstoqueCanvas.create_window(935,415,window=self.scroll,width=15,height=348) 
        
        ##AREA DE REGISTROS
        self.registros = Text(self.EstoqueCanvas,yscrollcommand=self.scroll.set,bg="black",fg="white")
        self.registros.config(width=80,height=20)
        self.scroll.config(command=self.registros.yview)
        self.EstoqueCanvas.create_window(600,415,window=self.registros)
        
        self.numero_voltas = 0
        self.id_inicial = 1
        self.posicao_inicial = 0
        self.produtos_cadastrados = []
        while self.numero_voltas<len(self.Ids):
            self.cursor.execute("SELECT * FROM produtos WHERE id=?",(self.id_inicial,))
            for produto11 in self.cursor.fetchone():
                self.produtos_cadastrados.append(produto11)
            self.registros.insert(END, "                              CÓDIGO - "+str(self.produtos_cadastrados[0])+"\n")
            self.registros.insert(END, "                              PRODUTO - "+str(self.produtos_cadastrados[1])+"\n")
            self.registros.insert(END, "                              DESCRIÇÃO - "+str(self.produtos_cadastrados[2])+"\n")
            self.Conversao2 = str(self.produtos_cadastrados[3])
            self.registros.insert(END, "                              VALOR - "+str(self.Conversao2.replace(".",","))+"\n")
            self.registros.insert(END, "______________________________________________________________________________""\n\n")
            self.posicao_inicial +=1
            self.id_inicial+=1
            self.numero_voltas+=1
            self.produtos_cadastrados.clear()
        self.connect.close()
        
        self.EstoqueWindow.mainloop()
#Estoque()