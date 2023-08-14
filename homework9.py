def search_devide(n):
    array_with_devide = []
    for i in range(1, n):
        if n % i == 0:
            array_with_devide.append(i)
    return sum(array_with_devide)

def search_friendly_numders():
    n = int(input())
    for x in range(n):
        for y in range(x, n):
            if x != y:
                if search_devide(x) == y and search_devide(y) == x:
                    print(x, y)

def search_numbers_Armstrong():
    n = int(input())
    for x in range(10**(n-1), 10**n):
        a = [int(i)**n for i in str(x)]
        #print(a, x, str(x).split())
        if sum(a) == x:
            print(x)

if __name__ == '__main__':
    search_numbers_Armstrong()
