largenum=int(input("Enter a large number: "))
num=1
factors = []
largestfactor = 0

#I tried to divide the number by the factor as soon as I found a factor. THis
#does not work. Because when inputting a number like 36. The program showed
#larget factor was 6. Incorrect. Therefore, when a factor is found, for e.g. 2 in this case,
#that factor should be divided from the number as much as possible.
while True:
    num=num+1
    if (largenum%num==0):
        factors.append(num)
        while(largenum%num==0):
            largenum=largenum/num
    if(largenum==1):
        break
print("Factors are:")
for f in factors:
    print (f)
    if f>largestfactor:
        largestfactor=f
print("Largest factor is: ", largestfactor)
    
    
    
    
    
    
