from tkinter import *
from tkinter.ttk import *
import control


class Application:

    def __init__(self, window):
        # Cores Padrao
        corDeFundo = "#0f703c"
        corDoBotao = "#56db94"
        corDaFonte = "#000"
        # Configurando a janela
        window.geometry("570x530")
        window.resizable(0, 0)
        window.title("Agenda")
        window['background'] = corDeFundo

        # Configuração de Estilos
        self.TituloStyle = Style()
        self.TituloStyle.configure("ttk.TituloStyle.TLabel", font=(
            "Arial", 16), background=corDeFundo, foreground="white")

        self.DefaultTextStyle = Style()
        self.DefaultTextStyle.configure(
            "TLabel", background=corDeFundo, foreground=corDaFonte)

        self.DefaultButtonStyle = Style()
        self.DefaultButtonStyle.configure(
            "TButton", background=corDoBotao, relief="flat", foreground=corDaFonte, highlightness=0)
        self.DefaultButtonStyle.map(
            'TButton', background=[('active', 'black')], foreground=[('active', 'white')])

        self.TextStyle = Style()
        self.TextStyle.configure("tkk.TextStyle.TLabel", font=(
            "Arial", 12), background=corDeFundo, foreground=corDaFonte)

        self.BotaoRemoveStyle = Style()
        self.BotaoRemoveStyle.configure(
            "tkk.BotaoStyleRemove.TButton", background="red")

        # Definindo Elementos
        # |- Titulo
        self.lb_Titulo = Label(
            window, text="Agenda Pessoal de Contatos", style="ttk.TituloStyle.TLabel")
        self.lb_Titulo.grid(row=0, column=0, columnspan=3, padx=25, pady=10)

        # |- Label e Entry Nome
        self.lb_Nome = Label(window, text="Nome", style="tkk.TextStyle.TLabel")
        self.lb_Nome.grid(row=1, column=0, padx=25, pady=10, stick="we")
        self.Et_Nome = Entry(window, width=50)
        self.Et_Nome.grid(row=1, column=1, padx=25,
                          pady=10, stick="w", columnspan=2)

        # |- Label e Entry Telefone
        self.lb_Telefone = Label(
            window, text="Telefone", style="tkk.TextStyle.TLabel")
        self.lb_Telefone.grid(row=2, column=0, padx=25, pady=10, stick="we")
        self.Et_Telefone = Entry(window, width=50)
        self.Et_Telefone.grid(row=2, column=1, padx=25,
                              pady=10, stick="w", columnspan=2)

        # |- Botao Adicionar
        self.btn_Adicionar = Button(
            window, text="Adicionar", style="tkk.BotaoStyle.TButton", command=lambda: control.adicionar(self))
        self.btn_Adicionar.grid(row=3, column=0, columnspan=2, stick='e')

        # |- Botao Alterar
        # Quando pressionado uma vez, entra no modo de alteração. Após terminar a modificação, pressionar novamente para altera-lo;
        self.modoAlterar = False
        # Salva o ID a qual se refere a alteração. Caso o usuario quero selecionar outro mas mudar de ideia depois.
        self.id = None
        self.btn_Alterar = Button(
            window, text="Alterar", command=lambda: control.alterar(self, self.modoAlterar))
        self.btn_Alterar.grid(row=3, column=2)

        # |- Label com os status da consulta
        self.lb_Status = Label(window, text="", font=("Arial", 24))
        self.lb_Status.grid(row=4, column=0, columnspan=3,
                            stick="we", padx=25, pady=10)

        # |- Exibição dos dados
        self.tv_Treeview = Treeview(window, columns=("id", "nome", "telefone"), displaycolumns=[
                                    'nome', 'telefone'], selectmode="browse")
        self.tv_Treeview.grid(row=5, column=0, columnspan=3,
                              padx=25, pady=10, stick="we")
        self.tv_Treeview.heading("#0", text="ID", anchor="w")
        self.tv_Treeview.heading("nome", text="NOME", anchor="w")
        self.tv_Treeview.heading("telefone", text="TELEFONE", anchor="w")
        self.tv_Treeview.column("#0", width=10)
        self.tv_Treeview.column("nome", width=150)
        self.tv_Treeview.column("telefone", width=150)

        # |- Botao para remover
        self.btn_Remove = Button(
            window, text="Remover", style="tkk.BotaoStyleRemove.TButton", command=lambda: control.remover(self))
        self.btn_Remove.grid(row=6, column=0, columnspan=3, padx=25)

        # |- Creditos
        self.lb_Credito = Label(
            window, text="By: Daniel.augusto191@gmail.com", foreground="#FFF")
        self.lb_Credito.grid(row=7, column=0, columnspan=3,
                             padx=25, pady=10, stick="e")
        control.atualizar(self)


if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()
