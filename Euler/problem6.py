sum_sq = 0
sq_sum = 0

x = 100

for i in range(x+1):
    sum_sq += i**2
    sq_sum += i
    
print sq_sum**2 - sum_sq