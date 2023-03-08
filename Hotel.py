individual = 2500
doble = 4600
familiar= 5200

huspedes= int(input("cuantos huespedes son:"))
dia_estadia= int(input("cuantos dias se van a quedar:"))

if huspedes == 1:
    descuento = individual * 0.05
    iva = individual * 0.21
    tarifa = dia_estadia * individual 
    print ("el valor con el iva es:")
    print (iva)  
    print ("su valor sin el iva sera de: ")
    print (tarifa)
    print ("su descuento es:")
    print (descuento)
elif huspedes == 2:
    descuento = doble * 0.09
    iva = doble * 0.21
    tarifa = dia_estadia * doble
    print ("el valor con el iva es: ")
    print (iva)
    print ("su valor sin el iva sera de:")
    print (tarifa)
    print ("su descuento es:")
    print (descuento)
else:
    descuento = familiar * 0.15
    iva = familiar * 0.21
    tarifa = dia_estadia * familiar 
    print ("el valor con el iva es:")
    print (iva)
    print ("su sin el iva sera de: ")
    print (tarifa)
    print ("su descuento es:")
    print (descuento)
