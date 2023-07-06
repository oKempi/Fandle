#Version 0.1

def write_list(list, fileVariable, spaces):
    if spaces == True:
        list = " ".join(list)
        fileVariable.writelines(list)
    else:
        fileVariable.writelines(list)

def write_tuple(tuple, fileVariable, spaces):
    if spaces == True:
        tuple = " ".join(tuple)
        fileVariable.writelines(tuple)
    else:
        fileVariable.writelines(tuple)

def write_set(set, fileVariable, spaces):
    if spaces == True:
        set = " ".join(set)
        fileVariable.writelines(set)
    else:
        fileVariable.writelines(set)