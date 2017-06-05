x = 1000;
total = 0;


for i in range(x+1):
    if i % 3 == 0 or i % 5  == 0:
        total += i;



'''
# Alternative method
count = 1
while ((3*count) < x):
    total += 3*count
    count+=1
    
count = 1 
while ((5*count) < x):
    total += 5*count
    count += 1
'''
 
  
print (total)