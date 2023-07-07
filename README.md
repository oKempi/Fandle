# Fandle
File handling library for python

## Commands: 
### **print(Fandle.Version)** 

- prints out the current version of the library

### **write_list** (arguments: list, file (variable that opens the file), spaces (True/False)

- If you specify that: "*spaces* == **True**" the command writes the list with spaces

- Takes your pre-defined arguemts and uses them to write them into a file

### **write_tuple** (arguments: tuple, file (variable that opens the file), spaces(True/False)

- If you specify that: "*spaces* == **True**" the command writes the tuple with spaces

- Takes your pre-defined arguments and uses them to write them into a file

### **write_set** (arguments: set, file (variable that opens the file), spaces(True/False)

- If you specify that: "*spaces* == **True**" the command writes the set with spaces

- Takes your pre-defined arguments and uses them to write them into a file

### **sort** (arguments: constant)

- (You can use list with dicts in it)

### **findIn_dict** (arguments: dict/list (of dicts), keyword)

- Finds value in the **dict/list of dicts** using the set **keyword**

### **check_write** (arguments: data (It can be: str, int, float, range, set, tuple, list))

- Checks if you can write something into any file (right now it only checks in .txt file)

### **CauseOfcheck_write** (arguments: data (It can be: str, int, set, tuple, list))

- Checks if you can write the argument into any file (right now it only checks in .txt file)

- Gives an error at the part that did not work

### **write_eachLine** (arguments: data (It can be: list, set, tuple, dict), file (variable that opens the file), space(True/False))

- Takes your pre-defined argument and uses it to write each part on one line

- If you specify that: "*space* == **True**" the command writes it with space beforehand

### **delete** (arguments: file (variable that opens the file))

- Deletes the file you chose