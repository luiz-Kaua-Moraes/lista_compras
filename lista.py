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
    sequenciaProduto = 0
    print("\nADICIONAR PRODUTO")

    while True:
        print("\nDigite -1 quando quiser parar de adicionar o produto")

        #entrada do produto com sequencia e aumento da primeira letra
        sequenciaProduto +=1
        produtoNome = input(f"\n{sequenciaProduto}° produto:").capitalize()
        
        #Verificação para sair do menu de adicionar
        if produtoNome == "-1":
            break
        #adição do produto à slista
        else:
            listacompras.append(produtoNome)
            

def remover_produto():
    sequenciaProduto = 0
    print("\nREMOVER PRODUTO")

    while True:
        listar_produtos()

        print("\nDigite -1 quando quiser parar de remover o produto")

        print("\nPara remover um produto você deve digitar o número que corresponde ao produto")

        sequenciaProduto +=1
        numeroProduto = int(input(f"\n{sequenciaProduto}° Produto:"))
       

        if numeroProduto == -1:
            break
        else:
            listacompras.remove(listacompras[numeroProduto-1])
            
def listar_produtos():
    sequencia = 0
    print("\nLISTA\n")

    for produto in listacompras:
        sequencia +=1
        print(f"{sequencia}-{produto}")

def procurar_produto():
    sequenciaProduto = 0
    print("\nPROCURAR PRODUTO")

    while True:
        print("\nDigite -1 quando quiser voltar para o menu")

        sequenciaProduto += 1
        nomeProduto = input(f"\n{sequenciaProduto}°Produto: ").capitalize()

        if nomeProduto in listacompras:
            print(f"{nomeProduto} está na lista")

        else:
            print(f"{nomeProduto} não está na lista")
            perguntaAdicionar = input(f"\nDeseja adicionar {nomeProduto} à sua lista? (s/n):").capitalize()

            if perguntaAdicionar == "S":
                listacompras.append(nomeProduto)
                print(f"\n{nomeProduto} adicionado com sucesso!")

            elif perguntaAdicionar == "N":
                break

            else:
                print("Você só deve informar s ou n")


def contar_qntd_produtos():
    qntdProdutos = 0
    print("\nQUANTIDADE DE PRODUTOS")

    for produto in listacompras:
        qntdProdutos +=1
    print(f"\n{qntdProdutos} Produtos na sua lista")

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


        


