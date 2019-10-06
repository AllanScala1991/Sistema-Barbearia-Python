from tkinter import *
import sqlite3
import menu as menupy




class Login():
    def __init__ (self):
        self.LoginWindow = Tk()
        self.LoginWindow.title("Sistema de Barbearia")
        self.LoginWindow.minsize(width=1200,height=600)
        self.LoginWindow.resizable(False,False)
        self.LoginCanvas = Canvas(self.LoginWindow)
        self.LoginCanvas.pack(expand=1,fill=BOTH)
        #BACKGROUND
        self.LoginBack = PhotoImage(file="image/loginback.png")
        self.LoginCanvas.create_image(0,0,image=self.LoginBack,anchor=NW)
        #TITULO DA JANELA
        self.LoginTitle = PhotoImage(file="image/logintitle.png")
        self.LoginCanvas.create_image(600,100,image=self.LoginTitle) 
        #BANCO DE DADOS
        self.connect = sqlite3.connect("database/login.db")
        self.cursor = self.connect.cursor()     
        self.cursor.execute("SELECT id FROM logins")
        self.NumeroDeCadastros = self.cursor.fetchall()
        self.connect.close()
        self.connect = sqlite3.connect("database/login.db")
        self.cursor = self.connect.cursor()     
        self.cursor.execute("SELECT nome FROM logins")
        self.UserLog = []
        self.Usuarios = 0
        while self.Usuarios<len(self.NumeroDeCadastros):
            for log in self.cursor.fetchone():
                self.UserLog.append(log)
                self.Usuarios +=1
        self.connect.close()
        
       
            

        
        #FUNCOES
        def LoginConfirm():
            if self.LoginUser.get() in self.UserLog:
                self.connect = sqlite3.connect("database/login.db")
                self.cursor = self.connect.cursor()     
                self.cursor.execute("SELECT senha FROM logins WHERE nome = ?",(self.LoginUser.get(),))
                self.UserPassword= []
                for password in self.cursor.fetchone(): 
                    self.UserPassword.append(password)   
                print (self.UserPassword)
                if self.SenhaUser.get() in self.UserPassword:
                    self.connect.close()
                    self.connect = sqlite3.connect("database/config.db")
                    self.cursor = self.connect.cursor()
                    self.cursor.execute("UPDATE config SET usuario = ? WHERE id = ?",(self.LoginUser.get(),1))
                    self.connect.commit()
                    self.connect.close
                    self.LoginWindow.destroy()
                    menupy.Menu.__init__(self)
                else:
                    self.LoginCanvas.itemconfigure(self.LogError,text="Senha incorreta!")
            else:
                self.LoginCanvas.itemconfigure(self.LogError,text="Login incorreto!")
        
        def Cadastrar():
            self.cadastrar_canvas = Canvas(self.LoginCanvas)
            self.cadastrar_canvas.config(width=400,height=400)
            self.LoginCanvas.create_window(600,300,window=self.cadastrar_canvas)   
            self.cadastrar_canvas.create_text(200,20,text="LOGIN:",font=("Arial Black",10,"bold"),fill="black") 
            self.nome_entry = Entry(self.cadastrar_canvas,width=30,justify='center')
            self.cadastrar_canvas.create_window(200,50,window=self.nome_entry)
            self.cadastrar_canvas.create_text(200,80,text="SENHA:",font=("Arial Black",10,"bold"),fill="black") 
            self.senha_entry = Entry(self.cadastrar_canvas,width=30,justify='center')
            self.cadastrar_canvas.create_window(200,110,window=self.senha_entry)
            self.texto_erro = self.cadastrar_canvas.create_text(200,300,text="",font=("Arial Black",10,"bold"),fill="black")
            def Aceitar():
                if self.nome_entry.get() != "" and self.senha_entry.get() != "" :
                    try:
                        self.connect2 = sqlite3.connect("database/login.db")
                        self.cursor2 = self.connect2.cursor()
                        self.cursor2.execute('INSERT INTO logins (nome,senha,adm) VALUES (?,?,?)',(self.nome_entry.get(),self.senha_entry.get(),"nao",))    
                        self.connect2.commit()
                        self.connect2.close()
                        self.nome_entry.delete(0,END)  
                        self.senha_entry.delete(0,END)  
                        self.cadastrar_canvas.itemconfigure(self.texto_erro,text="")
                        
                    except:
                        self.cadastrar_canvas.itemconfigure(self.texto_erro,text="ERRO TENTE NOVAMENTE")
                        
                else:
                    self.cadastrar_canvas.itemconfigure(self.texto_erro,text="PREENCHE TODOS OS CAMPOS")
             
            self.btn_confirmar = Button(self.cadastrar_canvas,text='CONFIRMAR',width=10,bg="blue",fg="white",activebackground="#00008B",command=Aceitar)
            self.cadastrar_canvas.create_window(200,200,window=self.btn_confirmar)
            def Voltar():
                self.cadastrar_canvas.destroy()
                
            self.btn_back = Button(self.cadastrar_canvas,text='VOLTAR',width=10,bg="blue",fg="white",activebackground="#00008B",command=Voltar)
            self.cadastrar_canvas.create_window(200,250,window=self.btn_back)

            
           
        #AREA DE LOGIN
        self.Fundo = PhotoImage(file="image/fundo.png")
        self.LoginCanvas.create_image(600,370,image=self.Fundo)
        self.LoginCanvas.create_rectangle(400,195,800,545,width=3,outline="black")
        self.LoginCanvas.create_text(600,230,text="LOGIN",font=("Arial Black",18,"bold"),fill="white")
        self.LoginCanvas.create_text(600,270,text="Nome de usuário",font=("Arial",12,"bold"),fill="white")
        self.LoginUser = Entry(self.LoginCanvas,width=20,highlightcolor="blue")
        self.LoginCanvas.create_window(600,300,window=self.LoginUser)
        self.LoginCanvas.create_text(600,350,text="Senha",font=("Arial",12,"bold"),fill="white")
        self.SenhaUser = Entry(self.LoginCanvas,width=20,highlightcolor="blue",show="*")
        self.LoginCanvas.create_window(600,380,window=self.SenhaUser)
        self.ButtonAccept = Button(self.LoginCanvas,text="FAZER LOGIN",width=10,bg="blue",fg="white",activebackground="#00008B",command=LoginConfirm)
        self.LoginCanvas.create_window(600,430,window=self.ButtonAccept)
        self.ButtonCadastrar = Button(self.LoginCanvas,text='CADASTRAR',width=10,bg="blue",fg="white",activebackground="#00008B",command=Cadastrar)
        self.LoginCanvas.create_window(600,470,window=self.ButtonCadastrar)
        #ERRO DE LOGIN
        self.LogError = self.LoginCanvas.create_text(600,530,text="",font=("Arial",12,"bold"),fill="yellow")
        
        #CREDITOS
        self.LoginCanvas.create_text(600,580,text="Sistema desenvolvido por Allan Scala",font=("Arial",8,"bold"),fill="white")
        
        
        
        self.LoginWindow.mainloop()
#Login()

        
        