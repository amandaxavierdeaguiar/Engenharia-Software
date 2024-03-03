""" Crie um sistema que utilize o interactivehelpdo python. O utilizador deve digitar o comando e o sistema deve retornar o manual. Quando o utilizador digitar “FIM” o programa deve encerrar."""

def main():
    print("Bem-vindo ao sistema de ajuda interativa do Python!")
    print("Para ver o manual de um comando, digite-o abaixo. Digite 'FIM' para sair.")

    while True:
        command = input("\nComando: ").lower()

        if command == "fim":
            print("Até mais!")
            break

        else:
            try:
                help(command)
            except Exception as e:
                print(f"Não foi possível encontrar o manual para '{command}'. Erro: {e}")

main()