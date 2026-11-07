from typing import List

def read_integers() -> List[int]:
    user_input = input()
    int_list = user_input.split(",")
    new_list = []
    for num in int_list:
        new_list.append(int(num))
    return int_list

    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
