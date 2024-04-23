class Carro:
    def __init__(self, marca, modelo, cor, ano):
      self.marca = marca
      self.modelo = modelo
      self.cor = cor
      self.ano = ano

    def exibir_informacoes(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Ano: ", self.ano)

carro = []

while True:
   marca = input("digite a marca do carro ou 'sair' para encerrar o programa")


   if marca.lower == "sair":
      print("Até a Proxima!")
      break
   
   modelo = input("digite o modelo")
   cor = input("digite a cor")
   ano = input("digite o ano")

   carro = Carro(marca,modelo,cor)
   carros.append(carro)

print("\n informações do carro")
for i, carros in enumerate(carros, start=1):
   print(f"\n Carro{i}")
   carro.exibir_informacoes()
