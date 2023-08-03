original_list = [0,2,4,6,8,10,16,20,30,35,37,50,100,105,120,130,150,200,300,340,400,500] # a random ascending list
original_index = 0 # it will be the index of the input in the list
                   # if input is not in the list, then it will the index of element smaller than input

print('This code will return the "original list" with elements smaller than your input and also your input if it was in the list')

while True:
    try:
        inpt = int(input('Enter a positive number: '))
        break
    except:
        print('Please type an integer')

def search(list, original_index):

    index = len(list)//2 # the index of middle element
    
    try: 
        variable = list[index] # middle element
    except:
        return original_list

    if variable > inpt: # checks if middle element is bigger than input

        before_variable = list[index-1] # element coming before middle element

        if before_variable < inpt: # checks if before_variable is smaller than input
            original_index += index # if it is, then input is between before_variable and variable
            return original_list[0:original_index] # and it returns list of all elements until before_variable
        else:
            return search(list[0:len(list)//2],original_index)  # recursion -> will search in list[0:len(list)//2]
# list[0:len(list)//2] is the list of elements smaller than middle element (variable) and the element before middle element (before_variable)

    elif variable < inpt:  # checks if middle element is smaller than input

        original_index += (index+1) 

        try: 
            after_variable = list[index+1] # element bigger than middle element
        except: # if there is no element bigger than middle element, it means that middle element was the last element in the list ->
#                 -> input is bigger than all elements in the original list
            return original_list

        if after_variable >= inpt:  # checks if after_variable is bigger than input -> input is between middle element and after_variable
                                    # check if after_variable is equal to input
            return original_list[0:original_index+1]
        else:
            return search(list[(len(list)//2)+1::],original_index) # recursion -> will search in list[(len(list)//2)+1::]
# list[(len(list)//2)+1::] is the list of elements bigger than middle element (variable) and the element after middle element (after_variable)
        
    else: # if middle element is equal to input
        original_index += index
        return original_list[0:original_index+1] # returns list of elemends from the first element to a middle element (or input) (included)

result = search(original_list, original_index)
if inpt not in original_list and inpt < result[-1]:
    print(result[:-1])
else:
    print(result)