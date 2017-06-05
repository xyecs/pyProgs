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

primes = sieve_primes(2000000)
print sum(primes)