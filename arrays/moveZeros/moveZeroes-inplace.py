# O(n) time
# O(n) space

def move_zeros(lst):
    zeros = 0

    for i in range(len(lst)):
        j = i - zeros
        if lst[j] == 0:
            lst.append(lst.pop(j))
            zeros += 1

    return lst


if __name__ == '__main__':
    lst = [int(a) for a in input().split()]
    print(move_zeros(lst))
