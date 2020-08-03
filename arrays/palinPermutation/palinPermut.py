def _gen_perms(string, prefix):
    perms = []

    if len(string) == 0:
        return [prefix]

    for i, char in enumerate(string):
        new_prefix = list(prefix)
        new_prefix.append(char)

        new_string = list(string)
        new_string.pop(i)

        local_perms = _gen_perms(new_string, new_prefix)
        for perm in local_perms:
            perms.append(perm)

    return perms


def gen_perms(string):
    return _gen_perms(list(string), [])


def is_palindrome(string):
    for i in range(len(string)//2+1):
        print(string[i], string[len(string)-1-i])
        if string[i] != string[len(string)-1-i]:
            return False
    return True



def main():
    string = input()

    permutations = gen_perms(string)
    for perm in permutations:
        print(perm)
        if is_palindrome(perm):
            print(True)
            return

    print(False)


if __name__ == '__main__':
    main()
