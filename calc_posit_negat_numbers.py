print("Calculating negative and positive whole numbers separately. \
\nTyping zero will stop adding new numbers and will give the results.\n")
positives=0
negatives=0
while True:
    n=int(input("Type a whole number (integer): "))
    if n==0:
        break
    elif n>0:
        positives+=n
    else:
        negatives+=n
print("\nThe sum of positive numbers typed is {}.".format(positives))
print("The sum of negative numbers typed is {}.".format(negatives))
