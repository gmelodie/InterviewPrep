def urlify(string, length):
    copy = ''

    for char in string:
        url_char = char
        if char == ' ':
            url_char = '%20'
        copy += url_char

    return copy


string, length = input().split(',')
string = string.strip(' "')
length = int(length)

print(f"'{string}' {length}")

urlified = urlify(string, length)

print(f'"{urlified}"')

