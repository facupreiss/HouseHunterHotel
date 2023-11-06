class Estado:

  def __init__(self, descripcion, id=None):
    self._id = id
    self._descripcion = descripcion

  def getId(self):
    return self._id

  def setId(self, id):
    self._id = id

  def getDescripcion(self):
    return self._descripcion

  def setDescripcion(self, descripcion):
    self._descripcion = descripcion
