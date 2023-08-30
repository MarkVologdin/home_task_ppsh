# f = open('input.txt', 'r')
# s = open('input.txt', 'r')
# one_string = f.readline()  # read one string from file
# one_big_string = s.read()  # read file and create one big string with all strings from file
# L1 = s.readlines()  # read all file and creacte list with string from file, different of split() make with '\n'
# L2 = one_big_string.split('\n')  # devides string on many strings for '\n'
#
# # for line in f:
# #     print(line) or print(line.rstrip(' \n '))
# # f.close() or f.seek()
# f = open('out1.txt','w') # a-append w-write r-read / r+ w+ a+
# s1 = 'hello world'
# f.write(s1)
# f.writelines(L2) # write list of strings in file
# # f.flush() # скидывается данные на диск
# f.close()
#
# # create space WITH
# with open('input.txt','r') as g, open('output.txt','w') as f:
#     for line in g:
#         print(line, file= f)
#

def read_all_file_in_one_string(filename):
    with open(filename, 'r+') as f:
        s = f.read()
    f.close()
    return s


def read_one_string(filename):
    with open(filename, 'r+') as f:
        s = f.readline()
    f.close()
    return s


def read_all_strings_in_list(filename):
    with open(filename, 'r+') as f:
        L1 = f.readlines()
    return L1


def read_all_strings_in_list_without_n(filename):
    with open(filename, 'r+') as f:
        s = f.read()
    list1 = s.split('\n')

    return list1


def read_file_on_strings(filename):
    with open(filename, 'r+') as f:
        for line in f:
            print(line.rstrip('\n')) # delete char \n in the end of string [line]



def read_file_and_return_one_big_string_through_space(filename):
    with open(filename, 'r+') as f:
        list1 = f.read().split('\n')
    return ' '.join(list1)

def processDictionary(name): # 14
    dictionary = {}
    with open(name, "r", encoding="utf-8") as f:
        data = f.readlines()
        for line in data:
            temp = line.split()
            dictionary[temp[0]] = (temp[1], temp[2])
    return dictionary


if __name__ == '__main__':
    print(read_file_and_return_one_big_string_through_space('input.txt'))
