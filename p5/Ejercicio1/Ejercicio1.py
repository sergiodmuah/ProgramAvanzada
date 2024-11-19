# Decorador para registrar la operación, entradas y resultado
def operation_logger(func, operation_name):
    def wrapper(*args, **kwargs):
        try:
            # Realizamos la operación
            result = func(*args, **kwargs)
            # Registramos la operación
            print(f"Operación: {operation_name}")
            print(f"Entradas: {args} ")
            print(f"Resultado:")
            return result
        except Exception as e:
            print(f"Error en la operación {operation_name}: {e}")
            return None
    return wrapper

# Funciones lambda para operaciones matemáticas básicas
add = lambda *args: sum(args)
subtract = lambda *args: args[0] - sum(args[1:])
multiply = lambda *args: 1 if len(args) == 0 else args[0] * multiply(*args[1:])
divide = lambda *args: args[0] / args[1] if args[1] != 0 else 'Error: División por cero'

# Función que realiza la operación matemática
def math_operation(operation, operation_name, *args, **kwargs):
    return operation_logger(operation, operation_name)(*args, **kwargs)

# Pruebas con diferentes operaciones
print(math_operation(add, "add", 5, 3))              
print(math_operation(subtract, "subtract", 10, 4))    
print(math_operation(multiply, "multiply", 2, 6))      
print(math_operation(divide, "divide", 15, 3))         
print(math_operation(divide, "divide", 10, 0))         
print(math_operation(add, "add", 1, 2, 3, 4, 5))       
