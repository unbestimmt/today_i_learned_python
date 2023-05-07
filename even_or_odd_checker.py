print(" Is it even or odd? ".center(30,"-"))
print(" ")
try:
    x=int(input("Type a number: "))
    r=x%2
    if r==0:
        print("{} is even.".format(x))
    else:
        print("{} is odd.".format(x))
except:
    print("input invalido")
print(" ")
print("-"*30)
