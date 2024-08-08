# https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
def mutate_string(string, position, character):
    string_length = len(string)
    string_list = []
    for index in range(position):
        string_list.append(string[index])
    string_list.append(character)
    for remaining_index in range((position+1), string_length):
        string_list.append(string[remaining_index])
    altered_string = "".join(string_list)
    return altered_string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
