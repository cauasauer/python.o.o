#ojetivo é uma unica coleção de dados(atributos) e comportamentos (metodos)
class contaBancaria:
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor

    def exibir_detalhes(self):
        print("Numero da conta:", self.numero)
        print("Titular", self.titular)
        print("Saldo:", self.saldo)


    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("O seu saldo inuficiente")
        
def exibir_menu():
    print("\nMENU:")
    print("1 - Exibir detalhes da conta")
    print("2 - Realizar Depósito")
    print("3 - Realizar Saque")
    print("0 - Sair do programa")

#aqui crio uma instancia do objeto contaBancaris
#como nome conta_do_caua

numero_conta = input("Digite o numero da conta: ")
titular_conta = input("Digite o titular da conta: ")
saldo_inicial = float(input("Digite o saldo inicial da conta: "))

conta_do_usuario = contaBancaria(numero_conta, titular_conta , saldo_inicial)

opcao = None

while opcao != 0:
    exibir_menu()
    opcao = int(input("Digite o numero da opção desejada: "))

    if opcao == 1:
        conta_do_usuario.exibir_detalhes()
    elif opcao == 2:
        valor_depositar = float(input("Digite o valor a ser depositado: ").replace(",","."))
        conta_do_usuario.depositar(valor_depositar)
    elif opcao == 3:
        valor_saque = float(input("Digite o valor que sera sacado: ").replace(",","."))
        conta_do_usuario.sacar(valor_saque)    


#Usando os metodos do objeto contaBancaria 

valor_depositar = float(input("digite o valor que sera depositado").replace(",","."))
valor_saque = float(input("digite o valor que sera sacado").replace(",","."))


conta_do_usuario.depositar(valor_depositar)
conta_do_usuario.sacar(valor_saque)

conta_do_usuario.exibir_detalhes()

