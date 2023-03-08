Articulos = ["Zapatos", "Tenis", "Camisetas", "Jeans"]
print (Articulos)

Precios_actuales = ["Zapato $350.000","Tenis $280.000","Camisetas $175.000","Jeans $200.000"]
print(Precios_actuales)


#Precio total de los articulos en venta 
precio= [350.000, 280.000, 175.000, 200.000]
resultados = precio[0] + precio[1] + precio[2] + precio[3]
print ("valor total de los articulos", resultados) 

#promedio de la venta 
precio= [350.000, 280.000, 175.000, 200.000]
resultado= (precio[0] + precio[1] + precio[2] + precio[3]) /4
print ("el promedio de las ventas", resultado) 

#Subir el precio de los Jeans 
resultado = (precio [3] *0.062) + precio [3]
print ("el precio de los jeans subio un", resultado) 

#Dsiminuir precio de los zapatos 
resultado = (precio [0] *0.008) - precio [0]
print ("el precio de los tenis dismunuye un", resultado) 

#Mostrar nuevo valor de los Jeans y los zapatos 
Nuevo_precio_Jeans = (precio[3] *0.062) + precio [3]  
print ("los jeans tienen un nuevo precio", Nuevo_precio_Jeans) 

Nuevo_precio_zapatos = (precio [0] *0.008) - precio [0]
print ("los zapatos tienen un nuevo precio",Nuevo_precio_zapatos)  