from tkinter import *
from tkinter import ttk
import sqlite3
import menu as menupy


class Caixa():
    def __init__(self):
        self.caixa_window = Tk()
        self.caixa_window.title("SISTEMA DE BARBEARIA - CAIXA")
        self.caixa_window.minsize(width=1200,height=600)
        self.caixa_window.resizable(False,False)
        self.caixa_canvas = Canvas(self.caixa_window)
        self.caixa_canvas.pack(expand=1,fill=BOTH)
        self.caixa_background = PhotoImage(file="image/menuback.png")
        self.caixa_canvas.create_image(0,0,image=self.caixa_background,anchor=NW)
        self.caixa_canvas.create_line(0,150,1200,150,width=3,fill="white")
        self.caixa_title = self.caixa_canvas.create_text(600,125,text="CAIXA",font=("Times New Roman",48,"bold"),fill="white")      
        self.dinheiro_img = PhotoImage(file="image/dinheiro.png")
        self.fundo_azul = PhotoImage(file="image/fundo_azul.png")
        self.caixa_canvas.create_image(430,120,image=self.dinheiro_img)
        self.caixa_canvas.create_image(770,120,image=self.dinheiro_img)
        
        ## BOTOES
        def Voltar():
            self.caixa_window.destroy()
            menupy.Menu.__init__(self)
        self.btn_voltar  = Button(self.caixa_canvas,text="VOLTAR",font=("Impact",10,"bold"),fg="black",bg="red",activebackground="#B22222",width=18,command=Voltar)
        self.caixa_canvas.create_window(600,450,window=self.btn_voltar)

        ##TOTAIS
        self.caixa_canvas.create_text(300,200,text="TOTAL GERAL:",font=("Times New Roman",28,"bold"),fill="white")
        self.caixa_canvas.create_rectangle(147,227,473,383,outline="red")
        self.caixa_canvas.create_image(310,305,image=self.fundo_azul)
        self.ganho_txt = self.caixa_canvas.create_text(310,305,text="R$ 0",font=("Times New Roman",22,"bold"),fill="green")
        
        self.caixa_canvas.create_text(800,200,text="TOTAL DO DIA:",font=("Times New Roman",28,"bold"),fill="white")
        self.caixa_canvas.create_rectangle(647,227,973,383,outline="red")
        self.caixa_canvas.create_image(810,305,image=self.fundo_azul)
        self.ganho_dia_txt = self.caixa_canvas.create_text(810,305,text="R$ 0",font=("Times New Roman",22,"bold"),fill="green")
        
        #VERIFICANDO OS VALORES GANHOS
        try:
            self.connect = sqlite3.connect("database/cortes.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT id FROM cortes")
            self.total_ids = []
            self.valor_total = 0
            self.loop = 0
            self.valores = []
            for ids in self.cursor.fetchall():
                self.total_ids.append(ids)
            self.cursor.execute("SELECT valor FROM cortes")
            while self.loop<len(self.total_ids):
                for valor in self.cursor.fetchone():
                    self.valores.append(valor)
                    self.valor_total += float(self.valores[0])
                    self.valores.clear()
                    self.loop+=1
            self.caixa_canvas.itemconfigure(self.ganho_txt,text="R$ "+str(self.valor_total).replace(".",","))
            self.connect2 = sqlite3.connect("database/config.db")
            self.cursor2 = self.connect2.cursor()
            self.cursor2.execute('SELECT data_atual FROM config')
            self.data = self.cursor2.fetchone()
            self.cursor.execute('SELECT id FROM cortes WHERE data_atual=?',(self.data[0],))
            self.ids = self.cursor.fetchall()
            self.listas = []
            self.valor_diario = 0
            self.loop2 = 0
            self.cursor.execute('SELECT valor FROM cortes WHERE data_atual=?',(self.data[0],))
            while self.loop2<len(self.ids):
                for i in self.cursor.fetchone():
                    self.listas.append(i)
                    self.valor_diario += float(self.listas[0])
                    self.listas.clear()
                    self.loop2+=1
            self.caixa_canvas.itemconfigure(self.ganho_dia_txt,text="R$ "+str(self.valor_diario).replace(".",","))
            self.connect.close()
            self.connect2.close()
                
        except:
            self.caixa_canvas.itemconfigure(self.ganho_txt,text="R$ 0")

        self.caixa_window.mainloop()
#Caixa()