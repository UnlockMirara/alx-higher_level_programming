#!/usr/bin/python3
# 11-delete_at.py



def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  # If idx is out of range or negative, return the same list

    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])

    return new_list

# Test the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)
