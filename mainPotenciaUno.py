#definir funcion
def a_power_b (a,b):
    prod=1
    for x in range (0,b):
        prod=prod*a
        return prod

#codigo

base=int(input("ingrese la base"))
exponente=int(input("ingrese el exponente"))

result=a_power_b(base,exponente)

print("el resultado de su potencia es: ",result)
