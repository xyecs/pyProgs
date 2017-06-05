import itertools

# need to use recursive permutation from 9 to n in tuples of 3
#failed attempt at q566
def permute(n):
    num_list = [x for x in range(9,n)]
    result_list = (list(itertools.permutations(num_list, 3)))
    final_list = []
    
    for three in result_list:
        a, b, c = three[0], three[1], three[2]
        
        if a < b < c:
            final_list.append(three)
            
    return final_list
        
        
def G(n):
    total = 0
    for three in permute(n):
        a, b, c = three[0], three[1], three[2]
        total += F(a,b,c)
        
    return total



def F(a, b, c):
    slices = [(360/a), (360/b), (360/c**0.5)]
    slice_index = 0
    
    icing = 360
    no_icing = 0
    
    flip = 0
    count = 0
    
    icing_state = 1
    
    while (1):
        
        if icing + no_icing != 360:
            print ('You fucked up somewhere')
            break
        
        # exit condition 
        if icing == 360 and flip == 1:
            break         
        
        if slice_index == 3:
            slice_index = 0        
        
        curr_slice = slices[slice_index]

        # add icing 
        if icing_state == 0:  
            
            result = icing + curr_slice
            
            if result > 360:
                no_icing = curr_slice - no_icing 
                icing = 360 - no_icing
            elif result == 360:
                flip = 1
            else: #result < 360
                icing = result
                no_icing = 360 - icing
                
            count += 1
            
                
        # remove icing 
        if icing_state == 1:
         
            result = icing - curr_slice
            
            if result <= 0:
                icing_state = 0
                icing = abs(result)
                no_icing = 360 - icing
            else: #result > 0
                icing = result
                no_icing = 360 - icing
                
                
            count += 1
                 
        slice_index += 1
        
    return count


print (G(20))
print (F(9,10,11))
print (F(10,14,16))

    