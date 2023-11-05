class Reserva:

  def __init__(self, id, fecha_entrada, fecha_salida, cliente, habitacion):
    self._id = id
    self._fecha_entrada = fecha_entrada
    self._fecha_salida = fecha_salida
    self._cliente = cliente
    self._habitacion = habitacion
  
  def getId(self):
    return self._id
  
  def setId(self, id):
    self._id = id
  
  def getFechaEntrada(self):
    return self._fecha_entrada
  
  def setFechaEntrada(self, fecha_entrada):
    self._fecha_entrada = fecha_entrada
  
  def getFechaSalida(self):
    return self._fecha_salida
  
  def setFechaSalida(self, fecha_salida):
    self._fecha_salida = fecha_salida
  
  def getCliente(self):
    return self._cliente
  
  def setCliente(self, cliente):
    self._cliente = cliente
  
  def getHabitacion(self):
    return self._habitacion
  
  def setHabitacion(self, habitacion):
    self._habitacion = habitacion

