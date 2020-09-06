def get_sum(a, b, delimiter='&'):
    return f"{str(a)}{delimiter}{str(b)}"


print(get_sum('Learn', 'python'))
print(get_sum('Learn', 'python').upper())
