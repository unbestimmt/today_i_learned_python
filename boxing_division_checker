print(" Boxing division's checker ".center(40, "-"))
print(" ")
while True:
    try:
        name = input("Type the fighter's name: ")
        weight = float(input("Type the fighter's weight in kilograms: "))
        division = ""
        if weight<=47.7:
            division = "Minimumweight"
        elif 47.7<weight<49.1:
            division = "Junior Flyweight"
        elif 49.1<weight<=50.8:
            division = "Flyweight"
        elif 50.8<weight<=52.16:
            division = "Super Flyweight"
        elif 52.16<weight<=53.52:
            division = "Bantamweight"
        elif 53.52<weight<=55.34:
            division = "Super Bantamweight"
        elif 55.34<weight<=57.15:
            division = "Featherweight"
        elif 57.15<weight<=58.97:
            division = "Super Featherweight"
        elif 58.97<weight<=61.23:
            division = "Lightweight"
        elif 61.23<weight<=63.5:
            division = "Super Lightweight"
        elif 63.5<weight<=66.68:
            division = "Welterweight"
        elif 66.68<weight<=69.85:
            division = "Super Welterweight"
        elif 69.85<weight<=72.57:
            division = "Middleweight"
        elif 72.57<weight<=76.2:
            division = "Super Middleweight"
        elif 76.2<weight<=79.38:
            division = "Light Heavyweight"
        elif 79.38<weight<=90.72:
            division = "Cruiserweight"
        elif weight>90.72:
            division = "Heavyweight"
        print(" ")
        print("Name: ", name)
        print("Weight: ", weight)
        print("The fighter {}, weighing {} kg, fights in the {} division.".format(name, weight, division))
    except:
        print("Invalid input")
    finally:
        x = input("\nDo you wanna type another fighter's info? (y/n) ")
        print(" ")
        if x=="n" or x=="N":
            break
print(" ")
print("-"*40)
