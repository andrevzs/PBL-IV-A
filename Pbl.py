# PBL IV-A  ~  SenhaQuebrador
# André Vinícius Zicka Schmidt
# Eduardo Scaburi Costa Barros
from random import randint
from random import choice
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SenhaQuebradorApp(BoxLayout):
    def gerarSenha(self):
        self.senha = []
        listaRadio    = ['Biscoito', 'Bolacha']
        listaSpinner  = ['Carro WhatsApp', 'Carro Telegram',
                        'Carro Discord', 'Carro Skype', 'Carro MSN']
        listaCheckbox = ['Coca-Cola', 'Pepsi', 'Guaraná']

        numSorteado     = randint(0, 10)
        radioSorteio    = choice(listaRadio)
        spinnerSorteio  = choice(listaSpinner)
        checkboxSorteio = choice(listaCheckbox)

        self.senha.append(numSorteado)
        self.senha.append(radioSorteio)
        self.senha.append(spinnerSorteio)
        self.senha.append(checkboxSorteio)
        return self.senha
    def numero(self):
        self.numselecionado = self.ids['numero'].text
        if self.numselecionado == '':
            self.ids['resposta'].text = "Você não digitou um numero"
        if isinstance(self.numselecionado, int) != True:
            self.ids['resposta'].text = "O numero não pode ser um texto."
        return self.numselecionado
    def check(self, n) :
        traquinas = ['Biscoito', 'Bolacha']
        self.TraqEscolhida = traquinas[n]
        return self.TraqEscolhida
    def carro(self, c):
        self.carroEscolhido = c
        return self.carroEscolhido
    def refri(self, r):
        lista = ['Coca-Cola', 'Pepsi', 'Guaraná']
        self.refriEscolhido = lista[r]
        return self.refriEscolhido
    def verificar(self):
        try:
            certo = []
            Escolhidos = [int(self.numselecionado), self.TraqEscolhida, self.carroEscolhido, self.refriEscolhido]
            for i  in range(0,4):
                if Escolhidos[i] == self.senha[i]:
                    certo.append(str(Escolhidos[i]))
                else:
                    pass
            acerto = ", ".join(certo)
            if certo == []:
                self.ids['resposta'].text = f"Você não acertou nada!"

            elif len(certo) == 4:
                self.ids['resposta'].text = "Parabens! Você acertou tudo!"
            else:
                self.ids['resposta'].text =f"Você acertou: {acerto}"
        except AttributeError:
            self.ids['resposta'].text = "Voce esqueceu de marcar algo"
        
class PBLApp(App):
    def build(self):
        return SenhaQuebradorApp()

App = PBLApp()
App.run()
