# PBL IV-A  ~  SenhaQuebrador
# André Vinícius Zicka Schmidt
# Eduardo Scaburi Costa Barros
from random import randint
from random import choice
from kivy.app import App
from kivy.uix.button import Button


# Variável que informa se uma senha já foi gerada
senhaExiste = False

# Listas que irão armazenar a senha e as escolhas do usuário
senha = []
escolhas = []

# Sorteio dos elementos da senha
if not senhaExiste:
    listaRadio = ['Biscoito', 'Bolacha']
    listaSpinner = ['Carro WhatsApp', 'Carro Telegram',
                    'Carro Discord', 'Carro Skype', 'Carro MSN']
    listaCheckbox = ['Coca-Cola', 'Pepsi', 'Guaraná']

    numSorteado = randint(0, 10)
    radioSorteio = choice(listaRadio)
    spinnerSorteio = choice(listaSpinner)
    checkboxSorteio = choice(listaCheckbox)

    senha.append(numSorteado)
    senha.append(radioSorteio)
    senha.append(spinnerSorteio)
    senha.append(checkboxSorteio)

    senhaExiste = True
else:
    pass


class SenhaQuebradorApp(App):
    def build(self):
        botao = Button(text='Exibir senha')

        botao.bind(on_release = self.mostrarSenha)
        return botao

    def mostrarSenha(self, event):
        print(senha)


if __name__ == '__main__':
    SenhaQuebradorApp().run()
