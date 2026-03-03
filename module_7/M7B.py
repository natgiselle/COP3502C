# Data Parsing

def parse_student(student_data):
    student = {}

    student['id'] = int(student_data[0:8])
    student['name'] = student_data[8:-4]
    student["birthdate"] = student_data[-4:-2] + "/" + student_data[-2:]
    return student

student_data = "12345678Will Albright0116"


# List Counting
def count_items(items_list):
    items_count_dict = {}

    for item in items_list:
        if item not in items_count_dict: # removes duplication
            items_count_dict[item] = items_list.count(item) # [item] is the key, item_list.count(item) is the value

    return items_count_dict

# print(count_items(["a", "b", "c", "a", "aa", "c", "hello"]))


# List Fighters
def list_fighters(battle_data):
    battle_data_set = set()
    for key in battle_data:
        battle_data_set.add(key)
        battle_data_set.update(battle_data[key].get("loss"))
        battle_data_set.update(battle_data[key].get("win"))

    battle_data_list = list(battle_data_set)
    battle_data_list.sort()
    return battle_data_list
