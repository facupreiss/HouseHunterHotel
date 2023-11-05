class Empleado:

  def __init__(self,dni,nombre,apellido,telefono,email):
    self._dni = dni
    self._nombre = nombre
    self._apellido = apellido
    self._telefono = telefono
    self._email = email

  def getDni(self):
    return self._dni

  def setDni(self,dni):
    self._dni = dni

  def getNombre(self):
    return self._nombre

  def setNombre(self,nombre):
    self._nombre = nombre

  def getApellido(self):
    return self._apellido

  def setApellido(self,apellido):
    self._apellido = apellido

  def getTelefono(self):
    return self._telefono

  def setTelefono(self,telefono):
    self._telefono = telefono

  def getEmail(self):
    return self._email
  
  def setEmail(self,email):
    self._email = email

  def __toString__(self):
    return "DNI: " + str(self._dni) + "\nNombre: " + str(self._nombre) + "\nApellido: " + str(self._apellido) + "\nTelefono: " + str(self._telefono) + "\nEmail: " + str(self._email)