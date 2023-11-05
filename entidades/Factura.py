class Factura:
  def __init__(self, id, precio_total, fecha, metodo_pago, cliente, reserva):
    self.precio_total = precio_total
    self.fecha = fecha
    self.metodo_pago = metodo_pago
    self.cliente = cliente
    self.reserva = reserva
    self.id = id
    
  def getId(self):
    return self.id

  def getPrecioTotal(self):
    return self.precio_total

  def getFecha(self):
    return self.fecha

  def getMetodoPago(self):
    return self.metodo_pago

  def getCliente(self):
    return self.cliente

  def getReserva(self):
    return self.reserva

  def setPrecioTotal(self, precio_total):
    self.precio_total = precio_total

  def setFecha(self, fecha):
    self.fecha = fecha

  def setMetodoPago(self, metodo_pago):
    self.metodo_pago = metodo_pago

  def setCliente(self, cliente):
    self.cliente = cliente

  def setReserva(self, reserva):
    self.reserva = reserva

  