def siva(list):
    for index in range(1,len(list)):
        currentvalue=list[index]
        position=index
        while position>0 and list[position-1]> currentvalue:
            list[position]=list[position-1]
            position=position-1
        list[position]=currentvalue

        

list=[9,8,7,5,6,4,2,1,3]
siva(list)
print(list)

        
        
  
