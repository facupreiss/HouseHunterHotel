class Cliente:

  def __init__(self, id, dni, nombre, apellido, telefono, email):
    self._id = id
    self._nombre = nombre
    self._apellido = apellido
    self._telefono = telefono
    self._email = email
    self._dni = dni
  
  def getId(self):
    return self._id
  
  def getNombre(self):
    return self._nombre
  
  def setNombre(self, nombre):
    self._nombre = nombre
  
  def setId(self, id):
    self._id = id
    
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
  
  def getDni(self):
    return self

  def setDni(self, dni):
    self._dni = dni

  