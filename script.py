# count the number of digits in a number

# count the number of digits in a number
def count_dig(n):
    if n == 0:
        return 1
    dig = 0
    while n != 0:
        n = n // 10
        dig += 1
    return dig

# multiply two n-bit numbers using Karatsuba Algorithm
def multiply(n1, n2):
    base = 10
    n_dig = max(count_dig(n1), count_dig(n2))

    if n_dig == 1:
        return n1 * n2

    divisor = 10 ** (n_dig // 2)

    n1_left = n1 // divisor
    n1_right = n1 % divisor
    n2_left = n2 // divisor
    n2_right = n2 % divisor

    a = multiply(n1_left, n2_left)
    d = multiply(n1_right, n2_right)
    e = multiply(n1_left + n1_right, n2_left + n2_right) - a - d
    return a * divisor ** 2 + e * divisor + d

n1=3789814159265358979323846987264338327959870980902884197169399375105820974944592
n2 = 909827188182845904528768760935360287471352662497757247093699959574966967627

k=multiply(n1,n2)
r=n1*n2
print(r==k)
