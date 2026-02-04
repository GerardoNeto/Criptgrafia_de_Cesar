import os


# Interface

def limpar_tela():
    os.system("clear" if os.name == "posix" else "cls")


def cabecalho():
    print("=" * 45)
    print("        Cifra de César - ICC")
    print("=" * 45)


def menu():
    print("[1] Criptografar mensagem")
    print("[2] Descriptografar mensagem")
    print("[3] Ataque de Força Bruta")
    print("[4] Criptografar arquivo .txt")
    print("[5] Descriptografar arquivo .txt")
    print("[0] Sair")


# Functions


def normalizar_chave(chave):
    return chave % 26


def cifrar(texto, chave):
    chave = normalizar_chave(chave)
    resultado = ""

    for c in texto:
        if c.isupper():
            codigo = ord(c) - ord('A')
            resultado += chr((codigo + chave) % 26 + ord('A'))

        elif c.islower():
            codigo = ord(c) - ord('a')
            resultado += chr((codigo + chave) % 26 + ord('a'))

        else:
            resultado += c

    return resultado


def decifrar(texto, chave):
    return cifrar(texto, -chave)


def brute_force(texto_cifrado):
    print("\nAtaque de Força Bruta")
    print("Testando todas as 25 chaves possíveis.\n")

    for chave in range(1, 26):
        tentativa = decifrar(texto_cifrado, chave)
        print(f"Chave {chave:02d}: {tentativa}")

    print("\nA cifra de César é insegura pois possui poucas chaves.")


def ler_arquivo(nome):
    try:
        with open(nome, "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print("ERRO: arquivo não encontrado.")
        return None


def salvar_arquivo(nome, conteudo):
    with open(nome, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)


def cifrar_arquivo(entrada, saida, chave):
    texto = ler_arquivo(entrada)
    if texto is not None:
        salvar_arquivo(saida, cifrar(texto, chave))
        print("Arquivo criptografado com sucesso!")


def decifrar_arquivo(entrada, saida, chave):
    texto = ler_arquivo(entrada)
    if texto is not None:
        salvar_arquivo(saida, decifrar(texto, chave))
        print("Arquivo descriptografado com sucesso!")


# Main

while True:
    limpar_tela()
    cabecalho()
    menu()

    opcao = input("\nEscolha uma opção: ")

    if opcao == '0':
        print("\nEncerrando o programa. Até mais!")
        break

    elif opcao == '1':
        mensagem = input("\nDigite a mensagem: ")

        try:
            chave = int(input("Digite a chave (1 a 25): "))
            print("\nMensagem criptografada:")
            print(cifrar(mensagem, chave))
        except ValueError:
            print("ERRO: a chave deve ser um número inteiro.")

    elif opcao == '2':
        mensagem = input("\nDigite a mensagem cifrada: ")

        try:
            chave = int(input("Digite a chave usada: "))
            print("\nMensagem original:")
            print(decifrar(mensagem, chave))
        except ValueError:
            print("ERRO: a chave deve ser um número inteiro.")

    elif opcao == '3':
        mensagem = input("\nDigite a mensagem criptografada: ")
        brute_force(mensagem)

    elif opcao == '4':
        entrada = input("\nArquivo de entrada (.txt): ")
        saida = input("Arquivo de saída (.txt): ")

        try:
            chave = int(input("Digite a chave: "))
            cifrar_arquivo(entrada, saida, chave)
        except ValueError:
            print("ERRO: a chave deve ser um número inteiro.")

    elif opcao == '5':
        entrada = input("\nArquivo criptografado (.txt): ")
        saida = input("Arquivo de saída (.txt): ")

        try:
            chave = int(input("Digite a chave usada: "))
            decifrar_arquivo(entrada, saida, chave)
        except ValueError:
            print("ERRO: a chave deve ser um número inteiro.")

    else:
        print("ERRO: opção inválida.")

    input("\nPressione ENTER para continuar...")
