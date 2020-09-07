def get_sum(a, b, delimiter='&'):
    return f"{str(a)}{delimiter}{str(b)}"


def discount(price, percent_discount):
    try:
        price = abs(round(float(price)))
        percent_discount = float(percent_discount)
        if 0 < percent_discount < 100:
            return price - (price * percent_discount / 100)
        else:
            return price
    except ValueError:
        return "Error: can't convert value to a float"


if __name__ == '__main__':
    print(get_sum('Learn', 'python'))
    print(get_sum('Learn', 'python').upper())
    print(discount("545", 23))
    print(discount(545, "7"))
    print(discount("9i8", "er"))
    print(discount("7698", "34"))
