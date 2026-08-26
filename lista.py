listacompras = []
opcaoMenu = 0

def menu():
    global opcaoMenu
    print("\nMENU")
    print("\n1-Adicionar Produto")
    print("2-Remover Produto")
    print("3-Listar Produtos")
    print("4-Procurar Produto")
    print("5-Mostrar quantidade de produtos")
    print("6- Sair")

    opcaoMenu = int(input("\nInforme o número correspondente o que deseja fazer:"))
    
def adicionar_produto():
    sequenciaProduto = 1
    print("\nADICIONAR PRODUTO")

    while True:
        print("\nDigite sair quando quiser parar de adicionar o produto")
        produtoNome = input(f"\n{sequenciaProduto}° produto:")
        sequenciaProduto +=1

        listacompras.append(produtoNome)

def remover_produto():
    sequenciaProduto = 1
    print("\nREMOVER PRODUTO")
    while True:
        print("\nDigite sair quando quiser parar de remover o produto")
        print("\nPara remover um produto você deve digitar o número que corresponde ao produto")
        numeroProduto = int(input(f"\n{sequenciaProduto}° Produto:"))
        sequenciaProduto +=1

        listacompras.remove(numeroProduto)

def listar_produtos():
    print("\nLISTA")
    for produto in listacompras():
        print(produto)

def procurar_produto():
    sequenciaProduto = 1
    print("\nPROCURAR PRODUTO")

    while True:
        print("\nDigite sair quando voltar para o menu")
        nomeProduto = input(f"\n{sequenciaProduto}°Produto")
        sequenciaProduto += 1

        if nomeProduto in listacompras:
            print("Está na lista")

def contar_qntd_produtos():
    qntdProdutos = 0
    print("\nQUANTIDADE DE PRODUTOS")

    for produto in listacompras():
        qntdProdutos +=1
    print(f"\n{qntdProdutos}")

while opcaoMenu !=6:
    menu()
    match opcaoMenu:
        case 1:
            adicionar_produto()
        case 2:
            remover_produto()
        case 3:
            listar_produtos()
        case 4:
            procurar_produto()
        case 5:
            contar_qntd_produtos()
        case 6:
            break


        


