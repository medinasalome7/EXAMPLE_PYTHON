accion_uno = "Ya estoy en la entrada del evento"
accion_dos = "Me estoy registrando"

#Estructura de control (condicional o sentencia if o si )
#Permite continual un flijo (realizar algo) si se cumple una condicion 
#y en caso de no cumplirse, se puede o no continual con otro flujo (hacer otra cosa)
# esta sentencia (condicional if) va acompañado de los operadores de comprension 
"""
if estructura_datos_uno < estructura_datos _dos 
if estructura_datos_uno <= estructura_datos_dos 
if estructura_datos_uno > estructura_datos_dos
if estructura_datos_uno >= estructura_datos_dos 
if estructura_datos_uno == estructura_datos_dos 
if estructura_datos_uno != estructura_datos_dos 
"""

#Hay varias maneras de utilizar la sentencia if 
#if simple, if compuesto, if anidado 

#if simple 
dato_comparacion = 18 
edad = 22
"""if edad >= dato_comparacion: 
    print("Ingresar, difrutar del evento")
"""
"""

#if compuesto 
if edad >= dato_comparacion: 
    print("Ingresar, difrutar del evento")
else:
    print("No ingresar")
    """

boleta = True
fecha_evento = "28-02-2023"
fecha_comparacion = "28-02-2023"
#if anidado
if edad >= dato_comparacion and boleta and fecha_evento == fecha_comparacion: 
    print("Ingresar, difrutar del evento")
else:
    print("No ingresar")

    