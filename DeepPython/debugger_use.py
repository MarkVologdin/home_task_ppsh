def multiplylist(lst):
    if len(lst) == 0:
        return None
    else:
        result = 1
        for i in range(len(lst)):
            result = result * lst[i]
        return result

if __name__ == '__main__':
    print(multiplylist([1, 2, 3, 4, 5, 6]))