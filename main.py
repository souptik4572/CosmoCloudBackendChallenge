from pprint import pprint

list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
    {"id": "4", "marks": 60}
]

def display_list(complete_list):
    for item in complete_list:
        pprint(item)

def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.

    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    # Time Complexity: O(n + m * k) where n is the number of elements in list_1 and m is the number of elements in list_2 and k is the number of keys in each item of list_2
    # Space Complexity: O(n) where n is the number of elements in list_1
    merged_list = list()
    indexing = dict()
    for item in list_1:
        indexing[item.get("id")] = len(merged_list)
        merged_list.append(item)
    for item in list_2:
        index = indexing.get(item.get("id"))
        if index == None:
            merged_list.append(item)
            continue
        merged_list[index].update(item)
    return merged_list

list_3 = merge_lists(list_1, list_2)
display_list(list_3)