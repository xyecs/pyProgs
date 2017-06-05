n = 999999

longest_chain_length = 0
longest_chain_start_num = 0

for i in range(n, n//2, -1):
    
    start = i
    steps = 0
    while start != 1:
        if start % 2 == 0:
            start = start/2
        else:
            start = 3*start + 1
        steps += 1
        
    if steps > longest_chain_length:
        longest_chain_length = steps
        longest_chain_start_num = i
        
print longest_chain_start_num