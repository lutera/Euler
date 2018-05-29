target=1000
sum=0
#simply add multiples of either 3 or 5 and print the sum. hard coded upper limit of 1000.
for i in range(1,target):
    if ((i%3==0) or (i%5==0)):
        sum=sum+i
print (sum)


    
