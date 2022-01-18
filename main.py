#https://www.youtube.com/watch?v=_h0hGfpWS-A&list=PL72uMH0hlJzoahdsn_Jpp8OjY8sW4C4FA&index=6&ab_channel=PythonFEI


import tkinter as tk
from tkinter import messagebox

class Tela:
    def __init__(self, master):
        self.nossa_tela = master
        self.nossa_tela.title("Primeira Aula")


        self.fr = tk.Frame(self.nossa_tela)
        self.fr2 = tk.Frame(self.nossa_tela)

        self.fr.pack()
        self.fr2.pack(side=tk.BOTTOM)

        self.lbl = tk.Label(self.fr, text='Estou no frame 1', font=('Arial', '16'))
        self.lbl.pack()

        self.lbl2 = tk.Label(self.fr2, text='Estou no frame 2', font=('Arial', '16'))
        self.lbl2.pack(side=tk.LEFT)

        self.lbl3 = tk.Label(self.fr2, text='Estou no frame 2', font=('Arial', '16'))
        self.lbl3.pack(side=tk.LEFT)


        # self.lbl = tk.Label(self.nossa_tela, text='Abrir Caixa', font=('Verdana', '16'), relief='raised')
        # self.lbl.pack(pady=20)
        # self.lbl.bind('<Button-1>', self.clique)
        # self.lbl.bind('<ButtonRelease>', self.resposta)

        # self.btn = tk.Button(self.nossa_tela, text='Clique', font=('Verdana', '16'), command=self.resposta_btn)
        # self.btn.pack()

        # self.lbl = tk.Label(self.nossa_tela, text='Olá Mundo', background='red')
        # self.lbl['font'] = ('verdana', '18')
        # self.lbl.pack(pady = 20, side=tk.LEFT, fill=tk.Y)
    # def resposta_btn(self):
    #     messagebox.showinfo("Caixa de mensagem", "Isso é uma mensage")
    #
    # def clique(self, even):
    #     self.lbl['relief'] = 'sunken'
    #
    #
    # def resposta(self, event):
    #     print(event.x, event.y)
    #     messagebox.showinfo('Caixa de Mensagem', 'Isso é uma mensagem')
    #     self.lbl['relief'] = 'raised'




#Gerar a nossa interface
janela_raiz = tk.Tk()

Tela(janela_raiz)
janela_raiz.mainloop()