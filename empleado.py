empleados = "trabajan 8 horas diarias"

valor_hora = "5.000"
proyecto_a = "20.000"
proyecto_b = "10.000"
dia = "8"
dias_trabajados = "30 dias" 
print(valor_hora)
print("Sueldo por hora")

#sueldo de las ocho horas trabajadas
sueldo_hora = [5.000, 8]
sueldo_dia = sueldo_hora[0] * sueldo_hora [1]
print(sueldo_dia)
print("Pago del día")

#sueldo total del mes
sueldo_mes = [40.000, 30]
sueldo_total = sueldo_mes[0] * sueldo_mes [1]
print(sueldo_total)
print("Pago total del mes")

#hora extra incrementada un 6%
hora_extra = [5.000, 0.006]
sueldo_extra = hora_extra [0] * hora_extra[1]
print(sueldo_extra)

#valor de las 3 horas extras incrementadas 
horas_extras = [5.300, 3]
sueldo_extra = horas_extras [0] * horas_extras[1]
print(sueldo_extra)
print("Se le incremento un 6 porciento al sueldo actual")

Nuevo_sueldo = sueldo_total + sueldo_extra
print(Nuevo_sueldo)
print("Aumento realizado")

sueldo_actual = 15000000

if sueldo_actual <= 15000000: 
    print("salario mayor a tope maximo")
else:
    print("se le incrementa un 6 porciento")
    