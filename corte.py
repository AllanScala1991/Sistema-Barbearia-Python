from tkinter import *
from tkinter import ttk
import sqlite3
import menu as menupy



class Corte ():
    def __init__(self):
        self.CorteJanela = Tk()
        self.CorteJanela.title("Sistema de Barbearia - CORTES")
        self.CorteJanela.minsize(width=1200, height=600)
        self.CorteJanela.resizable(False,False)
        self.CorteCanvas = Canvas(self.CorteJanela)
        self.CorteCanvas.pack(expand=1,fill=BOTH)
        self.CorteCanvasground = PhotoImage(file="image/menuback.png")
        self.CorteCanvas.create_image(0,0,image=self.CorteCanvasground,anchor=NW)
        self.Cadeira_image = PhotoImage(file="image/cadeira.png")
        self.CorteCanvas.create_image(1000,350,image=self.Cadeira_image)
        self.azul = PhotoImage(file="image/azul2.png")
        self.CorteCanvas.create_image(720,385,image=self.azul)
        ## CORTES
        self.CorteCanvastitle = self.CorteCanvas.create_text(600,100,text="CORTES",font=("Times New Roman",48,"bold"),fill="white")
        self.CorteCanvas.create_line(0,130,1200,130,width=3,fill="white")
        
        ##CONECTANDO AO BANCO DE DADOS
        self.connect = sqlite3.connect("database/cortes.db")
        self.cursor = self.connect.cursor()
        
        self.connect2 = sqlite3.connect("database/clientes.db")
        self.cursor2  = self.connect2.cursor()
        
        self.connect3 = sqlite3.connect("database/produtos.db")
        self.cursor3  = self.connect3.cursor()
        
        self.connect4 = sqlite3.connect("database/config.db")
        self.cursor4  = self.connect4.cursor()
        
        ## TEXTOS E LABELS
        self.cursor2.execute("SELECT id FROM clientes")
        self.Todos_ids = self.cursor2.fetchall()
        self.cursor2.execute("SELECT nome FROM clientes")
        self.Clientes = []
        self.loop = 0
        while self.loop<len(self.Todos_ids):
            for cliente in self.cursor2.fetchone():
                self.Clientes.append(cliente)
                self.loop +=1
        self.Clientes.sort()
        self.CorteCanvas.create_text(50,250,text="CLIENTE: ",font=("Times New Roman",10,"bold"),fill="white")
        self.nomes_clientes = ttk.Combobox(self.CorteCanvas,values=[],width=25,state='readonly')
        self.CorteCanvas.create_window(350,250,window=self.nomes_clientes)
        self.nomes_clientes['values']=self.Clientes
        
        self.total = 0
        self.CorteCanvas.create_text(720,300,text="VALOR A PAGAR: ",font=("Times New Roman",14,"bold"),fill="white")
        self.valor_a_pagar = self.CorteCanvas.create_text(720,380,text=str(self.total),font=("Times New Roman",40,"bold"),fill="white")
        self.CorteCanvas.create_rectangle(590,320,850,450,outline="red")

        
        #BOTOES E SUAS FUNCOES
        def Selecionar():
            self.cursor4.execute("SELECT * FROM config")
            self.User_and_Date = []
            for info in self.cursor4.fetchone():
                self.User_and_Date.append(info)   
            self.cursor.execute("INSERT INTO cortes (cliente,valor,usuario,data_atual) VALUES (?,?,?,?)",(self.nomes_clientes.get(),0,self.User_and_Date[1],self.User_and_Date[2],))
            self.connect.commit()
            self.cursor3.execute("SELECT id FROM produtos")
            self.Prod_ids = self.cursor3.fetchall()
            self.cursor3.execute("SELECT nome FROM produtos")
            self.Produtos_Cadastrados = []
            self.Prod_loop = 0
            while self.Prod_loop<len(self.Prod_ids):
                for produto in self.cursor3.fetchone():
                    self.Produtos_Cadastrados.append(produto)
                    self.Prod_loop +=1
            self.CorteCanvas.create_text(95,300,text="PRODUTOS / SERVIÇOS: ",font=("Times New Roman",10,"bold"),fill="white")
            self.produtos = ttk.Combobox(self.CorteCanvas,values=[],width=25,state='readonly')
            self.CorteCanvas.create_window(350,300,window=self.produtos)
            self.produtos['value'] = self.Produtos_Cadastrados
                 
            self.Box_Produtos = Text(self.CorteCanvas)
            self.Box_Produtos.config(width=40,height=15)
            self.CorteCanvas.create_window(350,450,window=self.Box_Produtos)
            self.CorteCanvas.create_text(100,350,text="SERVIÇOS ADQUIRIDOS: ",font=("Times New Roman",10,"bold"),fill="white")
            
        
        self.Btn_Selecionar = Button(self.CorteCanvas,text="SELECIONAR",width=10,bg="blue",fg="white",activebackground="#00008B",command=Selecionar)
        self.CorteCanvas.create_window(537,250,window=self.Btn_Selecionar)

        self.Meus_Produtos = []
        
        
        def Adicionar():
            if self.nomes_clientes.get() != "":
                
                self.produto_escolhido = self.produtos.get()
                self.cursor3.execute("SELECT valor FROM produtos WHERE nome = ?",(self.produto_escolhido,))
                self.cursor.execute("SELECT valor FROM cortes WHERE cliente = ?",(self.nomes_clientes.get(),))
                self.valor_produto = []
                self.valor_atual=[]
                for valor in self.cursor3.fetchone():
                    self.valor_produto.append(valor) 
                for valor2 in self.cursor.fetchone():
                    self.valor_atual.append(valor2)
                self.valor_atualizado = self.valor_produto[0] + self.valor_atual[0]
                self.Meu_id = []
                self.cursor.execute("SELECT id FROM cortes WHERE cliente = ?",(self.nomes_clientes.get(),))
                for ids in self.cursor.fetchall():
                    self.Meu_id.insert(0,ids)
                self.cursor.execute("UPDATE cortes SET valor = ? WHERE id=?",(self.valor_atualizado,self.Meu_id[0][0],))   
                self.connect.commit()       
                self.CorteCanvas.itemconfigure(self.valor_a_pagar,text=str(self.valor_atualizado))
                self.Box_Produtos.insert(END,self.produto_escolhido +" " +"\n")
                self.Meus_Produtos.append(self.produto_escolhido) 
                self.valor_produto.clear()
                self.valor_atual.clear()
                
                

            else:
                self.CorteCanvas.itemconfigure(self.valor_a_pagar,text="ERRO , PREENCHA TODOS OS CAMPOS")
            
            
        self.Btn_Adicionar= Button(self.CorteCanvas,text="+",width=1,bg="blue",fg="white",activebackground="#00008B",command=Adicionar)
        self.CorteCanvas.create_window(550,300,window=self.Btn_Adicionar)
        
        def Confirmar():
            self.cursor.execute("SELECT id FROM cortes WHERE cliente = ?",(self.nomes_clientes.get(),))
            self.Meu_id2 = []
            for ids2 in self.cursor.fetchall():
                self.Meu_id2.insert(0,ids2)
            self.cursor.execute("UPDATE cortes SET produtos = ? WHERE id = ?",(self.Box_Produtos.get(1.0,END),self.Meu_id2[0][0],))
            self.connect.commit()
            self.cursor2.execute("SELECT cortes FROM clientes WHERE nome=?",(self.nomes_clientes.get(),))
            self.valor_atual=[]
            for vlr in self.cursor2.fetchone():
                self.valor_atual.append(vlr)
            self.novo_valor = self.valor_atual[0]
            self.novo_valor +=1
            self.cursor2.execute("UPDATE clientes SET cortes = ?, ultimocorte = ? WHERE nome=?",(int(self.novo_valor),self.User_and_Date[2],self.nomes_clientes.get(),))
            self.connect2.commit()
            self.connect.close()
            self.connect2.close()
            self.connect3.close()
            self.connect4.close()
            self.CorteJanela.destroy()
            Corte()
        self.Btn_Confirmar= Button(self.CorteCanvas,text="CONFIRMAR",width=10,bg="red",fg="white",activebackground="yellow",command=Confirmar)
        self.CorteCanvas.create_window(720,500,window=self.Btn_Confirmar)
        
        def Voltar():
            self.connect.close()
            self.connect2.close()
            self.connect3.close()
            self.connect4.close()
            self.CorteJanela.destroy()
            menupy.Menu.__init__(self)
        self.Btn_Voltar= Button(self.CorteCanvas,text="VOLTAR",width=10,bg="red",fg="white",activebackground="yellow",command=Voltar)
        self.CorteCanvas.create_window(720,550,window=self.Btn_Voltar)
        
        self.CorteJanela.mainloop()
#Corte()



