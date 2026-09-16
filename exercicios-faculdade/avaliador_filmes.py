filmes = ["Matrix", "Interestelar", "Duna", "Vingadores", "Coringa"]

print("Bem-vindo à classificação de filmes!")
print("Você tem cinco filmes para classificar.")
print("Digite '0' a qualquer momento para parar o programa.\n")

parar = False  # flag que controla se o programa deve encerrar

for filme in filmes:
    if parar:
        break  # sai do for se a flag já foi ativada

    while True:
        classificacao = input(f"Como você classifica '{filme}' de 1 a 5? (ou 0 para parar): ")

        if classificacao == '0':
            print("Encerrando o programa.")
            parar = True   # avisa pro for que é pra parar
            break          # sai do while

        classificacao = int(classificacao)

        if classificacao < 1 or classificacao > 5:
            print("Nota inválida, tente novamente.")
        else:
            print(f"Você classificou '{filme}' com {classificacao} estrelas.\n")
            break  # sai do while porque a nota foi válida

    print()