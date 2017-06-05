first_term = 1
second_term = 2
next_term = 0

total = 0
max_value = 4000000

while first_term <= max_value and second_term <= max_value:
    
    next_term = first_term + second_term
    
    if first_term % 2 == 0:
        total += first_term  
    
    first_term = second_term
    second_term = next_term
    
    
if first_term % 2 == 0:
    total += first_term 
if second_term % 2 == 0:
    total += second_term 

print total