print("Hourly Salary Calculator\n")
valor_hora = float(input("Type the hourly wage: $ "))
horas_normais = float(input("Type the amount of hours worked this month: "))
horas_extras = float(input("Type the amount of overtime worked this month: "))
hora_extra_taxa = float(input("How much are you paid by doing overtime compared to normal hours? "))
salario = valor_hora*horas_normais + valor_hora*hora_extra_taxa*horas_extras
print("\nYour salary this month will be $ {:.2f}.\n".format(salario))
print("--- End of program. ---")
