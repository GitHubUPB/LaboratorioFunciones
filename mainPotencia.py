#definir funcion
def a_power_b (a,b):
    prod=1
    for x in range (1,b+1):
        if x>=1000:
            raise StopIteration("Pailas")
        
        prod=prod*a
    return prod


#codigo

while True:
    
    try:
        base=int(input("ingrese la base"))
        if base ==0:
            print("numero es cero ####")
            break
        exponente=int(input("ingrese el exponente"))
    except ValueError:
        print("ingreso una letra")
    except StopIteration:
        print("sobrepaso el limite")

    
    

    
   
 






    
