from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Habitacion(db.Model):
  __tablename__ = 'habitacion'
  id_habitacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
  numero = db.Column(db.Integer)
  capacidad = db.Column(db.Integer)
  precio = db.Column(db.Float)
  imagen = db.Column(db.String(255))
  id_tipo_habitacion = db.Column(
      db.Integer, db.ForeignKey('tipo_habitacion.id_tipo_habitacion'))
  id_estado = db.Column(db.Integer, db.ForeignKey('estado.id_estado'))

  tipo_habitacion = db.relationship('TipoHabitacion',
                                    back_populates='habitaciones')
  estado = db.relationship('Estado', back_populates='habitaciones')

  reservas = db.relationship('Reserva', back_populates='habitacion')

  def __init__(self, numero, capacidad, precio, imagen, id_tipo_habitacion,
               id_estado):
    self.numero = numero
    self.capacidad = capacidad
    self.precio = precio
    self.imagen = imagen
    self.id_tipo_habitacion = id_tipo_habitacion
    self.id_estado = id_estado

  def getImagen(self):
    return self.imagen


class TipoHabitacion(db.Model):
  __tablename__ = 'tipo_habitacion'
  id_tipo_habitacion = db.Column(db.Integer,
                                 primary_key=True,
                                 autoincrement=True)
  nombre = db.Column(db.String(255))

  habitaciones = db.relationship('Habitacion',
                                 back_populates='tipo_habitacion')

  def __init__(self, nombre):
    self.nombre = nombre
  

class Estado(db.Model):
  __tablename__ = 'estado'
  id_estado = db.Column(db.Integer, primary_key=True, autoincrement=True)
  descripcion = db.Column(db.String(255))

  habitaciones = db.relationship('Habitacion', back_populates='estado')

  def __init__(self, descripcion):
    self.descripcion = descripcion
    
class Empleado(db.Model):
  __tablename__ = 'empleado'
  id_empleado = db.Column(db.Integer, primary_key=True, autoincrement=True)
  dni = db.Column(db.Integer)
  nombre = db.Column(db.String(255))
  apellido = db.Column(db.String(255))
  telefono = db.Column(db.Integer)
  email = db.Column(db.String(255))
  id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id_categoria'))

  categoria = db.relationship('Categoria', back_populates='empleados')

  usuarios = db.relationship('Usuario', back_populates='empleado')

  def __init__(self, dni, nombre, apellido, telefono, email, id_categoria):
    self.dni = dni
    self.nombre = nombre
    self.apellido = apellido
    self.telefono = telefono
    self.email = email
    self.id_categoria = id_categoria

class Categoria(db.Model):
  __tablename__ = 'categoria'
  id_categoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre = db.Column(db.String(255))

  empleados = db.relationship('Empleado', back_populates='categoria')

  def __init__(self, nombre):
    self.nombre = nombre


class Usuario(db.Model):
  __tablename__ = 'usuario'
  id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre = db.Column(db.String(255))
  contrasenia = db.Column(db.String(255))
  id_empleado = db.Column(db.Integer, db.ForeignKey('empleado.id_empleado'))

  empleado = db.relationship('Empleado', back_populates='usuarios')

  def __init__(self, nombre, contrasenia, id_empleado):
    self.nombre = nombre
    self.contrasenia = contrasenia
    self.id_empleado = id_empleado


class Reserva(db.Model):
  __tablename__ = 'reserva'
  id_reserva = db.Column(db.Integer, primary_key=True, autoincrement=True)
  fecha_entrada = db.Column(db.DateTime)
  fecha_salida = db.Column(db.DateTime)
  id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'))
  id_habitacion = db.Column(db.Integer,
                            db.ForeignKey('habitacion.id_habitacion'))

  cliente = db.relationship('Cliente', back_populates='reservas')
  habitacion = db.relationship('Habitacion', back_populates='reservas')

  facturas = db.relationship('Factura', back_populates='reserva')

  def __init__(self, fecha_entrada, fecha_salida, id_cliente, id_habitacion):
    self.fecha_entrada = fecha_entrada
    self.fecha_salida = fecha_salida
    self.id_cliente = id_cliente
    self.id_habitacion = id_habitacion


class Cliente(db.Model):
  __tablename__ = 'cliente'
  id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
  dni = db.Column(db.Integer)
  nombre = db.Column(db.String(255))
  apellido = db.Column(db.String(255))
  telefono = db.Column(db.Integer)
  email = db.Column(db.String(255))

  reservas = db.relationship('Reserva', back_populates='cliente')
  facturas = db.relationship('Factura', back_populates='cliente')

  def __init__(self, dni, nombre, apellido, telefono, email):
    self.dni = dni
    self.nombre = nombre
    self.apellido = apellido
    self.telefono = telefono
    self.email = email

class Factura(db.Model):
  __tablename__ = 'factura'
  id_factura = db.Column(db.Integer, primary_key=True, autoincrement=True)
  precio_total = db.Column(db.Float)
  fecha = db.Column(db.DateTime)
  id_metodo_pago = db.Column(db.Integer,
                             db.ForeignKey('metodo_pago.id_metodo_pago'))
  id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'))
  id_reserva = db.Column(db.Integer, db.ForeignKey('reserva.id_reserva'))

  cliente = db.relationship('Cliente', back_populates='facturas')
  reserva = db.relationship('Reserva', back_populates='facturas')
  metodo_pago = db.relationship('MetodoPago', back_populates='facturas')

  def __init__(self, precio_total, fecha, id_metodo_pago):
    self.precio_total = precio_total
    self.fecha = fecha
    self.id_metodo_pago = id_metodo_pago

class MetodoPago(db.Model):
  __tablename__ = 'metodo_pago'
  id_metodo_pago = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre = db.Column(db.String(255))

  facturas = db.relationship('Factura', back_populates='metodo_pago')

  def __init__(self, nombre):
    self.nombre = nombre
