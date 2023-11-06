from flask import Flask, render_template
from basededatos.conexion import Conexion
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.abspath('basededatos/mi_bd.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
