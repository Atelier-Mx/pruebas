print("Prueba de Print")
print(0o105)
print(0x045)
print("Me gusta \"Monty Python\"")
print('Me encanta "estudiar"')
print("I\'m Monty Python.")
print('I"'"m Monty Python."'')
print(True > False)
print(True < False)
print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")
print("En aplicaciones de resta, el operador de resta espera dos argumentos: el izquierdo un minuendo en términos aritméticos y el derecho (un sustraendo).")
print (2 + 3 * 5)
##
john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=',')

total_apples = john + mary + adam
print("total=", total_apples)
##

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

##

var = "007"
print("Agent " + var)

# Este programa evalúa la hipotenusa c.
# a y b son las longitudes de los cátetos.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # Se emplea ** en lugar de una raíz cuadrada.
print("c =", c)

print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")


anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)


fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")





