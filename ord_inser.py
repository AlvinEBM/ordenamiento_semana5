def ordenamiento_inser(arr):
    #inicio=1
    for inicio in range(1,len(arr)):
     final=inicio
     while final >0 and arr[final-1]>arr[final]:
        arr[final],arr[final-1]=arr[final-1],arr[final]
        final=final-1

a=[9,8,7,6,5,4,3,2,1]
ordenamiento_inser(a)
print(a)     