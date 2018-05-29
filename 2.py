sum=0
num1=1
num2=2
bucket=0
while True:
    if num2 > 4000000:
        break
    elif num2%2==0:
        sum=sum+num2
    bucket=num1
    num1=num2
    num2=bucket+num2
print (sum)


    
