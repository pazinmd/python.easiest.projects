
def list_sort(i):
    import random                   #import random method
    listok=[]                       #create blank list
    for i in range(0,i):            #start cycle 
        n = random.randint(-30,30)  #calling  method and using only integer numbers 
        listok.append(n)            #add random numbers in our list
    listok.sort(key = abs)          #sort list using specific key
    print(listok)
    
