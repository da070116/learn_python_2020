a = 2
b = 0.5
print(f"{a + b = }")

name = "  AlExAnDer  "
print(f"Hello, {name.lower().strip().capitalize()}!")  # name.capitalize().strip() returns "alexander"

v = input("Enter any digit from 1 to 10: ")
print(f"Return 10 + v that is equal to {10 + int(v) }")
input_name = input('Enter your name: ')
print(f'Hello, {input_name}')

# type conversion
try:
    for item in [float('1'), int(2.5), bool(1), bool(''), bool(0)]:   # int('2.5') returns a value error
        print(f"{item}")
except ValueError:
    print('Got value error ')
