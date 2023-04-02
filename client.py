import socket
from threading import Thread
from tkinter import *

# nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 1234

client.connect((ip_address, port))

print("Connected with the server...")

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")

        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)

        # self.scrollbar = Scrollbar(orient="vertical", command=self.text_area.yview)
        # self.scrollbar.place(x=380, y=100, height=320)

        # self.text_area.config(yscrollcommand=scrollbar.set)
        self.pls = Label(self.login,
					text = "Please login to continue",
					justify = CENTER,
					font = "Helvetica 14 bold")
        self.pls.place( relheight = 0.15,
                        relx = 0.2,
                        rely = 0.07)

        self.labelName = Label(self.login,
							text = "Name: ",
							font = "Helvetica 12")
        self.labelName.place(   relheight = 0.2,
							    relx = 0.1,
							    rely = 0.2)

        self.entryName = Entry(self.login,
							font = "Helvetica 14")
        self.entryName.place(relwidth = 0.4,
							relheight = 0.12,
							relx = 0.35,
							rely = 0.2)
        self.entryName.focus()

        self.go = Button(self.login,
						text = "continue",
						font = "Helvetica 14 bold",
						command = lambda: self.goAhead(self.entryName.get()))
        self.go.place(relx = 0.4,
					    rely = 0.55)
        self.Window.mainloop()
    def write(self):
        self.textCons.config(state-DISABLED) 
        while True:
                message= (f"{self.name}: {self.msg}")
                client.send(message.encode('utf-8')) 
                self.show_message(message)
                receive_thread = Thread(target=receive)
                receive_thread.start()
                write_thread = Thread(target=write)
                break

    def goAhead(self, name):
        self.login.destroy()
        self.name = name
        self.layout(name)
        rcv = Thread(target=self.receive)
        rcv.start()

  
     
# write_thread.start()
    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    self.showMessage(message)
            except:
                print("An error occured!")
                client.close()
                break
    def sendButton():
        self.textCons.config(state = DISABLED) 
        self.msg=msg
        self.entryMsg.delete(0, END)
        snd= Thread(target = self.write) 
        snd.start()
    def showMessage(self,message):
        self.textCons.config(state = NORMAL) 
        self.textCons.insert(END, message+"\n\n") 
        self.textCons.config(state = DISABLED) 
        self.textCons.see(END)


g = GUI()
