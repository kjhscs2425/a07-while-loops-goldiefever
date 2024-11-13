# write a factorial function, given n, you return n!

def factorial(n):
    result = n
    number=1

    while number<=(n-1):
        result = result * (n-number)
        number += 1
    return result

print(factorial(5))
