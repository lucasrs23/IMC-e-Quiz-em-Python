print("Isso aqui é um jogo Quiz, seja muito bem vindo =D !")
resposta = input("Quer começar? S/N ")
if resposta.upper() != "S":
    quit()

score = 0  # <-- agora está no lugar certo, fora do if

print("Começando... \n")

while True:
    print("Quem desenvolveu o jogo GTA? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA")
    resposta_1 = input("Resposta: ")

    if resposta_1.upper() == "A":  # upper() deixa maiúsculo, aceita "a" ou "A"
        print("Você acertou!\n")
        score = score + 1
        break
    else:
        print("Eroooou! Tente novamente...\n")

while True:
    print("Quem é o protagonista do jogo Resident Evil 4? \n (A) Leandro \n (B) Ash \n (C) Leon \n (D) Joseph")
    resposta_2 = input("Resposta: ")

    if resposta_2.upper() == "C":
        print("Você acertou!\n")
        score = score + 1
        break
    else:
        print("Eroooou! Tente novamente...\n")

print(f"O jogo terminou, sua pontuação é de: {score}")
   

