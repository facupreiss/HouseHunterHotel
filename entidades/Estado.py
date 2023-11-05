class Estado:
  def __init__(self, id, descripcion, fecha_fin):
    self._id = id
    self._descripcion = descripcion
    self._fecha_fin = fecha_fin

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getDescripcion(self):
        return self._descripcion

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def getFechaFin(self):
        return self._fecha_fin

    def setFechaFin(self, fecha_fin):
        self._fecha_fin = fecha_fin