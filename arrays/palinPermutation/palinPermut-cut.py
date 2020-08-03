# This solution stops immediately after it finds the palindrome
# This doesn't make the *time* complexity better
# But it does make the *space* complexity better
#
def _is_palin_permut(string, prefix):
    perms = []

    if len(string) == 0:
        return is_palindrome(prefix)

    for i, char in enumerate(string):
        new_prefix = list(prefix)
        new_prefix.append(char)

        new_string = list(string)
        new_string.pop(i)

        if _is_palin_permut(new_string, new_prefix):
            return True

    return False


def is_palindrome_permutation(string):
    return _is_palin_permut(list(string), [])


def is_palindrome(string):
    for i in range(len(string)//2+1):
        print(string[i], string[len(string)-1-i])
        if string[i] != string[len(string)-1-i]:
            return False
    return True


if __name__ == '__main__':
    string = input()
    print(is_palindrome_permutation(string))
