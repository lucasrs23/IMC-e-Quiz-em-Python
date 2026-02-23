nome = input("Qual seu nome? ")
altura = float(input("Qual sua altura? "))
peso = float(input("Qual seu peso? "))
imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura} de altura'

print(linha_1)
print("Pesa", peso, "quilos e seu IMC é:")
print(imc)

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 35:
    print("Classificação: Obesidade Grau I")
elif 35 <= imc < 40:
    print("Classificação: Obesidade Grau II")
else:
    print("Classificação: Obesidade Grau III (mórbida)")