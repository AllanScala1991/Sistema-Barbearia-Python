from tkinter import *
import sqlite3
import menu as menupy

class Cadastro_Produtos():
    def __init__ (self):
        self.ProdutosWindow = Tk()
        self.ProdutosWindow.title("Sistema de Barbearia - CADASTRO DE PRODUTOS")
        self.ProdutosWindow.minsize(width=1200,height=600)
        self.ProdutosWindow.resizable(False,False)
        self.ProdutoCanvas = Canvas(self.ProdutosWindow)
        self.ProdutoCanvas.pack(expand=1,fill=BOTH)
        self.Background = PhotoImage(file="image/menuback.png")
        self.ProdutoCanvas.create_image(0,0,image=self.Background,anchor=NW)
        self.Img1 = PhotoImage(file="image/produtos2.png")
        self.ProdutoCanvas.create_image(850,300,image=self.Img1)
        self.salvo_sucesso = self.ProdutoCanvas.create_text(600,550,text="",font=("Times New Roman",15,"bold"),fill="red")
        ## TITULO
        self.Produtostitle = self.ProdutoCanvas.create_text(600,100,text="CADASTRO DE PRODUTOS",font=("Times New Roman",48,"bold"),fill="white")
        self.ProdutoCanvas.create_line(0,150,1200,150,width=3,fill="white")
        
        ## CAMPOS DE CADASTRO
        self.txt_nome = self.ProdutoCanvas.create_text(280,200,text="NOME DO PRODUTO:",font=("Times New Roman",12,'bold'),fill="white")
        self.entry_nome = Entry(self.ProdutoCanvas,width=20,justify="center")
        self.ProdutoCanvas.create_window(480,200,window=self.entry_nome)
        
        self.txt_descricao = self.ProdutoCanvas.create_text(280,250,text="DESCRIÇÃO DO PRODUTO:",font=("Times New Roman",12,'bold'),fill="white")
        self.entry_descricao = Entry(self.ProdutoCanvas,width=20,justify="center")
        self.ProdutoCanvas.create_window(480,250,window=self.entry_descricao)
    
        
        self.txt_valorV = self.ProdutoCanvas.create_text(280,300,text="VALOR:",font=("Times New Roman",12,'bold'),fill="white")
        self.entry_valorV = Entry(self.ProdutoCanvas,width=10,justify="center")
        self.ProdutoCanvas.create_window(480,300,window=self.entry_valorV)
        self.ProdutoCanvas.create_text(590,300,text="* CAMPO OBRIGATÓRIO",font=("Times New Roman",8,'bold'),fill="yellow")
             

        
        ## BOTÕES E FUNÇÕES
        def Salvar():
            try:
                self.venda = float(self.entry_valorV.get().replace(",","."))#TRANSFORMA A VIRGULA DIGITADA PELO USUARIO EM PONTO
                self.connect = sqlite3.connect("database/produtos.db")
                self.cursor = self.connect.cursor()
                self.cursor.execute("INSERT INTO produtos (nome,descricao,valor) VALUES (?,?,?)",
                                    (self.entry_nome.get(),self.entry_descricao.get(),self.venda,))
                self.connect.commit()
                self.connect.close()
                self.ProdutoCanvas.itemconfigure(self.salvo_sucesso,text="SALVO COM SUCESSO!")
                self.entry_nome.delete(0,END)
                self.entry_descricao.delete(0,END)
                self.entry_valorV.delete(0,END)
      
            except:
                self.ProdutoCanvas.itemconfigure(self.salvo_sucesso,text="PREENCHA TODOS OS CAMPOS CORRETAMENTE!")
            
            
        
        def Limpar():
            self.entry_nome.delete(0,END)
            self.entry_descricao.delete(0,END)
            self.entry_valorV.delete(0,END)
            self.ProdutoCanvas.itemconfigure(self.salvo_sucesso,text="")
        
        def Voltar():
            self.ProdutosWindow.destroy()
            menupy.Menu.__init__(self)
        
        self.btn_salvar = Button(self.ProdutoCanvas,text="SALVAR",font=("Arial Black",10,"bold"),fg="black",bg="blue",activebackground="#00008B",width=10,command=Salvar)
        self.ProdutoCanvas.create_window(450,500,window=self.btn_salvar)
        self.btn_limpar = Button(self.ProdutoCanvas,text="LIMPAR",font=("Arial Black",10,"bold"),fg="black",bg="blue",activebackground="#00008B",width=10,command=Limpar)
        self.ProdutoCanvas.create_window(600,500,window=self.btn_limpar)
        self.btn_voltar = Button(self.ProdutoCanvas,text="VOLTAR",font=("Arial Black",10,"bold"),fg="black",bg="blue",activebackground="#00008B",width=10,command=Voltar)
        self.ProdutoCanvas.create_window(750,500,window=self.btn_voltar)
        
        
        
        self.ProdutosWindow.mainloop()
#Cadastro_Produtos()