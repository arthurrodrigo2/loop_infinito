# Loop infinito
while True:
    # tratamento da exceção
    try:
        # declaração de variáveis
        nome = input('informe seu nome: ')
        idade = int(input('informe sua idade: '))

        # ternário
        saida = "É maior de idade." if idade >= 18 else "É menor de idade."

        # saída de dados
        print(f"{nome} {saida}")

        # verificação se o usuário deseja fazer outra verificação
        continuar = input("Deseja continuar? 'sim' para continuar ou outro valor para encerrar:").lower()
        if continuar == "sim":
            continue
        else:
            break 
    except Exception as e:
        print(f"Não foi possível verificar a maioridade. {e}")
    finally:
        print("Programa finalizado.")