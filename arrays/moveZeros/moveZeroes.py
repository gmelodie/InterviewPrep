# O(n) time
# O(2n) space

def move_zeros(lst):
    final_lst = []
    zeroes = 0

    for i in range(len(lst)):
        if lst[i] == 0:
            zeroes += 1
        else:
            final_lst.append(lst[i])

    for i in range(zeroes):
        final_lst.append(0)

    return final_lst

if __name__ == '__main__':
    lst = [int(a) for a in input().split()]
    print(move_zeros(lst))
