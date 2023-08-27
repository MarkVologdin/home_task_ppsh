from functools import reduce
# definition lambda function
#var = lambda x: x + 2

# definition filter function with lambda
#s = ['cat', 'dog', 'capybara']
#f1 = filter(lambda x: 'o' in x, s) # with list() will get list with this filter

def task_2():
    print(list(map(lambda x: x**3, list(map(int, input().split())))))


def task_3():
    print(list(filter(lambda x: x < 0, list(map(int, input().split())))))

def task_factorial_number():
    n = int(input())
    l = [x for x in range(1,n)]
    print(reduce(lambda x,y: x*y, l))
def task_6():
    array = [2, 4, 6, 8, 0, 3, 4, 2, 3, 5, 1, 2]
    a = lambda x: x % 3 == 0
    func1 = lambda x, y: x if x > y else y
    max1 = -10
    for i in range(len(array)):
        if a(array[i]):
            max1 = func1(max1 , array[i])
    print(max1)

    # from functools import reduce
    # array = [2, 4, 6, 8, 0, 3, 4, 2, 3, 5, 1, 2]
    # s1 = list(filter(lambda k: (k ** 2) % 9 == 0, array))
    # s2 = reduce(lambda a, b: a if a > b else b, s1)
    # print(s2)
    # ^ clean solution


if __name__ == '__main__':
    task_6()