# We can do the permutation be O(n) using hash tables
#

def populate_dict(string):
    chars_dict = {}

    for char in string:
        if char not in chars_dict:
            chars_dict[char] = 0
        chars_dict[char] += 1

    return chars_dict


def check_permutation(string_1, string_2):
    if len(string_1) != len(string_2):
        return False

    chars_string_1 = populate_dict(string_1)
    chars_string_2 = populate_dict(string_2)

    for char, amount in chars_string_1.items():
        if char not in chars_string_2:
            return False
        if chars_string_2[char] != amount:
            return False

    return True


if __name__ == '__main__':
    string_1 = input()
    string_2 = input()
    print(check_permutation(string_1, string_2))
