# 6 sided die roll and present a number
import random

class Funcionamento:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Rolar o dado novamente?(sim/não): '

    def Iniciar(self):
        escolha = input(self.mensagem).strip().lower()
        while escolha != 'não':
            if escolha == 'sim':
                self.RolarDado()
                escolha = input(self.mensagem).strip().lower()
            else:
                print('Opção inválida')
                escolha = input(self.mensagem).strip().lower()
        print('Ok, obrigado!')

    def RolarDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

rodar_dados = Funcionamento()
rodar_dados.Iniciar()