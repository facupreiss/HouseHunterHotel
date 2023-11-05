class Empleado:

  def __init__(self, id, dni, nombre, apellido, telefono, email, categoria):
    self._dni = dni
    self._nombre = nombre
    self._apellido = apellido
    self._telefono = telefono
    self._email = email
    self._categoria = categoria
    self._id = id

  def getDni(self):
    return self._dni

  def setDni(self, dni):
    self._dni = dni

  def getNombre(self):
    return self._nombre

  def setNombre(self, nombre):
    self._nombre = nombre

  def getApellido(self):
    return self._apellido

  def setApellido(self, apellido):
    self._apellido = apellido

  def getTelefono(self):
    return self._telefono

  def setTelefono(self, telefono):
    self._telefono = telefono

  def getEmail(self):
    return self._email

  def setEmail(self, email):
    self._email = email

  def getCategoria(self):
    return self._categoria

  def setCategoria(self, categoria):
    self._categoria = categoria

  def getId(self):
    return self._id

  def setId(self, id):
    self._id = id

  def __toString__(self):
    return "DNI: " + str(self._dni) + "\nNombre: " + str(
        self._nombre) + "\nApellido: " + str(
            self._apellido) + "\nTelefono: " + str(
                self._telefono) + "\nEmail: " + str(self._email)
