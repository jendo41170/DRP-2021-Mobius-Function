# base

import math

def isPrime(n) :
  
    if (n < 2) :
        return False
    for i in range(2, n + 1) :
        if (i * i <= n and n % i == 0) :
            return False
    return True
  
def mobius(N) :
      
    # Base Case
    if (N == 1) :
        return 1
  
    # For a prime factor i 
    # check if i^2 is also
    # a factor.
    p = 0
    for i in range(1, N + 1) :
        if (N % i == 0 and 
                isPrime(i)) :
  
            # Check if N is
            # divisible by i^2
            if (N % (i * i) == 0) :
                return 0
            else :
  
                # i occurs only once, 
                # increase f
                p = p + 1
  
    # All prime factors are
    # contained only once
    # Return 1 if p is even
    # else -1
    if(p % 2 != 0) :
        return -1
    else :
        return 1
