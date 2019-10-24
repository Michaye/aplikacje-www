def my_function(a_list, b_list):
    return_list = []
    for x in range(0, len(a_list)):
        if x % 2:
            return_list.append(a_list[x])
    for x in range(0, len(b_list)):
        if not x % 2:
            return_list.append(b_list[x])
    return return_list


a_list = [x for x in range(1, 16)]
b_list = [x for x in range(23, 39)]
print(my_function(a_list, b_list))
