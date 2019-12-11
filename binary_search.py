def siva(list):
    for siva in range(len(list)-1,0,-1):
        for i in range(siva):
            if list[i]>list[i+1]:
               k=list[i]
               list[i]=list[i+1]
               list[i+1]=k
 

list=[9,8,5,7,6,2,3,1]
siva(list)
print(list) 
