print("This program will give the lowest common multiple of consecutive numbers from the lower limit to the upper limit")
lowerlimit = int(input("Enter the Lower Limit:"))
upperlimit = int(input("Enter the Upper Limit:"))

factorsandcount = []

for checknum in range(upperlimit,lowerlimit,-1):
    num = 1
    while True:
        num=num+1
        if (checknum%num==0):
            factor = num
            factorcounted = False
            counter = 0
            while(checknum%factor == 0):
                checknum = checknum/factor
                counter = counter + 1
            for i in range(len(factorsandcount)):
                if factorsandcount[i][0] == factor:
                    if factorsandcount[i][1] >= counter:
                        factorcounted = True
                        #break
                    else:
                        factorsandcount[i][1] =  counter
                        factorcounted = True
            if factorcounted == True:
                continue
            else:
                factorsandcount.append([0,0])
                j = len(factorsandcount) -1
                factorsandcount[j][0] = factor
                factorsandcount[j][1] = counter
                factorcounted = True
                #break
        if(checknum==1):
            break
LCM = 1
for x in range(len(factorsandcount)):
    LCM = LCM * (factorsandcount[x][0] ** factorsandcount[x][1])
print("Factors and their powers:")
print(factorsandcount)
print("LCM: ",LCM)
