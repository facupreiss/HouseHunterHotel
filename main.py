import os
from flask import Flask, render_template
from basededatos.conexion import Conexion
from basededatos.models import TipoHabitacion, Estado, Habitacion


def createApp(testing=False):
  app = Flask(__name__)
  if testing:
    app.config.from_object('config.TestConfig')
  else:
    app.config.from_object('config.Config')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  return app


app = createApp()
conexion = Conexion(app)

with app.app_context():
  conexion.crearTablas()

@app.route('/')
def index():
  habitaciones = conexion.listarHabitaciones()
  print(habitaciones)
  return render_template('listadoHabitaciones.html', habitaciones=habitaciones)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
