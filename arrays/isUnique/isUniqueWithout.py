def has_all_unique(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True


if __name__ == '__main__':
    string = input()
    print(has_all_unique(string))
