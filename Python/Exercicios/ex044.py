""" Crie um programa onde o utilizador possa digitar vários números e guardálos numa lista. Caso o número inserido esteja na lista ele não deve ser adicionado. No final mostre todos os valores por ordem DECRESCENTE. """

lista = list()

while True:
    num = int(input("Digite um número para adicionar a lista: ")) 
    #continuar = input("Deseja continuar?[S/N]").lower()

    if num in lista:
        print("O valor digitado é o mesmo que já existe na lista.")
    else:
        lista.append(num)
        print("Valor adicionado com sucesso!")
        continuar = input("Deseja continuar?[S/N]").lower()

        if continuar == "n":
            print("Sua lista foi: ", lista)
            lista.sort(reverse = True)
            print ("A ordem decrescente foi:", lista)
            break
              