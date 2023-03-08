moneda_origen ="pesos colombianos"
valor_origen= 10000
moneda_destino="dolar"
dolar= "el valor del dolar es:"
valor_dolar= 4785.34
euro= "el valor del euro es:"
valor_euro= 5090
yen= "el valor del yen es:"
valor_yen = 35.18
bolivar= "el valor del bolivar es:"
valor_bolivar = 196.77
yuan= "el valor del yuan es:"
valor_yuan = 689.36
respuesta = input()

print ("ingresa tu nombre")
nombre= input ()

print('ingresa tu documento')
documento =  input ()

print('ingresa moneda de origen')
moneda_origen = input ()

print('ingresa moneda de destino')
moneda_destino = input()

if moneda_destino == "dolar":
 porcentaje = valor_dolar * 0.07 
 print (porcentaje)
elif moneda_destino =="euro":
  porcentaje = valor_euro * 0.10
  print(nombre, documento, moneda_origen, moneda_destino, valor_origen)
  print("desea hacer el intercambio")
  print("el valor de la intermediacion es mayor al 10%")
  respuesta = input(("desea continuar con la transaccion si/no: "))
  
if respuesta == "si":
  porcentaje = valor_dolar * 0.10
  print ("su porcentaje es:")
  print(porcentaje)

elif respuesta == "no":  
  print("no se aplica el incremento")
elif moneda_destino =="yen":
  porcentaje = valor_yen * 0.05 
  print (porcentaje)
elif moneda_destino =="bolivar":
  porcentaje = valor_bolivar * 0.03
  print (porcentaje)
elif moneda_destino =="yuan":
  porcentaje = valor_yuan * 0.01
  print (porcentaje)
else:
 print("error, no existe la moneda")