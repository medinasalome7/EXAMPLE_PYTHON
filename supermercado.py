#elegir 5 productos que sumados de un valor de 50.000

lista_productos = ["carne","salchichon","huevos","papas","spaghettis"]
 
precios_productos = [
  "carne 15.000", 
  "salchichon 9.000",
  "huevos 13.000",
  "papas 7.000",
  "spaghettis 6.000" 
]
print(precios_productos)

#valor total de la compra
precio= [15.000, 9.000, 13.000, 7.000, 6.000]
resultados = precio[0] + precio[1] + precio[2] + precio[3] + precio [4]
print (resultados) 

#huevos cuentan con un descuento de 25%
descuento = (precio [2] *0.025) - precio [2]
print (descuento) 

#valor total despues del descuento
Nuevo_valor_total = (precio[2] *0.025) - precio [2]  
print (Nuevo_valor_total) 
