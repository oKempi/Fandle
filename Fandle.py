#Version 0.2

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

def sort(constant):
    constant.sort()

def findIn_dict(dict, keyword):
    def keyw(e):
        return e[keyword]
    dict.sort(key = keyw)