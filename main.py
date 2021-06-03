# PBL IV-A  ~  SenhaQuebrador
# André Vinícius Zicka Schmidt
# Eduardo Scaburi Costa Barros
from random import randint
from random import choice
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SenhaQuebradorApp(BoxLayout):
    def __init__(self):  # Função Init para definição de atributos
        super().__init__()

        self.senhaExiste    = False
        self.senha          = []
        self.escolhas       = []

        self.listaRadio     = ['Biscoito', 'Bolacha']
        self.listaSpinner   = ['Carro WhatsApp', 'Carro Telegram',
                               'Carro Discord', 'Carro Skype', 'Carro MSN']
        self.listaCheckbox  = ['Coca-Cola', 'Pepsi', 'Guaraná']

        self.numSelecionado = ''
        self.traqEscolhida  = ''
        self.carroEscolhido = ''
        self.refriEscolhido = ''

    def gerarSenha(self):
        if not self.senhaExiste:
            numSorteado      = randint(0, 10)
            radioSorteado    = choice(self.listaRadio)
            spinnerSorteado  = choice(self.listaSpinner)
            checkboxSorteado = choice(self.listaCheckbox)

            self.senha.append(numSorteado)
            self.senha.append(radioSorteado)
            self.senha.append(spinnerSorteado)
            self.senha.append(checkboxSorteado)
        else: pass

        return self.senha

    def numero(self):
        self.numSelecionado = self.ids['numero'].text
        if self.numSelecionado is '':
            self.ids['resposta'].text = 'Você não digitou nenhum núemro!'
        if isinstance(self.numselecionado, int) != True:
            self.ids['resposta'].text = 'O número não pode ser um texto.'
        return self.numSelecionado

    def check(self, n):
        traquinas = ['Biscoito', 'Bolacha']
        self.traqEscolhida = traquinas[n]
        return self.traqEscolhida

    def carro(self, c):
        self.carroEscolhido = c
        return self.carroEscolhido

    def refri(self, r):
        lista = ['Coca-Cola', 'Pepsis', 'Guaraná']
        self.refriEscolhido = lista[r]
        return self.refriEscolhido

    def verificar(self):
        try:
            certo = []
            Escolhidos = [int(self.numSelecionado), self.traqEscolhida,
                          self.carroEscolhido, self.refriEscolhido]
            for i in range(0, 4):
                if Escolhidos[i] == self.senha[i]:
                    certo.append(str(Escolhidos[i]))
                else:
                    pass
            acerto = ', '.join(certo)
            if certo is []:
                self.ids['resposta'].text = f'Você não certou nada!'

            elif len(certo) == 4:
                self.ids['resposta'].text = f'Parabéns! Você descobriu a senha!'
            else:
                self.ids['resposta'].text = f'Você acertou: {acerto}'
        except AttributeError:
            self.ids['resposta'].text = 'Você esqueceu de marcar alguma coisa...'


class BuildApp(App):
    def build(self):
        return SenhaQuebradorApp()


App = BuildApp()
App.run()
