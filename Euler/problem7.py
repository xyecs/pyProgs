from bitarray import bitarray

def sieve_primes(limit):
    sieve = bitarray([False]) * (limit+1)
    primes = []
    primes_found = 0

    for i in range(2, limit):
        if sieve[i]:
            continue
        for j in xrange(i*2, limit, i):
            sieve[j] = True
            
        primes.append(i)
        primes_found += 1
        if primes_found == 10001:
            break
        
    return primes

primes = sieve_primes(1000000)
print primes[-1]