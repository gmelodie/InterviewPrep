# O(n)
#

def get_min_index(lst, minimal=True):
    mini = min(lst)
    if not minimal:
        mini = max(lst)

    for i, number in enumerate(lst):
        if number == mini:
            return i


def highest_product_three(list_of_ints):
    positive_ints = [0, 0, 0]
    negative_ints = [0, 0]

    for number in list_of_ints:
        if number > min(positive_ints):
            i = get_min_index(positive_ints)
            positive_ints[i] = number
        elif number < max(negative_ints):
            i = get_min_index(negative_ints, minimal=False)
            negative_ints[i] = number

    positive_product = positive_ints[0]*positive_ints[1]*positive_ints[2]
    negative_product = negative_ints[0]*negative_ints[1]*max(positive_ints)

    return max(positive_product, negative_product)


if __name__ == '__main__':
    list_of_ints = [int(a) for a in input().split()]
    print(highest_product_three(list_of_ints))
