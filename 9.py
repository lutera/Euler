outerloop=1
innerloop=1
found = False
for a in range(1000,0,-1):
    outerloop=outerloop+1
    for b in range(1,1000-a):
        innerloop=innerloop+1
        c=1000-a-b
        if(c**2==a**2+b**2):
            print(a,b,c,a*b*c)
            found = True
            break
    if (found == True):
        break

print(outerloop,innerloop)


        
    
    

    
    




                       
        
            
    
        

       
        

        
    
