import decimal


def pi():
    decimal.getcontext().prec += 2
    three = decimal.Decimal(3)
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    return +s


def main():
    print("Welcome to the Pi shop. Here you can request to see as many digits as you like of Pi and we will return them to")
    num_of_digits = int(input("How many digits would you like to see?: "))
    decimal.getcontext().prec = num_of_digits
    print(f"Here are your {num_of_digits} digits of Pi!")
    print(pi())


main()
