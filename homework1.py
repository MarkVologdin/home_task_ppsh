def first_task():
    word_1 = input()
    word_2 = input()
    word_3 = input()
    print(word_1 + word_2 + word_3)


def second_task():
    a = int(input())
    b = int(input())

    result = 2 ** 8 * a ** 8 - 2 ** 4 * a * 4 + 2 ** 2 * a ** 2 - 2 * b + 0.5 * b ** 0.5 + a * b ** (b + a) / 2
    print(result)


def third_task():
    a = input()
    b = input()
    print(a + b, end='!')


def sixth_task():
    count_santimetr = int(input())
    print(count_santimetr // 100000)

def standart_input():
    a = list(map(int, input().split())) # input numbers entered through space
    print(a)

if __name__ == '__main__':
    standart_input()
