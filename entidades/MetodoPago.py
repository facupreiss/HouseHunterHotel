class MetodoPago:

  def __init__(self, id, nombre):
    self._id = id
    self._nombre = nombre

  def getId(self):
    return self._id

  def getNombre(self):
    return self._nombre

  def setId(self, id):
    self._id = id

  def setNombre(self, nombre):
    self._nombre = nombre
