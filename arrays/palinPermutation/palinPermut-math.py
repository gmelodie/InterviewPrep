
def get_chars_dir(string):
    characters = {}

    for char in string:
        if char not in characters:
            characters[char] = 0
        characters[char] += 1

    return characters


def is_palindrome_permutation(characters):
    one_odd = False
    for char, quantity in characters.items():
        if is_odd(quantity):
            if one_odd:
                return False
            one_odd = True
    return True


def is_odd(number):
    if number % 2 == 0:
        return False
    return True

if __name__ == '__main__':
    string = input()
    characters = get_chars_dir(string)
    print(is_palindrome_permutation(characters))


