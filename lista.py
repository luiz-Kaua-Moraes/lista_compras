import colorama #Biblioteca responsável pela cor no teminal
from colorama import Style, Fore, Back, init
import time

init(autoreset= False)

listacompras = []
opcaoMenu = 0


def cores_terminal(id): #id: 1- titulo, 2 - mensgaens de erro, 3- mensgens de dica, 4-Mensagens de sucesso 5- entrada do usuário, 6- tsxto do menu

    def cor_titulo():
        ciano= Fore.CYAN
        return ciano
    
    def cor_erro():
        vermelho = Fore.RED
        return vermelho

    def cor_dica():
        amarelo = Fore.LIGHTYELLOW_EX
        return amarelo

    def cor_sucecesso():
        verde = Fore.LIGHTGREEN_EX
        return verde

    def cor_textoEntrada_Usuario():
        magenta = Fore.MAGENTA
        return magenta
    
    def cor_palavras_menu():
        branco = Fore.WHITE
        return branco
    
    def cor_textoDigitado_usuario():
        amarelo = Fore.YELLOW
        return amarelo
    
    def cor_lista():
        azul = Fore.BLUE
        return azul
    
    if id == 1:
        return cor_titulo()
    
    elif id == 2:
        return cor_erro()

    elif id == 3:
        return cor_dica()
    
    elif id == 4:
        return cor_sucecesso()

    elif id == 5:
        return cor_textoEntrada_Usuario()

    elif id == 6:
        return cor_palavras_menu()
    
    elif id == 7:
        return cor_lista()
    
    elif id == 8:
        return cor_textoDigitado_usuario()



def menu():
    global opcaoMenu

    print(f"\n{cores_terminal(1)} {"="*6} MENU {"="*6}")

    print(f"\n{cores_terminal(6)}1-Adicionar Produto")
    print("2-Remover Produto")
    print("3-Listar Produtos")
    print("4-Procurar Produto")
    print("5-Mostrar quantidade de produtos")
    print("6- Sair")

    try:
        opcaoMenu = int(input(f"{cores_terminal(5)}Informe o número correspondente ao que deseja fazer:{cores_terminal(8)}"))
    except:
        print(f"\n{cores_terminal(2)}Você só pode informar número")
    
def adicionar_produto():
    sequenciaProduto = 1
    print(f"\n{cores_terminal(1)} {"="*6} ADICIONAR PRODUTO {"="*6}")

    while True:
        print(f"\n{cores_terminal(3)}Digite -1 quando quiser parar de adicionar o produto")

        #entrada do produto com sequencia e aumento da primeira letra
        produtoNome = input(f"{cores_terminal(5)}{sequenciaProduto}° produto:{cores_terminal(8)}").capitalize()

        #Verifica se o usuário digitou algo
        if not produtoNome:
            print("Você deve infromar texto")
            continue

        sequenciaProduto +=1
        
        #Verificação para sair do menu de adicionar
        if produtoNome == "-1":
            print(f"\n{cores_terminal(4)}Produtos adicionados com sucesso!")
            print(mensagem_saindo_Ou_voltando("Saindo..."))
            tempo(3)
            break
        #adição do produto à slista
        else:
            listacompras.append(produtoNome)
            
            
def remover_produto():
    sequenciaProduto = 1
    print(f"{cores_terminal(1)}\nREMOVER PRODUTO")

    while True:
        listar_produtos()
        print(f"{cores_terminal(3)}\nDigite -1 quando quiser parar de remover o produto")
        print(f"{cores_terminal(3)}\nPara remover um produto você deve digitar o número que corresponda ao produto")

        try:  
            #Entrada de número do produto a ser removido
            numeroProduto = int(input(f"{cores_terminal(5)}\n{sequenciaProduto}° Produto:{cores_terminal(8)}"))
        
        except ValueError:
            print(f"{cores_terminal(2)}\nSomente números devem ser informados")
            
        else:
            
            if numeroProduto == -1:
                break

            #Impede de remover um número maior ou menor que o tamanho da lista o -1 fica isento
            if numeroProduto <=0 or numeroProduto >len(listacompras):
                print(f"{cores_terminal(2)}Este número não está na lista")
                continue

            #Remove o produto que corresponde ao número e mostra a mensagem com a contagem humanizada de que o produto foi removido com sucesso
            else:
            
                print(f"{cores_terminal(7)}{listacompras[numeroProduto-1]} {cores_terminal(4)}Removido com sucesso!")
                listacompras.remove(listacompras[numeroProduto-1])
                sequenciaProduto +=1

            if not listacompras:
                sair = 0

                print(f"{cores_terminal(3)}Você removeu todos os produtos!")

                while sair != "N":
                    sair = input(f"\n{cores_terminal(5)}Deseja sair? (s/n):{cores_terminal(8)}").capitalize()

                    if sair == "S":
                        mensagem_saindo_Ou_voltando("Saindo...")
                        tempo(3)
                        
                    elif sair == "N":
                        print(f"{cores_terminal(3)}Você removeu todos os produtos!")
                        
                        
                    else:
                        print(f"{cores_terminal(2)}Você só deve informar s ou n")


        
                
def listar_produtos():
    sequencia = 0
    print(f"\n{cores_terminal(1)}LISTA\n")

    for produto in listacompras:
        sequencia +=1
        print(f"{cores_terminal(7)}{sequencia}-{produto}")

def procurar_produto():
    sequenciaProduto = 0
    print(f"{cores_terminal(1)}\nPROCURAR PRODUTO")

    while True:
        print(f"{cores_terminal(3)}\nDigite -1 quando quiser voltar para o menu")

        sequenciaProduto += 1
        nomeProduto = input(f"\n{cores_terminal(5)}{sequenciaProduto}°Produto: ").capitalize()

        if nomeProduto in listacompras:
            print(f"\n{cores_terminal(4)}{nomeProduto} está na lista")

        else:
            print(f"{cores_terminal(2)}{nomeProduto} não está na lista")
            perguntaAdicionar = input(f"\nDeseja adicionar {nomeProduto} à sua lista? (s/n):").capitalize()

            if perguntaAdicionar == "S":
                listacompras.append(nomeProduto)
                print(f"\n{cores_terminal(4)}{nomeProduto} adicionado com sucesso!")

            elif perguntaAdicionar == "N":
                break

            else:
                print(f"{cores_terminal(2)}Você só deve informar s ou n")


def contar_qntd_produtos():
    qntdProdutos = 0
    print(f"{cores_terminal(1)}\nQUANTIDADE DE PRODUTOS")

    for produto in listacompras:
        qntdProdutos +=1
    print(f"{cores_terminal()}\n{qntdProdutos} Produtos na sua lista")

def verificar_se_lista_cheia(funcao):
    if len(listacompras) >=1:
        return funcao()
    else:
        print(f"{cores_terminal(2)}A lista está vazia")

def tempo(tempo):
    return time.sleep(tempo)

def mensagem_saindo_Ou_voltando(mensagem):
    cinza = Fore.LIGHTBLACK_EX
    return f"{cinza}{mensagem}"
    
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
            contar_qntd_produtos
        case 6:
            break
        case _:
            print("Informe um número válido que esteja na lista")


        


