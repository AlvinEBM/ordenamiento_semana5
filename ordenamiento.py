def ordenamiento(arr):
    for mano in range(len(arr)-1):
        posmin=mano
        for ojo in range(mano +1,len(arr)):
            if arr[ojo]<arr[posmin]:
                posmin=ojo
        arr[mano],arr[posmin]=arr[posmin],arr[mano]

a=[100,1,2,8,9,3,4,7,10,5]
ordenamiento(a)
print(a)