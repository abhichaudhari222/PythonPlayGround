myEle=[1,2,3,4,5,6,7,8,1,2,2]
for i in range(0,len(myEle)):
    count =1
    for j in range(i+1,len(myEle)):
        if (myEle[i]==myEle[j]):
            count +=1
            print(str(myEle[i])+" is Duplicated "+ str(count)+" Times")
            
            
            