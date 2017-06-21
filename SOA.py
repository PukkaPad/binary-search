def sieveOfAtkin(MaxN):
    '''
    https://en.wikipedia.org/wiki/Sieve_of_Atkin#Pseudocode

    Note that I do not need to go over N**0.5. I need to check all prime factors up to the square root of the limit (if N = 130, I must check up to int(130**0.5) which is 11. I do not need to check anything higher, because any number divisible by a larger number would also be divisible by a number less than the square root of N).
    Note that I had to add 1 to the limit because of the way range/xrange works.
    '''
    n1=[1, 13, 17, 29, 37, 41, 49, 53]
    n2=[ 7, 19, 31, 43]
    n3=[11, 23, 47, 59]
    P = [2,3,5] # Create a results list, filled with 2, 3, and 5
    sieve=[False]*(MaxN+1)  # Create a sieve list with an entry for every positive integer, marked as non prime
    # I need to compute n
    # I will flip the entry - flipping means changing the marking to the opposite marking
    for x in range(1,int(MaxN**0.5+1)):
        for y in range(1,int(MaxN**0.5+1)):
            n = 4*x**2 + y**2
            if n<=MaxN and n%60 in n1 :
                sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= MaxN and n%60 in n2 :
                sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=MaxN and n%60 in n3 :
                sieve[n] = not sieve[n]
    for x in range(7,int(MaxN)):
        if sieve[x]: # this will print True at 7
            for y in range(x**2,MaxN+1,x**2): # Square the number and mark all multiples of that square as non prime
                sieve[y] = False
    for p in range(7,MaxN):
        if sieve[p] : P.append(p)
    return P

