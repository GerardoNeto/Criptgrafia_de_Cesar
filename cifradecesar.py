
# Functions

def cabecalho():
    print("-" * 40)
    print("Criptografia de Cesar")
    print("-" * 40)


def cifrar(texto, chave):
    resultado = ""
    
    for caractere in texto:

        if caractere.isupper():
            codigo_original = ord(caractere) - ord('A')
            novo_codigo = (codigo_original + chave) % 26
            nova_letra = chr(novo_codigo + ord('A'))
            resultado += nova_letra

        elif caractere.islower():
            codigo_original = ord(caractere) - ord('a')
            novo_codigo = (codigo_original + chave) % 26
            nova_letra = chr(novo_codigo + ord('a'))
            resultado += nova_letra
            
        else:
            resultado += caractere
            
    return resultado


def decifrar(texto, chave):
    return cifrar(texto, -chave)


def brute_force(texto_cifrado):

    print("\n Usando BruteForce")
    print("Todas as possibilidades:\n")
    
    for tentativa_chave in range(1, 26):
        texto_tentativa = decifrar(texto_cifrado, tentativa_chave)
        print(f"Chave {tentativa_chave:02d}: {texto_tentativa}")
    
    print("\nProcure a frase legivel")

# MainCode

while True:
    cabecalho()
    print("1. Criptografar Mensagem")
    print("2. Descriptografar Mensagem")
    print("3. BruteForce")
    print("0. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '0':
        print("See you next time.")
        break
        
    if opcao == '1':
        msg = input("Digite a mensagem: ")

        try:
            chave = int(input("Digite a chave(Deslocamento numerico): "))
            print(f"\nResultado: {cifrar(msg, chave)}")

        except ValueError:
            print("ERROR: A chave precisa ser um numero inteiro")
            
    elif opcao == '2':
        msg = input("Digite a mensagem cifrada: ")

        try:
            chave = int(input("Qual foi a chave usada?: "))
            print(f"\nMensagem Original: {decifrar(msg, chave)}")

        except ValueError:
            print("ERRO: A chave necessita ser um numero inteiro")

    elif opcao == '3':
        msg = input("Digite a mensagem criptografada: ")
        brute_force(msg)
        
    else:
        print("Nao existe essa opção, tente novamente")
    
    input("\nPressione ENTER para continuar...")
    print("\n" * 2)
