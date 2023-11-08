from flask_sqlalchemy import SQLAlchemy
from basededatos.models import db, Habitacion, Estado, TipoHabitacion, Empleado, Categoria, Usuario, Reserva, Cliente, Factura, MetodoPago


class Conexion:

  def __init__(self, app=None):
    if app is not None:
      self.init_app(app)

  def init_app(self, app):
    db.init_app(app)

  def crearTablas(self):
    db.create_all()

#CRUD HABITACION

  def listarHabitaciones(self):
    return Habitacion.query.all()

  def eliminarHabitaciones(self):
    Habitacion.query.delete()
    db.session.commit()

  def getCantidadHabitaciones(self):
    return Habitacion.query.count()

  def getCantidadHabitacionesDisponibles(self):
    estado_disponible = Estado.query.filter_by(
        descripcion='Disponible').first()
    if estado_disponible:
      cantidad_disponibles = Habitacion.query.filter_by(
          id_estado=estado_disponible.id_estado).count()
      return cantidad_disponibles
    else:
      return 0

  def agregarHabitacion(self, numero, capacidad, precio, imagen,
                        tipo_habitacion, estado):
    nueva_habitacion = Habitacion(
        numero=numero,
        capacidad=capacidad,
        precio=precio,
        imagen=imagen,
        id_tipo_habitacion=tipo_habitacion.id_tipo_habitacion,
        id_estado=estado.id_estado)
    db.session.add(nueva_habitacion)
    db.session.commit()

  def eliminarHabitacionPorNumero(self, numero):
    habitacion = Habitacion.query.filter_by(numero=numero).first()
    if habitacion:
      db.session.delete(habitacion)
      db.session.commit()
      return True
    else:
      return False

#CRUD TIPO HABITACION

  def agregarTipoHabitacion(self, nombre):
    nuevo_tipo_habitacion = TipoHabitacion(nombre=nombre)
    db.session.add(nuevo_tipo_habitacion)
    db.session.commit()

  def listarTipoHabitaciones(self):
    return TipoHabitacion.query.all()

  def eliminarTipoHabitaciones(self):
    TipoHabitacion.query.delete()
    db.session.commit()

  def eliminarTipoHabitacionPorNombre(self, nombre):
    tipo_habitacion = TipoHabitacion.query.filter_by(nombre=nombre).first()
    if tipo_habitacion:
      db.session.delete(tipo_habitacion)
      db.session.commit()
      return True
    else:
      return False


#CRUD ESTADO

  def agregarEstado(self, descripcion):
    nuevo_estado = Estado(descripcion=descripcion)
    db.session.add(nuevo_estado)
    db.session.commit()

  def listarEstados(self):
    return Estado.query.all()

  def eliminarEstados(self):
    Estado.query.delete()
    db.session.commit()

  def eliminarEstadoPorNombre(self, descripcion):
    estado = Estado.query.filter_by(descripcion=descripcion).first()
    if estado:
      db.session.delete(estado)
      db.session.commit()
      return True
    else:
      return False
