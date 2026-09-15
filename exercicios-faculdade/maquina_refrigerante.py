# Máquina de venda automática de refrigerantes

estoque = {
    "coca": {"preco": 5.00, "quantidade": 3},
    "guarana": {"preco": 4.50, "quantidade": 0},
    "fanta": {"preco": 4.00, "quantidade": 5},
}

def exibir_menu():
    print("\n=== Máquina de Refrigerantes ===")
    for nome, dados in estoque.items():
        status = "disponível" if dados["quantidade"] > 0 else "ESGOTADO"
        print(f"- {nome.capitalize()}: R$ {dados['preco']:.2f} ({status})")
    print("Digite 'sair' para encerrar.\n")

def comprar_refrigerante(escolha, valor_inserido):
    escolha = escolha.lower()

    if escolha not in estoque:
        print("Erro: refrigerante não encontrado no menu.")
        return

    preco = estoque[escolha]["preco"]
    quantidade = estoque[escolha]["quantidade"]

    if quantidade > 0 and valor_inserido >= preco:
        estoque[escolha]["quantidade"] -= 1
        troco = valor_inserido - preco
        print(f"Entregando {escolha}! Troco: R$ {troco:.2f}")
    elif quantidade == 0:
        print(f"Erro: {escolha} está esgotado.")
    elif valor_inserido < preco:
        faltam = preco - valor_inserido
        print(f"Erro: valor insuficiente. Faltam R$ {faltam:.2f}.")

# --- Loop principal (interativo) ---
while True:
    exibir_menu()
    escolha = input("Qual refrigerante você quer? ")

    if escolha.lower() == "sair":
        print("Encerrando a máquina. Até logo!")
        break

    valor_texto = input("Quanto dinheiro você vai inserir? R$ ")
    try:
        valor_inserido = float(valor_texto)
    except ValueError:
        print("Erro: digite um valor numérico válido (ex: 5.00).")
        continue

    comprar_refrigerante(escolha, valor_inserido)