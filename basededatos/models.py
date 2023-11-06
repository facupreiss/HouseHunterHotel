from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Habitacion(db.Model):
  __tablename__ = 'habitacion'
  id_habitacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
  numero = db.Column(db.Integer)
  capacidad = db.Column(db.Integer)
  precio = db.Column(db.Float)
  imagen = db.Column(db.String(255))
  id_tipo_habitacion = db.Column(db.Integer, db.ForeignKey('tipo_habitacion.id_tipo_habitacion'))
  id_estado = db.Column(db.Integer, db.ForeignKey('estado.id_estado'))

  tipo_habitacion = db.relationship('TipoHabitacion', back_populates='habitaciones')
  estado = db.relationship('Estado', back_populates='habitaciones')

  def getImagen(self):
    return self.imagen

class TipoHabitacion(db.Model):
  __tablename__ = 'tipo_habitacion'
  id_tipo_habitacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre = db.Column(db.String(255))
  habitaciones = db.relationship('Habitacion', back_populates='tipo_habitacion')

class Estado(db.Model):
  __tablename__ = 'estado'
  id_estado = db.Column(db.Integer, primary_key=True, autoincrement=True)
  descripcion = db.Column(db.String(255))
  habitaciones = db.relationship('Habitacion', back_populates='estado')