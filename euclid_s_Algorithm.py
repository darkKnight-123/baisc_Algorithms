#Euclid's Algorithm to find GCD of two (not-both-0) integers
#Computes gcd(m,n) using Euclid's Algorithm
#Input: Two non negative, not-both-0 integers m and n
#Output: The Greatest Common Divisor (GCD/HCF) of m and n


def euclid_gcd(m,n): #function definition
#algorithm start  
    while n != 0: 
        r = m % n
        m = n
        n = r
    return m 
#algorithm end

print("The gcd for the numbers 60 and 12 is:",euclid_gcd(60,12))
