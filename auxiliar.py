lista = []
usuario = 0
adicionar = 0

while usuario != 5:
    adicionar = input("ad:")
    lista.append(adicionar)

    if adicionar == "5":
        print(lista)
        remover = int(input(":"))
        lista.remove(lista[remover-1])
        print(lista)

    if adicionar == 6:
        break