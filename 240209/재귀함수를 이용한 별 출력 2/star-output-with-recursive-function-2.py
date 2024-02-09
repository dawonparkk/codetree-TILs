def star(x):
    for i in range(x): 
        i = x-i
        if i==1:
            print('*'*i,end="")
        else:
            print('*'*i)
    for i in range(x): 
        print('*'*i)        
    
    
n = int(input())
star(n)