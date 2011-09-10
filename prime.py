from math import ceil
from math import log
from time import time
def nthprime(n):
    if n <=0:
        print ("invalid input (less than one)")
    elif n ==1:
        print ("First prime is 2!")
        return 2
    elif n == 2:
        print ("Second prime is 3!")
        return 3
    primelist = [2,3]
    nth_prime =3
    # guestimate the maximum number of iteration to run
    large_num = int(ceil((n*((1+2*log(n))/(log(n))+(log(n))))))
    print large_num
    x=3
    while x<= large_num:
        x+=2
        prime_factor_found = False
        #below for question regarding prime set with largest prime below 2mil
        #if x >= 2000000:
            #print (sum(primelist))
            #return True
        for y in primelist:
            if y**2 > x: # search for a prime factor until square root of the number
                break
            elif not x%y: # if no remainder, y is a prime factor
                prime_factor_found = True
                break
        if prime_factor_found:
            pass
        else:
            primelist.append(x)
            if nth_prime == n:
                print (str(x)+" is "+str(n)+"th prime!")
                return x
            nth_prime += 1
    return primelist
                    
if __name__ == "__main__":
    number = int(raw_input("What nth prime do you want to find?"))
    print ("Finding "+str(number)+"th prime.")
    t = time()
    nthprime(number)
    print (time()-t)

