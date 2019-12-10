int_code = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,6,23,27,1,5,27,31,1,10,31,35,2,10,35,39,1,39,5,43,2,43,6,47,2,9,47,51,1,51,5,55,1,5,55,59,2,10,59,63,1,5,63,67,1,67,10,71,2,6,71,75,2,6,75,79,1,5,79,83,2,6,83,87,2,13,87,91,1,91,6,95,2,13,95,99,1,99,5,103,2,103,10,107,1,9,107,111,1,111,6,115,1,115,2,119,1,119,10,0,99,2,14,0,0]

def optcode_reader(code_list):
    
    
    for x in range(0, len(code_list), 4):
        new_list = code_list
        new_position = code_list[x + 3]
        pos1 = code_list[x + 1]
        pos2 = code_list[x + 2]
        if code_list[x] == 99:
            print("breaking..")
            break
        if code_list[x] == 1:
            new_list[new_position] = code_list[pos1] + code_list[pos2]
            print("hi")
        elif code_list[x] == 2:
            new_list[new_position] = code_list[pos1] * code_list[pos2]
        
            
    return new_list
                
            
            
            
            




print(optcode_reader(int_code))

