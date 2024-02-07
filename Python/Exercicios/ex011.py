"""Crie um programa que leia uma frase e mostre:
1 - Quantas vezes aparece a letra "A" 
2 - Em que posição aparece a primeira vez
3 - Em que posição aparece a última vez"""

frase_usuario = input("Digite sua frase: ").upper().strip()
quantidade_a = frase_usuario.count("A")
primeiro_a = frase_usuario.find("A") + 1
ultimo_a = frase_usuario.rfind("A") + 1

print(f"Sua Frase aparece {quantidade_a} letras A")
print(f"Em que posição aparece a primeira vez? {primeiro_a}")
print(f"Em que posição aparece a última vez? {ultimo_a}")
