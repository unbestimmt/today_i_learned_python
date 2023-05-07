print("Finding multiples of 5 within a range of numbers\n")

min=int(input("Type the minimum value of the range: "))
max=int(input("Type the maximum value of the range: "))

if max<min:
    print("\nThe minimum value is higher than the maximum value. Let's switch them.\n")
    x = max
    max = min
    min = x
    print("Now, minimum is {} and maximum is {}.\n".format(min, max))

while min<=max:
    r = min%5
    if r == 0:
        print("{}, ".format(min), end="")
    min += 1
