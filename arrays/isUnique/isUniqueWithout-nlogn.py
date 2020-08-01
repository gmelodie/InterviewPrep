def has_all_unique(string):
    # Sorting the string first makes it O(nlogn)
    string = sorted(string)
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return False
    return True


if __name__ == '__main__':
    string = input()
    print(has_all_unique(string))
