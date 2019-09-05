print("this is fragile. enter only great than 2 whole numbers")

occur=int(input("Enter the occurence of the prime number you want: "))
x=2
num=3

#First to write the logic to determine if a number is prime or not.
#Ignore even numbers

while True:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # number is not prime
            break  # exit from for loop
    

    if is_prime:
        if(x==occur):
            print("Found: ",num)
            break
        x=x+1
        num=num+2
    else:
        num=num+2

print("Done")
    

        
    
    
        
    

        
        
        
        


    
        
            
    


