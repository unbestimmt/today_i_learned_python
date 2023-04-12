print("Type a list of numbers and the checker will automatically \
calculate which ones are the highest and the lowest ones, \
the number of values, the sum and the average.\n\
If you type a negative number or zero, the list will stop.\n")
a = []
sum = 0
while True:
    n = int(input("Type a whole number: "))
    if n <= 0:
        break
    else:
        a.append(n)
        sum += n
average = sum / len(a)
print("\nThe lowest number is", min(a))
print("The highest number is", max(a))
print(f"The sum of {len(a)} numbers is {sum}")
print(f"The average of {len(a)} numbers is {average:.2f}")
