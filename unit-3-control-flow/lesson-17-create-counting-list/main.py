def create_counting_list(count_to_number):
    result=[]
    i=1
    while count_to_number >= 0:
        
        if count_to_number == 0:
            return result
            
        elif i <= count_to_number:
           result.append(i)
           i=i+1
           
        else:
             return result
            
    else:
        print"Number cannot be negative"
        exit()
        
    

result=create_counting_list(7)
print result
result=create_counting_list(3)
print result
result=create_counting_list(0)
print result
result=create_counting_list(-9)
print result