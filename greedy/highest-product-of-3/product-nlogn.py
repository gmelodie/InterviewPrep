# O(nlogn)
#
def highest_product_three(list_of_ints):
    list_of_ints = sorted(list_of_ints)

    positive = list_of_ints[-1]*list_of_ints[-2]*list_of_ints[-3]
    negative = list_of_ints[0]*list_of_ints[1]*list_of_ints[-1]

    return max(positive, negative)


if __name__ == '__main__':
    list_of_ints = [int(a) for a in input().split()]
    print(highest_product_three(list_of_ints))
