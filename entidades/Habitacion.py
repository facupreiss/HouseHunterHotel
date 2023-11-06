class Habitacion:

  def __init__(self, numero, capacidad, precio, imagen, tipo, estado, id=None):
    self._id = id
    self._numero = numero
    self._capacidad = capacidad
    self._precio = precio
    self._imagen = imagen
    self._tipo = tipo
    self._estado = estado

  def getId(self):
    return self._id

  def setId(self, id):
    self._id = id

  def getNumero(self):
    return self._numero

  def setNumero(self, numero):
    self._numero = numero

  def getCapacidad(self):
    return self._capacidad

  def setCapacidad(self, capacidad):
    self._capacidad = capacidad

  def getPrecio(self):
    return self._precio

  def setPrecio(self, precio):
    self._precio = precio

  def getImagen(self):
    return self._imagen

  def setImagen(self, imagen):
    self._imagen = imagen

  def getTipo(self):
    return self._tipo

  def setTipo(self, tipo):
    self._tipo = tipo

  def getEstado(self):
    return self._estado

  def setEstado(self, estado):
    self._estado = estado
