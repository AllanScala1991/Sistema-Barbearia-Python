from tkinter import *
from tkinter import ttk
import sqlite3
import menu as menupy


class Relatorio():
    def __init__(self):
        self.relatorio_janela = Tk()
        self.relatorio_janela.title("Sistema de Barbearia - RELATÓRIO")
        self.relatorio_janela.minsize(width=1200, height=600)
        self.relatorio_janela.resizable(False,False)
        self.relatorio_canvas = Canvas(self.relatorio_janela)
        self.relatorio_canvas.pack(expand=1,fill=BOTH)
        self.relatorio_background = PhotoImage(file="image/menuback.png")
        self.relatorio_canvas.create_image(0,0,image=self.relatorio_background,anchor=NW)
        
        # TITULO
        self.relatorio_title = self.relatorio_canvas.create_text(600,100,text="RELATÓRIO",font=("Times New Roman",48,"bold"),fill="white")
        self.relatorio_canvas.create_line(0,130,1200,130,width=3,fill="white")
        
        #BANCO DE DADOS
        self.connect = sqlite3.connect("database/cortes.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT id FROM cortes")
        self.Ids = self.cursor.fetchall()
        
        #FILTRO
        self.relatorio_canvas.create_text(430,200,text="SELECIONE O FILTRO:",font=("Times New Roman",12,"bold"),fill="white")
        self.filtro = ttk.Combobox(self.relatorio_canvas,value=['GERAL','POR DATA'],width=15,state='readonly')
        self.relatorio_canvas.create_window(600,200,window=self.filtro)
        def Selecionar():
            if self.filtro.get()=="GERAL":
                self.all_list = []
                self.loop = 0
                self.id_inicial = 1
                while self.loop<len(self.Ids):
                    self.cursor.execute("SELECT * FROM cortes WHERE id = ?",(self.id_inicial,))
                    for corte in self.cursor.fetchone():
                        self.all_list.append(corte)  
                    self.relatorio_geral.insert(END,"CÓD. VENDA: "+str(self.all_list[0])+"\n")
                    self.relatorio_geral.insert(END,"CLIENTE: "+str(self.all_list[1])+"\n")
                    self.relatorio_geral.insert(END,"PRODUTOS: \n"+str(self.all_list[2])+"\n")
                    self.relatorio_geral.insert(END,"VALOR: "+str(self.all_list[3])+"\n")
                    self.relatorio_geral.insert(END,"USUARIO: "+str(self.all_list[4])+"\n")
                    self.relatorio_geral.insert(END,"DATA: "+str(self.all_list[5])+"\n")
                    self.relatorio_geral.insert(END,"________________________________________________________________________________")
                    self.all_list.clear()
                    self.loop +=1
                    self.id_inicial +=1
            if self.filtro.get() == "POR DATA":
                self.relatorio_canvas.create_text(500,250,text="INFORME A DATA SEPARADO POR /",font=("Times New Roman",10,"bold"),fill="white")
                self.nova_data =  Entry(self.relatorio_canvas,width=15)
                self.relatorio_canvas.create_window(700,250,window=self.nova_data)
                def Confirmar ():
                    self.cursor.execute("SELECT id FROM cortes WHERE data_atual=?",(self.nova_data.get(),))
                    self.total_id = self.cursor.fetchall()
                    self.all_list2 = []
                    self.loop2 = 0
                    self.list = 0
                    while self.loop2<len(self.total_id):
                        self.cursor.execute("SELECT * FROM cortes WHERE data_atual=?",(self.nova_data.get(),))
                        self.teste = self.cursor.fetchall()
                        for data in self.teste:
                            self.all_list2.append(data)
                        self.relatorio_geral.insert(END,"CÓD. VENDA: "+str(self.all_list2[self.list][0])+"\n")
                        self.relatorio_geral.insert(END,"CLIENTE: "+str(self.all_list2[self.list][1])+"\n")
                        self.relatorio_geral.insert(END,"PRODUTOS: \n"+str(self.all_list2[self.list][2])+"\n")
                        self.relatorio_geral.insert(END,"VALOR: "+str(self.all_list2[self.list][3])+"\n")
                        self.relatorio_geral.insert(END,"USUARIO: "+str(self.all_list2[self.list][4])+"\n")
                        self.relatorio_geral.insert(END,"DATA: "+str(self.all_list2[self.list][5])+"\n")
                        self.relatorio_geral.insert(END,"________________________________________________________________________________")
                        self.all_list2.clear()
                        self.loop2 +=1
                        self.list+=1
                        
                            
                self.btn_confirmar = Button(self.relatorio_canvas,text="CONFIRMAR",width=10,bg="blue",fg="white",activebackground="#00008B",command=Confirmar)
                self.relatorio_canvas.create_window(600,300,window=self.btn_confirmar)
                
        self.btn_selecionar = Button(self.relatorio_canvas,text="SELECIONAR",width=10,bg="blue",fg="white",activebackground="#00008B",command=Selecionar)
        self.relatorio_canvas.create_window(750,200,window=self.btn_selecionar)
        
        def Limpar():
            self.relatorio_geral.delete(1.0, END)
        self.btn_limpar = Button(self.relatorio_canvas,text="LIMPAR",width=10,bg="blue",fg="white",activebackground="#00008B",command=Limpar)
        self.relatorio_canvas.create_window(880,200,window=self.btn_limpar)
        
        def Voltar():
            self.relatorio_janela.destroy()
            menupy.Menu.__init__(self)
        self.btn_voltar = Button(self.relatorio_canvas,text="VOLTAR",width=10,bg="blue",fg="white",activebackground="#00008B",command=Voltar)
        self.relatorio_canvas.create_window(1050,560,window=self.btn_voltar)
            
        
        #RELATORIO
        self.scroll = Scrollbar(self.relatorio_canvas,bg="black")
        self.relatorio_canvas.create_window(940,450,window=self.scroll,width=15,height=260)
        
        self.relatorio_geral = Text(self.relatorio_canvas,yscrollcommand=self.scroll.set)
        self.relatorio_geral.config(width=80,height=15)
        self.relatorio_canvas.create_window(600,450,window=self.relatorio_geral)
        self.scroll.config(command=self.relatorio_geral.yview)

        
        
                
        self.relatorio_janela.mainloop()
#Relatorio()