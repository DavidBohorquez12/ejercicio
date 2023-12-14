#Inicialización de variables
salario = 0
diasTra = 30
valorBase = 1300000
valorDia = valorBase / 30
subTransporte = valorBase * 0.1
aporteSocial = valorBase * 0.04
llamadosAtencion = valorBase * 0.9

#Solicitar datos al usuario
nombreEmpleado = input("Ingresa el Nombre del Empleado: ")
print("Ingresa el Rango de Empleado")
print("A. Mensajero")
print("B. Administrativo")
print("C. IT Soluciones")
print("D. Seguridad")
rangoEmpleado = input()

#Calcular el valor del bono según el rango del empleado
if rangoEmpleado == 'A':
    valorBono = subTransporte
elif rangoEmpleado in ['B', 'C']:
    valorBono = valorBase * 0.1
elif rangoEmpleado == 'D':
    valorBono = 300000
else:
    print("Error: Rango no reconocido. Inténtalo de nuevo más tarde.")
    exit()

#Verificar si el empleado tiene llamados de atención
continuar = input("El Empleado Cuenta con Llamados de Atencion (s/n): ")
if continuar.lower() == 's':
    salario = llamadosAtencion
else:
    salario = valorBase

#Verificar si el empleado tiene días de incapacidad
continuar = input("El Empleado Cuenta con Dias de Incapacidad (s/n): ")
if continuar.lower() == 's':
    diasIncapacidad = int(input("Cuantos dias? 1, 2, 3: "))
    diasTra = 30 - diasIncapacidad
    valorDia = salario / diasTra
    salario = diasTra * valorDia

#Verificar si el empleado tiene horas extras
continuar = input("El Empleado Cuenta con Horas Extras (s/n): ")
if continuar.lower() == 's':
    horasTrabajadas = int(input("Cuantas Horas? 1, 2, 3: "))
    salario += horasTrabajadas * 20000

#Mostrar resultados
print("**")
print("Nombre:", nombreEmpleado)
print("Salario Base:", salario)
print("Dias Trabajados:", diasTra)
print("Valor Dia:", valorDia)
print("Valor Bono:", valorBono)
print("Valor Descuento por Penalizacion:", llamadosAtencion)
print("Seguridad Social:", aporteSocial)
print("Total a Pagar:", salario + valorBono)

              

