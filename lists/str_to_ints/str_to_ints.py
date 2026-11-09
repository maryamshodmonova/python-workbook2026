def str_to_ints(string: str):
    numbers = [] 
    for piece in string.split():
        numbers.append(int(piece))
    return numbers
if _name_== "_main_":
    print (str_to_ints(2))


    
