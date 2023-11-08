import unittest
from basededatos.conexion import Conexion
from basededatos.models import TipoHabitacion, Habitacion, Estado
from main import createApp
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class TestConexion(unittest.TestCase):

  def setUp(self):
    self.app = createApp(testing=True)  
    self.conexion = Conexion(self.app)
    self.app_context = self.app.app_context()
    self.app_context.push()
    self.conexion.crearTablas()
    self.conexion.agregarEstado(descripcion='Ocupado')
    self.conexion.agregarEstado(descripcion='Disponible')
    self.conexion.agregarTipoHabitacion(nombre='Suite')
    habitacion_tipo = TipoHabitacion.query.filter_by(nombre='Suite').first()
    estado_disponible = Estado.query.filter_by(descripcion='Disponible').first()
    estado_ocupado = Estado.query.filter_by(descripcion='Ocupado').first()
    self.conexion.agregarHabitacion(numero=1,
                                      capacidad=4,
                                      precio=166,
                                      imagen='hotel.jpg',
                                      tipo_habitacion=habitacion_tipo,
                                      estado=estado_disponible)
    self.conexion.agregarHabitacion(numero=2,
                                      capacidad=4,
                                      precio=166,
                                      imagen='hotel.jpg',
                                      tipo_habitacion=habitacion_tipo,
                                      estado=estado_disponible)
    self.conexion.agregarHabitacion(numero=3,
                                      capacidad=4,
                                      precio=166,
                                      imagen='hotel.jpg',
                                      tipo_habitacion=habitacion_tipo,
                                      estado=estado_ocupado)
    
  def tearDown(self):
    self.conexion.eliminarHabitaciones()
    self.conexion.eliminarTipoHabitaciones()
    self.conexion.eliminarEstados()
    self.app_context.pop()

  def test_obtener_cantidad_total_de_habitaciones(self):
    cantidad_total = self.conexion.getCantidadHabitaciones()
    self.assertEqual(cantidad_total, 3)

  def test_obtener_cantidad_habitaciones_disponibles(self):
    cantidad_disponibles = self.conexion.getCantidadHabitacionesDisponibles()
    self.assertEqual(cantidad_disponibles, 2)



if __name__ == '__main__':
  unittest.main()
