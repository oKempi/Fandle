Version = 0.3
import os

def write_list(list:list, fileVariable, spaces:bool):
    if spaces == True:
        list = " ".join(list)
        fileVariable.writelines(list)
    else:
        fileVariable.writelines(list)

def write_tuple(tuple:tuple, fileVariable, spaces:bool):
    if spaces == True:
        tuple = " ".join(tuple)
        fileVariable.writelines(tuple)
    else:
        fileVariable.writelines(tuple)

def write_set(set:set, fileVariable, spaces:bool):
    if spaces == True:
        set = " ".join(set)
        fileVariable.writelines(set)
    else:
        fileVariable.writelines(set)

def sort(constant):
    constant.sort()

#def findIn_dict(dict, keyword):
#    def keyw(e):
#        return e[keyword]
#    dict.sort(key = keyw)

def check_write(data: str | int | float | set | range | tuple | list):
    try:
        open("testFandle.txt", "a").writelines(data)
    except:
        print("The data you have entered can not be writen... There is something wrong")
    else: 
        os.remove("testFandle.txt")
        print("Test was successful! This data can be written into a file")

def CauseOfcheck_write(data: str | int | float | set | range | tuple | list):
    try:
        f = open("testFandle.txt", "a")
        try: 
            f.writelines(data)
        except:
            print("Something went wrong when trying to write your argument into the file...")
    except: 
        print("Something went wrong when trying to open the file...")
    else:
        os.remove("testFandle.txt")
        print("Success! There is nothing wrong...")

def write_eachLine(data: set | tuple | list | dict, fileVariable, space: bool):
    if space == True:
        for x in data:
            file = fileVariable
            file.writelines("\n")
            file.writelines(x)
            file.writelines("\n")
    else:
        for x in data:
            file = fileVariable
            file.writelines(x)
            file.writelines("\n")

def delete(fileVariable):
    os.remove(fileVariable)