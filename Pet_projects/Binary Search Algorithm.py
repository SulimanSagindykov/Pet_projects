original_list = [0,2,4,6,8,10,20,30,35,37,50,100,1000]
inpt = int(input('What is the number? : '))
original_index = 0

def search(original, list, original_index):
    index = len(list)//2
    try:
        variable = list[index]
    except:
        return original

    if variable > inpt:

        variable = list[index-1]

        if variable < inpt: 
            original_index += index
            return original[0:original_index]
        else:
            return search(original_list,list[0:len(list)//2],original_index)
        
    elif variable < inpt:

        try:
            variable = list[index+1]
        except:
            return original
        original_index += index

        if variable > inpt: 
            return original[0:original_index+1]
        else:
            return search(original_list, list[len(list)//2::],original_index)
        
    else:
        return original[0:original_index+1]
    
print(search(original_list,original_list,original_index))