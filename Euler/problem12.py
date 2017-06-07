def triangular_num(n):
    total_sum = 0
    for i in range(n+1):
        total_sum += i
    return total_sum

found = 0
counter = 10
while found == 0:

    divisors = []
    value = triangular_num(counter)
    for i in range(1, int(value**0.5)+1):
        if value % i == 0:
            divisors.append(i)
            if i != value/i:
                divisors.append(i)
    if len(divisors) > 500:
        found = value
        break
    counter+= 1

print found