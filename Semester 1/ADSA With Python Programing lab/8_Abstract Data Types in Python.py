def perform_actions_on_list(my_list):
    print("List:", my_list)
    print("Inserting data to list...")
    my_list.append(6)
    print("List after insertion:", my_list)
    
    print("Accessing data from list:")
    for item in my_list:
        print(item)

    print("Updating data in list...")
    if len(my_list) > 2:
        my_list[2] = 9
    print("List after updating:", my_list)

    print("Removing data from list...")
    if 4 in my_list:
        my_list.remove(4)
    print("List after removal:", my_list)


def perform_actions_on_set(my_set):
    print("Set:", my_set)
    print("Inserting data to set...")
    my_set.add(6)
    print("Set after insertion:", my_set)
    
    print("Accessing data from set:")
    for item in my_set:
        print(item)

    print("Removing data from set...")
    if 4 in my_set:
        my_set.remove(4)
    print("Set after removal:", my_set)


def perform_actions_on_dictionary(my_dict):
    print("Dictionary:", my_dict)
    print("Inserting data to dictionary...")
    my_dict['c'] = 3
    print("Dictionary after insertion:", my_dict)

    print("Accessing data from dictionary:")
    for key, value in my_dict.items():
        print(f"{key}: {value}")

    print("Updating data in dictionary...")
    if 'b' in my_dict:
        my_dict['b'] = 5
    print("Dictionary after updating:", my_dict)

    print("Removing data from dictionary...")
    if 'a' in my_dict:
        del my_dict['a']
    print("Dictionary after removal:", my_dict)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    my_set = {1, 2, 3, 4, 5}
    my_dict = {'a': 1, 'b': 2}

    perform_actions_on_list(my_list)
    print("--------------------------------------------")
    perform_actions_on_set(my_set)
    print("--------------------------------------------")
    perform_actions_on_dictionary(my_dict)
    print("--------------------------------------------")
