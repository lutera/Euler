print("This module calculates the largest palindrome in the products of all X digit and Y digit numbers. Enter X and Y")
A = int(input("Enter A>>>"))
B = int(input("Enter B>>>"))
maxnuma = 10**A - 1
minnuma = 10**(A-1) - 1
maxnumb = 10**B - 1
minnumb = 10**(B-1) - 1


palindromelist = []
for y in range(maxnuma,minnuma,-1):
    for x in range(maxnumb,minnumb,-1):
        checknum=product=x*y
        reversestring = []
        reverse  = 0
        loop = True
        while loop:
            reversestring.append(checknum%10)
            checknum=int(checknum/10)
            if(checknum==0):
                loop=False
        i=0
        for j in range(len(reversestring),0,-1):
            powersof10 = j - 1
            reverse = reverse + reversestring[i]*10**powersof10
            i = i+1    
        if (reverse==product):
            palindromelist.append(reverse)
            #print("Product of ",x," and ",y," is ",product," which is a palindrome because"
            #          " it is equal to: ",reverse)
            #print("End")
            break
            #exit(0)
        else:
            del reversestring
            del reverse
            del i
            continue

print("There are a total ", len(palindromelist), "palindromes in the list of products of all ",A," and ",B,"  digit numbers and the largest of them is", max(palindromelist),".")
    


    
    
