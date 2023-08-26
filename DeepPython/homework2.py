def task_1():  # example of iterator
    a = [2, 4, 6, 8]
    b = {1, 3, 5, 7}
    a_itera = iter(a)
    b_iterb = iter(b)
    next(iter(a_itera))
    print(next(iter(a_itera)), next(iter(b_iterb)))
    next(iter(b_iterb))
    print(next(iter(b_iterb)), next(iter(a_itera)))

def task_3():
    d = {1: 'bee', 2: 'raccoon', 3: 'snake'}
    iterator = iter(d)
    print(d[next(iterator)])


def task_4():
    a = [int(s) for s in range(1, 20)]
    iterator = iter(a)
    print(9 in iterator)
    print(9 in iterator)

def task_6():
    a = (x ** 2 for x in range(1,6))
    k = iter(a)
    print(next(k))
    next(k)
    print(next(k))
    next(k)
    print(next(k))

def task_7():  # generator with iterator playing cards
    type_of_cards = ['Черви','Буби','Крести', 'Пики']
    type_of_seniority = ['Валет', 'Дама', 'Король', 'Туз']
    list_of_cards = [x for x in range(6,11)] + type_of_seniority
    cards_generator = (str(x)+ " " + y for x in list_of_cards for y in type_of_cards )
    for i in cards_generator:
        print(i)

if __name__ == '__main__':
    task_7()