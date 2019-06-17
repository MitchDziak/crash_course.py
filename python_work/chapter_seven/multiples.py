number = input("I can tell you if a number is a multiple of ten: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of ten.")
else:
    print(str(number) + " is not a multiple of ten.")
