from bitarray import bitarray

def sieve_primes(limit):
    sieve = bitarray([False]) * limit
    primes = []

    for i in range(2, limit):
        if sieve[i]:
            continue
        for j in xrange(i*2, limit, i):
            sieve[j] = True
            
        primes.append(i)
    return primes

n = 600851475143
primes = sieve_primes(int(n**0.5))

for i in range(len(primes)-1 , -1, -1):
    if n % primes[i] == 0:
        print primes[i]
        break
        