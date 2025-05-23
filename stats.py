def get_number_of_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_each_character_count(text: str) -> dict:
    character_dict = {}
    book_text_lower = text.lower()
    for character in book_text_lower:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(list_of_dicts: dict) -> int:
    return list_of_dicts["num"]

def get_sorted_dicts(character_dict: dict) -> list:
    dict_list = []
    for key, value in character_dict.items():
        current_dict = {"char": key, "num": value}
        dict_list.append(current_dict)
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list