class Usuario:

  def __init__(self, id, username, password, empleado):
    self._id = id
    self._username = username
    self._password = password
    self._emlpeado = empleado

  def getId(self):
    return self._id

  def getUsername(self):
    return self._username

  def getPassword(self):
    return self._password

  def getEmpleado(self):
    return self._empleado

  def setId(self, id):
    self._id = id

  def setUsername(self, username):
    self._username = username

  def setPassword(self, password):
    self._password = password

  def setEmpleado(self, empleado):
    self._empleado = empleado
