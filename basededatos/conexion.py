from flask_sqlalchemy import SQLAlchemy
from basededatos.models import Habitacion, Estado, TipoHabitacion, db


class Conexion:
  def __init__(self, app=None):
      if app is not None:
          self.init_app(app)

  def init_app(self, app):
      db.init_app(app)

  def crearTablas(self):
      db.create_all()

  def listarHabitaciones(self):
      return Habitacion.query.all()

  def eliminarHabitaciones(self):
     Habitacion.query.delete()
     db.session.commit()

  def agregarHabitacion(self, numero, capacidad, precio, imagen, tipo_nombre, estado_descripcion):
    tipo_habitacion = TipoHabitacion.query.filter_by(nombre=tipo_nombre).first()
    estado = Estado.query.filter_by(descripcion=estado_descripcion).first()

    if not tipo_habitacion or not estado:
        return False

    nueva_habitacion = Habitacion(
        numero=numero,
        capacidad=capacidad,
        precio=precio,
        imagen=imagen,
        tipo_habitacion=tipo_habitacion,
        estado=estado
    )

    db.session.add(nueva_habitacion)
    db.session.commit()
    return True

  def eliminarTipoHabitaciones(self):
    TipoHabitacion.query.delete()
    db.session.commit()

  def eliminarEstados(self):
    Estado.query.delete()
    db.session.commit()

  def agregarEstado(self, descripcion):
    nuevo_estado = Estado(descripcion=descripcion)
    db.session.add(nuevo_estado)
    db.session.commit()

  def agregarTipoHabitacion(self, nombre):
    nuevo_tipo = TipoHabitacion(nombre=nombre)
    db.session.add(nuevo_tipo)
    db.session.commit()