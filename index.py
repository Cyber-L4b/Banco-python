import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [1] Criar usuário
    [2] Criar conta
    [3] Depositar
    [4] Sacar
    [5] Extrato
    [6] Listar contas
    [7] Sair
    => """
    return input(textwrap.dedent(menu))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        contas.append({
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        })
        print("Conta criada com sucesso!")
    else:
        print("Usuário não encontrado! Cadastre-o primeiro.")

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor excede o limite de saque.")
    elif numero_saques >= limite_saques:
        print("Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Valor inválido para saque.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: {conta['agencia']}
        Conta: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print("=" * 30)
        print(textwrap.dedent(linha))

# Programa principal
AGENCIA = "0001"
usuarios = []
contas = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = menu()

    if opcao == "1":
        criar_usuario(usuarios)

    elif opcao == "2":
        numero_conta = len(contas) + 1
        criar_conta(AGENCIA, numero_conta, usuarios, contas)

    elif opcao == "3":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "4":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "5":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "7":
        print("Saindo... Volte sempre!")
        break

    else:
        print("Operação inválida. Tente novamente.")
