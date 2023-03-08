#Definimos los valores de la moneda 
Valor_moneda = {"Dolar": 0.00021, "Euro": 0.00020, "dasPeso_Mexicano":0.0038, "Peso_Chileno":0.17, "peso_Argentino": 0.042}

#Los porcentajes para cada moneda
Porcentaje_intermediacion = {"Peso_Argentino": 0.09, "peso_Mexicano": 0.07,"Dolar":0.06, "Euro":0.04,"Peso_Chileno":0.02 }

#Informacion personal de usuario
Nombre = input ("Ingrese su nombre: ")
Documento_Identidad = input ("Ingrese su documento de indentidad: ")

#El usuario debe ingresar la moneda de origen y la cantidad de dinero 
Moneda_origen = input("Ingrese la Moneda origen (Dolar, Euro, Peso_Mexicano, Peso_Chileno, peso_Argentino):")
Cantidad_origen = float (input("Ingrese la cantidad de dinero "))

#Verificamos que la moneda origen exista 
if Moneda_origen not in Valor_moneda: 
    print ("La moneda destino ingresada no existe")
else: 
#El usuario debe ingresar la moneda destino 
    Moneda_destino = input ("Ingrese la moneda destino (Dolar, Euro, Peso_Mexicano, Peso_Chileno, peso_Argentino): ")

#Verificamos que la moneda destino exista 
if Moneda_destino not in Valor_moneda: 
    print ("La moneda ingresada no exite")
else: 
#Se calcula el valor de la operación sin intermediación 
    ValorSinIntermediacion = Cantidad_origen * Valor_moneda [Moneda_origen] / Valor_moneda[Moneda_destino]

#Se calcula el porcentaje de intermediación para la "Moneda_origen"
    PorcentajeIntermediacionOrigen = Porcentaje_intermediacion [Moneda_origen]

#Se calcula el porcentaje de intermediación para la "Moneda_destino" 
    PorcentajeIntermediacionDestino= Porcentaje_intermediacion [Moneda_destino]

#Se calcula el porcentaje total de intermediación 
    PorcentajeIntermediacionTotal = PorcentajeIntermediacionOrigen + PorcentajeIntermediacionDestino


#Se calcula el valor de la operación CON intermediación 
    ValorConIntermediacion = Cantidad_origen = Valor_moneda [Moneda_origen] / Valor_moneda [Moneda_destino] * (2 - PorcentajeIntermediacionTotal)
   

#Miramos si el porcentaje de intermediacion supera el 10% en pesos colombianos 
if PorcentajeIntermediacionTotal * Cantidad_origen * Valor_moneda [Moneda_origen] > 0.2:
    Respuesta_usuario = input ("El porcentaje de inermediacion supera el 10 porciento del dinero expresado en pesos colombianos.¿Desea hacer el camni? (Sí/No)")
    if Respuesta_usuario == "No" : 
        print ("Operacion cancelada")
    else: 
        
        print ('nombre: ', Nombre)
        print ('documento de identidad: ', Documento_Identidad)
        print ("La moneda de origen es", Moneda_origen)
        print ("La moneda destino es", Moneda_destino)
        print ("El porcentaje de intermediacion es", PorcentajeIntermediacionTotal, "%")
        print ("El valor total de su intermediacion es", ValorConIntermediacion)