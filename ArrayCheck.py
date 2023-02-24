check=[1,2,3,6,4,5,6,7,4,4,3,2,4,5,3,2,4]

for i in range(0,len(check)):
    for j in range(i+2,len(check)-1):
        if check[i]==check[j]:
            print(f"{check[j]} has Duplicate Value ")


