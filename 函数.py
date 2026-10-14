def max_ab(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def min_ab(a, b):
    return abs(a * b) // max_ab(a, b)


def tri(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    a, b, c = sorted([a, b, c])
    return a + b > c


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_100():
    print("100以内的质数：")
    for i in range(2, 101):
        if is_prime(i):
            print(i)
    print()


num1 = int(input('a'))
num2 = int(input('b'))
print(f'最小公倍数：{min_ab(num1, num2)}')
x = int(input('请输入第1条边：'))
y = int(input('请输入第2条边：'))
z = int(input('请输入第3条边：'))
if tri(x, y, z):
    print('可以构成三角形')
else:
    print('不能构成三角形')
primes_100()