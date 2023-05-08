def random():
    from random import randint
    print("Matrix generator filled with random numbers\n")
    try:
        lin=int(input("Type the number of lines you want: "))
        col=int(input("Type the number of columns you want: "))
        print(" ")
    except:
        print("Invalid input. Try a whole number.")
        random()
    else:
        i=0
        lista=[]
        while i < lin:
            lista.append([])
            j=0
            while j < col:
                x = randint(1, 50)
                if x in lista:
                    continue
                else:
                    lista[i].append(x)
                    j+=1
            i+=1
        print("This is the matrix generated with random numbers:\n")
        i=0
        while i < lin:
            j=0
            print("|", end="")
            while j < col:
                print("{0:4}".format(lista[i][j]), end="")
                j+=1
            print(" |")
            i+=1
random()