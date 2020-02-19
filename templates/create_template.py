"""create jinja template for sublevel 2 ~ 6"""
#!/usr/bin/python

temp = [] 
with open("./h1.jinja2", 'r') as file:
    for i, line in enumerate(file):
        if i >= 3:
            temp.append(line)
temp = temp[:-1]

temp_str = "".join(temp)

for level_num in range(2, 7):
    temp_str_new = temp_str
    replace_dict = {}
    replace_dict["h2"] = "h"+str(level_num+1)
    replace_dict["h1"] = "h"+str(level_num)
    replace_dict["_2"] = "_"+str(level_num+1)
    replace_dict["_1"] = "_"+str(level_num)
    for target in replace_dict:
        temp_str_new = temp_str_new.replace(target, replace_dict[target])
    file_name = "h" + str(level_num) + ".jinja2"
    with open(file_name, "w") as file:
        file.write(temp_str_new)
