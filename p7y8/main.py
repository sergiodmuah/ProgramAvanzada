from publicacion import Libro, Revista
from utils import guardar_publicaciones, cargar_publicaciones, validar_input_tipo
from excepciones import ErrorBiblioteca, ErrorArchivo

def menu():
    """Muestra el menú principal y gestiona las opciones."""
    publicaciones = []

    while True:
        print("\nMenú:")
        print("1. Añadir publicaciones (libros o revistas)")
        print("2. Mostrar publicaciones disponibles")
        print("3. Guardar publicaciones en un fichero")
        print("4. Cargar publicaciones desde un fichero")
        print("5. Salir")

        opcion = validar_input_tipo('int', "Seleccione una opción: ")

        if opcion == 1:
            tipo = input("¿Es un libro o una revista? (l/r): ").lower()
            try:
                if tipo == 'l':
                    titulo = input("Ingrese el título del libro: ")
                    autor = input("Ingrese el autor del libro: ")
                    anio = validar_input_tipo('int', "Ingrese el año de publicación: ")
                    genero = input("Ingrese el género del libro: ")
                    publicaciones.append(Libro(titulo, autor, anio, genero))
                elif tipo == 'r':
                    titulo = input("Ingrese el título de la revista: ")
                    autor = input("Ingrese el autor de la revista: ")
                    anio = validar_input_tipo('int', "Ingrese el año de publicación: ")
                    num_edicion = validar_input_tipo('int', "Ingrese el número de edición: ")
                    publicaciones.append(Revista(titulo, autor, anio, num_edicion))
                else:
                    print("Opción no válida.")
            except ValueError as e:
                print(f"Error de entrada: {e}")
            except ErrorBiblioteca as e:
                print(f"Error de biblioteca: {e}")

        elif opcion == 2:
            if publicaciones:
                for pub in publicaciones:
                    print(pub.descripcion())
            else:
                print("No hay publicaciones registradas.")

        elif opcion == 3:
            nombre_fichero = input("Ingrese el nombre del fichero para guardar las publicaciones: ")
            try:
                guardar_publicaciones(publicaciones, nombre_fichero)
                print("Publicaciones guardadas correctamente.")
            except ErrorArchivo as e:
                print(f"Error al guardar el archivo: {e}")

        elif opcion == 4:
            nombre_fichero = input("Ingrese el nombre del fichero para cargar las publicaciones: ")
            try:
                publicaciones = cargar_publicaciones(nombre_fichero)
                print("Publicaciones cargadas correctamente.")
            except ErrorArchivo as e:
                print(f"Error al cargar el archivo: {e}")

        elif opcion == 5:
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
