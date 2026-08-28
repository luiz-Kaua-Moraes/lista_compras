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

    try:
        opcaoMenu = int(input("\nInforme o número correspondente o que deseja fazer:"))
    except:
        #Vermelhho
        print("\nVocê só pode informar número")

    
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
    sequenciaProduto = 1
    print("\nREMOVER PRODUTO")

    while True:
        listar_produtos()
        print("\nDigite -1 quando quiser parar de remover o produto")
        print("\nPara remover um produto você deve digitar o número que corresponda ao produto")

        try:
            #Entrada de número do produto a ser removido
            numeroProduto = int(input(f"\n{sequenciaProduto}° Produto:"))

        
        except ValueError:
            print("\nSomente números devem ser informados")
            
        else:
            
            if numeroProduto == -1:
                break

            #Impede de remover um número maior ou menor que o tamanho da lista o -1 fica isento
            if numeroProduto <=0 or numeroProduto >len(listacompras):
                print("Este número não está na lista")
                continue

            #Remove o produto que corresponde ao número emostra a mensagem com a contagem humanizada de que o produto foi removido com sucesso
            else:
                print(f"{listacompras[numeroProduto-1]} Removido com sucesso!")
                listacompras.remove(listacompras[numeroProduto-1])
                sequenciaProduto +=1
                
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

def verificar_se_lista_cheia(funcao):
    if len(listacompras) >=1:
        return funcao()
    else:
        print("A lista está vazia")
    
while opcaoMenu !=6:
    menu()
    match opcaoMenu:
        case 1:
            adicionar_produto()
        case 2:
            verificar_se_lista_cheia(remover_produto)
        case 3:
            verificar_se_lista_cheia(listar_produtos)
        case 4:
            verificar_se_lista_cheia(procurar_produto)
        case 5:
            verificar_se_lista_cheia(contar_qntd_produtos)
        case 6:
            break
        case _:
            print("Informe um número válido que esteja na lista")


        


