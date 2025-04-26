def ordena_bur(lista):
    for inicio in range(1,len(lista)):
        for final in range(0,len(lista)-1):
            if lista[final]>lista[final+1]:
                #inicio=final
                lista[final],lista[final+1]=lista[final+1],lista[final]

a=[9,8,7,6,5,4,3,2,1]
ordena_bur(a)
print(a)     