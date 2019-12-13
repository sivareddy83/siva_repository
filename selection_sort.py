def siva(list):
    s=len(list)
    for i in range(0,s):
        for j in range(i+1,s):
            if list[j]<list[i]:
               min=list[j]
               list[j]=list[i]
               list[i]=min

list=[9,5,7,8,4,6,2,1,3]
siva(list)
print(list)  
