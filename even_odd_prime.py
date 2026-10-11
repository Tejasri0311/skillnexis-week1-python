
def check_even_odd(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")


def check_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

check_even_odd(num)

if check_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")
