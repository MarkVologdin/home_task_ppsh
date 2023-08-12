def task_1():
    x = int(input())
    while ( x % 2 != 0) and ( x % 10 != 5):
        x = int(input())


def task_3():
    k = int(input())
    n = int(input())
    sum = 0
    while k < n:
        if k % 2 == 1:
            sum +=k
        k +=1
    print(sum)
# 768125652


def factorial():
    x = int(input())
    fact = 1
    for i in range(1,x+1):
        fact *= i

    return fact
 #3628800
if __name__ == '__main__':
    print(factorial())
