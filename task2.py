#array = [1, 2, 3, 44, 43, 7, 77, 42, 5, 10, 11, 14]
#i = 0

#for x in array:
    #if x % 7 == 0:
        #print(x, i)
    #i += 1


array = [4, 8, 7, 65, 77, 99, 1246, 9999]
result = []
for i, x in enumerate(array):
    if x % 7 == 0:
        result.append((x,i))
        print(x, i)

print(result)