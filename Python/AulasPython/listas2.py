"""aluno = list()
aluno.append("Amanda")
aluno.append("31")

turma= list()
turma.append(aluno)

aluno[0] = "Ricardo"
aluno[1] = 31

print(aluno)
print(turma) #Ele junta os dois"""


turma = list()
aluno = list()

for c in range(0,3):
    aluno.append(input("Digite o nome do Aluno: "))
    aluno.append(int(input("Digite a sua idade: ")))
    turma.append(aluno[:]) #Colocando uma copia da lista em
    #vez de referenciar para que as modificações na
    #lista original não afetem a lista da posição atual
    aluno.clear() #Limpar a lista antes de adicionar os dados

#Lista aluno dado temporario.
    
#print(f"A lista aluno tem {aluno}")
#print(f"A lista turma tem {turma}")

"""for aluno in turma:
    print(f"O aluno {aluno[0]} tem {aluno[1]} anos.")

for indice, aluno in enumerate(turma): #pega no objeto(lista) e partir em indice e dados. O primeiro o indice e o segundo os dados.
    print(f"O {indice}º e é o aluno {aluno}")"""

for i in range(0, len(turma)): 
    for aluno in range (0, len(turma[0])):
        #print(i, aluno)
        print(f"{i+1}º  --> ")


