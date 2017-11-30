import readline # for reading in input correctly
import os # for centering output

# Calculator based on the infix notation
# By Shardul Shah

# Things to add later on:
# Exponents
# Brackets
# Decimals
# Negative numbers
# GUI (possibly)
# A loop to output results based on os.get_terminal_size().

def center_amnt():
   num_col =  os.get_terminal_size().columns
   return num_col


def dict_to_list(a_dict):
    
    converted_l = []
    
    for i in range(len(a_dict)):
        converted_l.append(a_dict[i])
          
    print(converted_l)          
    return converted_l          
    

def do_math(all_dict): # always first function call with counter = 0 (doesn't matter though)
    
    counter = 0 # for potential later use
    
    all_list = dict_to_list(all_dict)
    
    num_items = len(all_list)
    
    while (num_items != 1):
        
        # need these 4 variables as if there is a statement like "40/30/50/90", there will be mistakes, which can only be avoided with these; in short,
        # do each of one +, -, /, * operation only once in a math statement, and do it until there is only one element left in the list.
        div_bool = False
        mult_bool = False
        sub_bool = False
        add_bool = False
                
        # note 2 for loops : one for the "DM" in BEDMAS, going from left to right (if-else statement) and another for the "AS" in BEDMAS, going from left to right (if-else statement)        
        
        for i, item in enumerate(all_list):
            if ((all_list[i] == '/') and (not div_bool and not mult_bool)):
                all_list[i] = all_list[i-1]/all_list[i+1]
                del all_list[i-1]
                del all_list[i] # remove i because list gets smaller by 1 when you reduce an element
                counter+=1
                div_bool = True
                print(all_list)
    
            elif ((all_list[i] == '*') and (not mult_bool and not div_bool)):
                all_list[i] = all_list[i-1]*all_list[i+1]
                del all_list[i-1]
                del all_list[i] # remove i because list gets smaller by 1 when you reduce an element
                counter+=1
                mult_bool = True   
                print(all_list)        
            
        if (not div_bool and not mult_bool):    
            for i, item in enumerate(all_list):
                if ((all_list[i] == '+') and (not add_bool and not sub_bool)):
                    all_list[i] = all_list[i-1]+all_list[i+1]
                    del all_list[i-1]
                    del all_list[i] # remove i because list gets smaller by 1 when you reduce an element
                    counter+=1
                    add_bool = True
                    print(all_list)     

                elif ((all_list[i] == '-') and (not sub_bool and not add_bool)): # need elif instead of else, to make sure only one operation happens at a time (- or +, not multiple at once)
                    all_list[i] = all_list[i-1]-all_list[i+1]
                    del all_list[i-1]
                    del all_list[i] # remove i because list gets smaller by 1 when you reduce an element
                    counter+=1
                    sub_bool = True 
                    print(all_list) 
    
        num_items = len(all_list)        
                    
    return all_list                   
    

def inspect_string(input_str):
    list_of_num = {}
    # for 2 separate lists FIXME  dict_of_symbols = {}
    num_string = ""
    old_char = ''
    # for 2 separate lists FIXME counter = 0 
    counter1 = 1 
    i=0

    for char in input_str:
        if char != ' ':
            # for 2 separate lists FIXME counter+=1
            if (char == '+' or char == '-' or char == '*' or char == '/'):
                 # for 2 separate lists FIXME dict_of_symbols[counter] = char
                list_of_num[counter1] = char
                counter1+=2
                old_char = char
            else:
                if (old_char == '+' or old_char == '-' or old_char == '*' or old_char == '/'):
                    num_string=""
                    i+=2
                num_string = num_string + char
                old_char = char
            
                list_of_num[i] = int(num_string)
                
        #print(list_of_num)
        
    return list_of_num
        
        # for 2 separate lists FIXME print(dict_of_symbols)
        
def main():
    print("Note: a basic math statement only includes +, -, /, and *, without brackets.\n")
    math_str = input("Please input any basic math statement (see above) with natural numbers to be calculated, in the INFIX (e.g. 40*30-20) notation: \n")
    test_str = inspect_string(math_str)
    math_var = do_math(test_str)
    print(math_var) #there will always be ONE number as the final result in math_var
    print("===========================================================================================".center(center_amnt()))
    print("||                                                                                       ||".center(center_amnt()))
    print("||                                                                                       ||".center(center_amnt()))
    result_str ="YOUR RESULT: " + str(math_var[0])
    print(result_str.center(center_amnt()))                         
    print("||                                                                                       ||".center(center_amnt()))
    print("||                                                                                       ||".center(center_amnt()))
    print("===========================================================================================".center(center_amnt()))       
        
if __name__ == "__main__":
    main()
    
    
    