def get_book_word_count(file_contents):
    return len(file_contents.split())

def get_character_count(file_contents):
    character_dict = {}
    for i in file_contents:
        lower_i = i.lower()
        if lower_i in character_dict:
            character_dict[lower_i] += 1
        else:
            character_dict[lower_i] = 1
    return character_dict

def sort_on(dict):
    return dict["count"]

def get_sorted_character_dicts(character_dict):
    dict_list = [{"char": i, "count": character_dict[i]} for i in character_dict]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
