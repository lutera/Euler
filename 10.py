num=2000000
sumofprimes=5

for primesuspect in range(5,num,2):
    is_prime = True
    for i in range(2, primesuspect//2):
        if primesuspect % i == 0:
            is_prime = False  # number is not prime
            break  # exit from for loop

    if is_prime:
        print(primesuspect)
        sumofprimes=sumofprimes+primesuspect

print(sumofprimes)
    
