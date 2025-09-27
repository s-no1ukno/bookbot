def get_word_count(text):
    return len(text.split())


def get_character_count(text):
    char_dict = {}

    for character in text:
        proc_char = character.lower()
        if proc_char in char_dict:
            char_dict[proc_char] += 1
        else:
            char_dict[proc_char] = 1

    return char_dict


def sort_character_dict(char_dict):
    def sort_on(items):
        return items["num"]

    char_list = []

    for item in char_dict:
        new_dict = {}
        if item.isalpha():
            new_dict["char"] = item
            new_dict["num"] = char_dict[item]
            char_list.append(new_dict)

    char_list.sort(reverse=True, key=sort_on)
    return char_list
