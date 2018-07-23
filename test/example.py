number_lines=0
words=[]
chars=[]

with open('alice.txt','r') as readfile:
    for line in readfile:
        number_lines+=1
        print(line)
        words+=line.split(" ")
        print(number_lines)
        
        char_count= [ len(i) for i in words]
        for j in char_count:
            print(j)
            
        print("char_count",sum(char_count) ) 
        

        #print("Char count is :",sum(chars)) 
        print("words count",len(words))        

     

