from tkinter import *
from tkinter import ttk
import menu as menupy
import sqlite3


class Cadastro():
    def __init__ (self):
        self.CadastroWindow = Tk()
        self.CadastroWindow.title("Sistema de Barbearia - CADASTRO DE CLIENTES")
        self.CadastroWindow.minsize(width=1200,height=600)
        self.CadastroWindow.resizable(False,False)
        self.CadastroCanvas = Canvas(self.CadastroWindow)
        self.CadastroCanvas.pack(expand=1,fill=BOTH)
        self.Background = PhotoImage(file="image/menuback.png")
        self.CadastroCanvas.create_image(0,0,image=self.Background,anchor=NW)
        ############## TITULO
        self.Cadastrotitle = self.CadastroCanvas.create_text(600,100,text="CADASTRO DE CLIENTES",font=("Times New Roman",48,"bold"),fill="white")
        self.CadastroCanvas.create_line(0,150,1200,150,width=3,fill="white")
        
        ############# CAMPOS E LABEL DA AREA DE CADASTRO
        self.NomeTxt = self.CadastroCanvas.create_text(400,200,text="NOME DO CLIENTE:",font=("Times New Roman",12,'bold'),fill="white")
        self.NomeEntry = Entry(self.CadastroCanvas,width=30,fg="black")
        self.CadastroCanvas.create_window(620,200,window=self.NomeEntry)
        self.TelefoneTxt = self.CadastroCanvas.create_text(400,250,text="TELEFONE:",font=("Times New Roman",12,'bold'),fill="white")
        self.TelefoneEntry = Entry(self.CadastroCanvas,width=30,fg="black")
        self.CadastroCanvas.create_window(620,250,window=self.TelefoneEntry)
        self.NascimentoTxt = self.CadastroCanvas.create_text(380,300,text="DATA DE NASCIMENTO:",font=("Times New Roman",12,'bold'),fill="white")
        self.NascimentoDia =  Spinbox(self.CadastroCanvas,width=3,from_=1, to=31)
        self.CadastroCanvas.create_window(518,300,window=self.NascimentoDia)   
        self.NascimentoMes =  Spinbox(self.CadastroCanvas,width=8,values=('Janeiro','Fevereiro','Março','Abril','Maio',
                                                                          'Junho','Julho','Agosto','Setembro','Outubro',
                                                                          'Novembro','Dezembro'))
        self.CadastroCanvas.create_window(600,300,window=self.NascimentoMes)    
        self.NascimentoAno =  Spinbox(self.CadastroCanvas,width=8,from_=1900, to=2050)
        self.CadastroCanvas.create_window(700,300,window=self.NascimentoAno) 
        self.ServicoTxt = self.CadastroCanvas.create_text(400,350,text="TIPO DE SERVIÇO:",font=("Times New Roman",12,'bold'),fill="white")
        self.Servico1 =  ttk.Combobox(self.CadastroCanvas,values=['Barba','Cabelo','Barba & Cabelo'],width=20)   
        self.CadastroCanvas.create_window(585,350,window=self.Servico1) 
        self.ComoConheceuTxt = self.CadastroCanvas.create_text(400,400,text="COMO CONHECEU:",font=("Times New Roman",12,'bold'),fill="white")
        self.ComoConheceu =  Text(self.CadastroCanvas,width=50,height=10)
        self.CadastroCanvas.create_window(700,480,window=self.ComoConheceu)   
        
        # BOTOES E FUNCOES
        def Salvar():
            self.connect = sqlite3.connect("database/clientes.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("INSERT INTO clientes (nome,telefone,dia,mes,ano,servico,comentario,cortes) VALUES(?,?,?,?,?,?,?,?)",
                                (self.NomeEntry.get(),self.TelefoneEntry.get(),self.NascimentoDia.get(),self.NascimentoMes.get(),
                                 self.NascimentoAno.get(),self.Servico1.get(),self.ComoConheceu.get(1.0,END),0,))
            self.connect.commit()
            self.connect.close()
            self.PopUp = Canvas(self.CadastroCanvas,bg="black",width=250,height=100)
            self.CadastroCanvas.create_window(600,300,window=self.PopUp)
            self.PopUp.create_text(125,20,text="SALVO COM SUCESSO",font=("Times New Roman",14,'bold'),fill="white")
            def Close():
                self.PopUp.destroy()
            self.ButtonOK = Button(self.PopUp,text="OK",command=Close)
            self.PopUp.create_window(125,60,window=self.ButtonOK)
            self.NomeEntry.delete(0,END)
            self.TelefoneEntry.delete(0,END)
            self.NascimentoDia.delete(0,END)
            self.NascimentoMes.delete(0,END)
            self.NascimentoAno.delete(0,END)
            self.Servico1.delete(0,END)
            self.ComoConheceu.delete(1.0,END)
            self.ComoConheceu.update()
        
        def Limpar():
            self.NomeEntry.delete(0,END)
            self.TelefoneEntry.delete(0,END)
            self.NascimentoDia.delete(0,END)
            self.NascimentoMes.delete(0,END)
            self.NascimentoAno.delete(0,END)
            self.Servico1.delete(0,END)
            self.ComoConheceu.delete(1.0,END)
            self.ComoConheceu.update()
        def Voltar():
            self.CadastroWindow.destroy()
            menupy.Menu.__init__(self)
        
        self.Btn_Salvar = Button(self.CadastroCanvas,text="SALVAR",width=10,bg="blue",fg="white",activebackground="#00008B",command=Salvar)
        self.CadastroCanvas.create_window(1000,420,window=self.Btn_Salvar)
        self.Btn_Limpar = Button(self.CadastroCanvas,text="LIMPAR",width=10,bg="blue",fg="white",activebackground="#00008B",command=Limpar)
        self.CadastroCanvas.create_window(1000,470,window=self.Btn_Limpar)
        self.Btn_Voltar = Button(self.CadastroCanvas,text="VOLTAR",width=10,bg="blue",fg="white",activebackground="#00008B",command=Voltar)
        self.CadastroCanvas.create_window(1000,520,window=self.Btn_Voltar)
        
        
        

        
       
        
   
        
        self.CadastroWindow.mainloop()
#Cadastro()