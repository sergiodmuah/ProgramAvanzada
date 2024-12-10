from registro_diario import RegistroDiario
from cliente import Cliente
from empleado import Empleado
from utils import leer_cadena, leer_entero

def main():
    registro = RegistroDiario()
    
    while True:
        print("\nMenú Principal:")
        print("1. Introducir empleado")
        print("2. Introducir cliente")
        print("3. Buscar por nombre (y edad)")
        print("4. Mostrar registro diario")
        print("5. Mostrar empleados")
        print("6. Visualizar persona por índice")
        print("7. Combinar registros diarios")
        print("8. Salir")

        opcion = leer_entero("Seleccione una opción: ")
        
        if opcion == 1:
            nombre = leer_cadena("Nombre: ")
            edad = leer_entero("Edad: ")
            categoria = leer_cadena("Categoría: ")
            antiguedad = leer_entero("Antigüedad: ")
            empleado = Empleado(nombre, edad, categoria=categoria, antiguedad=antiguedad)
            registro.agregar_persona(empleado)

        elif opcion == 2:
            nombre = leer_cadena("Nombre: ")
            edad = leer_entero("Edad: ")
            dni = leer_cadena("DNI: ")
            cliente = Cliente(nombre, edad, dni=dni)
            registro.agregar_persona(cliente)

        elif opcion == 3:
            nombre = leer_cadena("Nombre: ")
            edad = leer_entero("Edad: ")
            encontrado = [p.visualizar() for p in registro._personas if p.nombre == nombre and p.edad == edad]
            print(encontrado if encontrado else "No se encontró la persona.")

        elif opcion == 4:
            print("\nRegistro Diario:")
            print("\n".join(registro.visualizar_registro()))

        elif opcion == 5:
            print("\nEmpleados:")
            print("\n".join(registro.visualizar_empleados()))

        elif opcion == 6:
            index = leer_entero("Índice: ")
            try:
                print(registro[index])
            except IndexError:
                print("Índice fuera de rango.")

        elif opcion == 7:
            otro_registro = RegistroDiario()
            print("Añadiendo dos personas al segundo registro...")
            otro_registro.agregar_persona(Cliente("Ana", 30, dni="12345678A"))
            otro_registro.agregar_persona(Empleado("Carlos", 45, categoria="Técnico", antiguedad=10))
            registro = registro + otro_registro
            print("Registros combinados exitosamente.")

        elif opcion == 8:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
