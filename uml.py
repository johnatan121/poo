import PySimpleGUI as sg

class Endereco:
    def __init__(self, cidade, rua):
        self. cidade = cidade
        self. rau = rua

    def mostrar_endereco(self):
        return f"rua:{self.rua} cidade:{self.cidade}"

    @staticmethod
    def validar(cidade, rua):
        if not cidade or not rua:
            return False
        return True




class Pessoa:
    def __init__(self, nome, idade, Endereco):
        self. nome = nome 
        self. idade = idade
        self. Endereco = Endereco

    def apresentar (self):
        return f"Nome: {self.nome} - idade: {self.idade} anos - {self.Endereco_Endereco()}"        

    @staticmethod
    def validar_idade(idade):
        if not idade.isdigit():
            return False
        if int(idade) <=0:
            return False
        return True
    
class InterfaceSistema:
    def __init__(self):
        layout = [
                [sg.Text('Nome:'), sg.Input(key = "Nome")],
                [sg.Text("Idade:"), sg.Input(key="idade")],
                [sg.Text("Cidada"), sg.Input(key ="cidade")],
                [sg.Text("rua"), sg.Input(key = "rua")],
                [sg.Button("Cadastrar")],
                [sg.Text("", key = "saida")]
        ] 
        self.janela = sg.Window("cadastro", layout)
        self. executar()

    def executar(self):
        while True:
            evento, valores = self.janela.read()  
            if evento == sg.WIN_CLOSED():
                break
            if evento == "cadastra":
                self.mostrar_dados(valores)
        self. janela.close()

    def mostrar_dadaos(self, valores):
        if not Pessoa.validar_idade(valores["idade"]):
            self.janela["saida"].update("idade invalida!") 
        if not Endereco.validar(valores["cidade"], valores["rua"]):
            self.janela["saida"].update("endereço invalido")

        endereco = Endereco(valores["cidade"], valores["rua"])
        pessoa = Pessoa(valores["nome"], int (valores["idade"]), endereco)

        self.janela["saida"] .update(pessoa.apresentar())                  

InterfaceSistema()
