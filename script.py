
# count the number of digits in a number
def count_dig(n):
    dig = 0
    while n != 0:
        n = n // 10
        dig += 1
    return dig

# multiply two n-bit numbers using Karatsuba Algorithm
def multiply(n1, n2):
    base = 10
    n_dig = count_dig(n1)

    if n_dig == 1:
        return n1 * n2

    divisor = 10 ** (n_dig // 2)

    n1_left = n1 // divisor
    n1_right = n1 % divisor
    n2_left = n2 // divisor
    n2_right = n2 % divisor

    a = multiply(n1_left, n2_left)
    d = multiply(n1_right, n2_right)
    e = (n1_left + n1_right) * (n2_left + n2_right) - a - d
    return a*base**n_dig + e*base**(n_dig//2)+d

print(multiply(1234, 4321), 1234 * 4321)

