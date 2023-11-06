class TipoHabitacion:

  def __init__(self, nombre, id=None):
    self._id = id
    self._nombre = nombre

  def getId(self):
    return self._id

  def getNombre(self):
    return self._nombre

  def setNombre(self, nombre):
    self._nombre = nombre

  def setId(self, id):
    self._id = id
