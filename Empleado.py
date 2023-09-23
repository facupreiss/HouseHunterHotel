class Empleado:
    def __init__(self, dni, nombre, apellido, email, telefono):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

# Ejemplo de cómo crear un objeto Empleado
empleado1 = Empleado("12345678", "Juan", "Pérez", "juan@example.com", "123-456-789")

print("DNI:", empleado1.dni)
print("Nombre:", empleado1.nombre)
print("Apellido:", empleado1.apellido)
print("Email:", empleado1.email)
print("Teléfono:", empleado1.telefono)
