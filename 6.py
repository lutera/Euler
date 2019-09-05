print("This program will give the difference between the sum of the squares of the consecutive natural numbers and the square of the sum.")
lowerlimit = int(input("Enter the Lower Limit:"))
upperlimit = int(input("Enter the Upper Limit:"))

sumofsquares = 0
sumofnum = 0
#Or we can use the formulae like n(n+1)/2
for num in range(lowerlimit,upperlimit+1):
    sumofsquares = sumofsquares + num**2
    sumofnum = sumofnum + num

squareofsum = sumofnum**2
print("Sum of squares: ",sumofsquares)
print("Square of sum: ",squareofsum)
print("Difference is: ",squareofsum-sumofsquares)
