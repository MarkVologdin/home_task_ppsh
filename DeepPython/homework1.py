import copy
import sys


def task_two():
    l = [int(i) for i in input().split()]  # ввод через одну строку
    print(l)
    a1 = l[:]
    print(a1)

    a2 = l.copy()
    print(a1)

    a3 = copy.copy(l)
    print(a3)

    a4 = copy.deepcopy(l)
    print(a4)

    a5 = list(l)
    print(a5)
    print(sum(a5))


def task_4():
    animal = ['cat', 'dog', 'dog', 'cat', 'bird', 'capybara', 'capybara', 'capybara']
    type_animal = set(animal)
    dict_animal = {}
    for i in type_animal:
        dict_animal[i] = 0
    for i in animal:
        dict_animal[i] += 1
    s1 = 0  # count reference on number count of animal
    s2 = 0  # count reference on string of type animal
    for i in dict_animal:
        s1 += sys.getrefcount(dict_animal[i])
        s2 += sys.getrefcount(i)
    print(s1, s2, sep='\n')


def task_5():  # difference a pair of object
    animals = ["capybara", "capybara", "capyba", "capyba", "capybara",
               2999, 2999, "capybara", [7, 7, 7], [7, 7, 7], [7, 7, 7],
               [7, 7, 7]] + [[8, 8]] * 5
    summa1 = 0
    summa2 = 0
    count_of_pair_reference = 0
    for i in range(len(animals)):
        for j in range(i + 1, len(animals)):
            summa1 += (animals[i] is animals[j]) * 1
            summa2 += (animals[i] == animals[j]) * 1
    print('count_of_pair_object=', summa1)
    print('count_of_pair_reference=', summa2)


def task_6():
    recursive_salad = ['lettuce', 'chicken', 'cheese', 'souce', 'tomatoes', 'croutons']
    recursive_salad.append(recursive_salad)
    recursive_salad[6].append('solt')
    recursive_salad[6].append('pepper')
    print(recursive_salad)
    print(recursive_salad[4])
    print(recursive_salad[-1])


if __name__ == '__main__':
    task_6()
