# WAP  in  python to sort the following list.
# LIST = [25, 47, -23, 0, -50, 24 8 1 9 10]


LIST = [25, 47, -23, 0, -50, 24, 8, 1, 9, 10]
for i in range(len(LIST)):
    for j in range(i + 1, len(LIST)):
        if LIST[i] > LIST[j]:
            temp = LIST[i]
            LIST[i] = LIST[j]
            LIST[j] = temp
print( "SORTED LIST :" , LIST)
