#https://www.youtube.com/watch?v=_h0hGfpWS-A&list=PL72uMH0hlJzoahdsn_Jpp8OjY8sW4C4FA&index=6&ab_channel=PythonFEI


import tkinter as tk
from tkinter import  messagebox

class Tela:
    def __init__(self, master):
        self.nossa_tela = master
        self.nossa_tela.title("Primeira Aula")

        self.lbl = tk.Label(self.nossa_tela, text='Abrir Caixa', font=('Verdana', '16'), relief='raised')
        self.lbl.pack(pady=20)
        self.lbl.bind('<Button-1>', self.resposta)

        # self.lbl = tk.Label(self.nossa_tela, text='Olá Mundo', background='red')
        # self.lbl['font'] = ('verdana', '18')
        # self.lbl.pack(pady = 20, side=tk.LEFT, fill=tk.Y)

    def resposta(self, event):
        print(event.x, event.y)
        messagebox.showinfo('Caixa de Mensagem', 'Isso é uma mensagem')




#Gerar a nossa interface
janela_raiz = tk.Tk()

Tela(janela_raiz)
janela_raiz.mainloop()