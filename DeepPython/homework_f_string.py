age = 29
name = 'Mark'
surname = 'Vologdin'

s = f'My name is {name} {surname} and i am {age} years old.'
# refactor {x:,.08b}

def task_1():
    name = ['Александру','Алексу','Алберту']
    surname = ['Вотяку','Вотякову','Вотяковичу']
    last_name = 'Романовичу'
    for x in name:
        for y in surname:
            print(f'Диплом с отличием вручается {y} {x} {last_name}')

def task_2(): # generator car's number
    name = input()
    first_number = int(input())
    second_numbber = int(input())
    print(f'{name}{first_number:04}-{second_numbber:03}')


def task_3():
    first_number = int(input())
    second_number = int(input())
    print(f'{first_number:>10}')
    print(f'{second_number:>10}')
    print(f'{first_number + second_number:>10}')


def task_4():
    deposit = 100000000
    r = int(input())
    k = int(input())
    sum = deposit * (( 100 + r )/100) ** k
    print(f'{sum:,.2f}')

def task_5():
    for a in range(1,101):
        for b in range(1,101):
            print(f'[DEBUG] {a=} {b=} result={a*b}')


def task_6():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    result = []
    for template in ["{:08b}", "{:b}", "{:o}", "{}", "{:x}"]:
        result.append(".".join([template] * 4).format(a, b, c, d))
    print( "\n".join(result))

if __name__ == '__main__':
    task_6()
