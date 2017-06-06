total_sum = 1000
a_max = total_sum // 3
b_max = total_sum // 2

for a in range(1, a_max):
    for b in range(a+1, b_max):
        c = total_sum - a - b
        if (a**2 + b**2) == c**2:
            print a*b*c
