import random
import math

#likePrime = 0
#composite = 0
#pc = 5
#Function to get our values/canadiates of prime numbers 
def oddNum(a,b):
    odds = []
    if a % 2 == 0:
        a = a + 1
    for x in range(a, b, 2):
        odds.append(x)
    return odds

def fast_power(base, power, pc):
    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base) % pc

        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = (base * base) % pc
    return result

def findUR(pc): # square and multiple equation
    u = 0
    temp = (2**u)
    #temp < (pc-1)
    while ((pc-1)/(temp)).is_integer():
        u+=1
        temp = (2**u)
    u -= 1
    r = (pc-1) / (2**u)
    return u,r
    
def millerRabin(pc):
    i = 1
    j = 1
    likePrime = 0
    composite = 0
    uandr = findUR(pc) # this sends your prime canidate over to a helper function to generate the u and the r
    u = uandr[0]
    r = uandr[1]
    for i in range(4): # have 10 be our security parameter
        a = random.randrange(2,pc-2)
        # remainder = (a**(pc-1)) % pc # this will get the remainder which will be used to check conditions 
    #   uandr = findUR(pc) # this sends your prime canidate over to a helper function to generate the u and the r
    #   u  = uandr[0]
    #   r = uandr[1]
        #z = (a**r) % pc # 
        z = pow(a,r,pc)
        if z != 1 and z != pc-1:
            for j in range(u-1):
                #z = fast_power(z,2,pc)
                z = (z*z) % pc
                if z == 1:
                    composite +=1
                    print("here")
                    #return("P is composite")
                if z != pc-1:
                    composite +=1
                    print("here")
                    #return("P is composite")
    #likePrime+=1
    print(composite)
    errorprob = ("Number " + str(pc) + " False Positive Rate: " + str((composite/(pc-3)) * 100) + "%")
    return errorprob


       

if __name__ == '__main__':
    #templist = oddNum(95000, 105000)
    print(millerRabin(26))
    #for i in templist:
    #    print(i)
    #uandr = findUR(53) # this sends your prime canidate over to a helper function to generate the u and the r
    #u = uandr[0]
    #r = uandr[1]
    #print(u)
    #print(r)
    #millerRabin(53)
    #temp = findUR(50)
    #print(fast_power(2,1,53))
    #print(temp[0])
    #print(temp[1])
    #print("The u that I got was: " + str(u) + " And the r that I got was: ", + str(r))
