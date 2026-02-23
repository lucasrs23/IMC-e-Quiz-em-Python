import random

print("Seja muito bem-vindo ao Guess Number")

while True:
    choice_number = input("Digite o número máximo do desafio: ")
    try:
        choice_number = int(choice_number)
        break  # valor válido, sai do loop
    except ValueError:
        print("Erro: o valor informado não é numérico. Por favor, digite um número inteiro válido.")

random_number = random.randint(0, choice_number)

while True:
  answer_user = input("Advinhe o número: ")

  if answer_user.isdigit() or (answer_user.startswith('-') and answer_user[1:].isdigit()):
    answer_user = int(answer_user)
    print(f"Você digitou: {answer_user}")

  else:
    print("Erro: o valor informado não é numérico. Por favor, digite um número inteiro válido.")

  if answer_user == random_number:
    print("Você acertou!")
    break
  elif answer_user > random_number:
     print("Chutou muito alto, o número é menor que isso...")
  else:
     print("Chutou baixo, o número é maior que isso...")