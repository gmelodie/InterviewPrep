def has_all_unique(string):
    seen = {}
    for char in string:
        if char in seen:
            return False
        seen[char] = True
    return True


if __name__ == '__main__':
    string = input()
    print(has_all_unique(string))
