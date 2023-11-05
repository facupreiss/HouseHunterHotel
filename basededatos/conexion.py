from entidades.Empleado import Empleado
import sqlite3


#id_categoria FOREIGN KEY REFERENCES categoria(id_categoria)
class Conexion:

  def __init__(self, nombreBaseDatos):
    self.conexion = sqlite3.connect(nombreBaseDatos)
    self.cursor = self.conexion.cursor()

#CREO LAS TABLAS DE LA BD

  def crearTabla(self):

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS empleado(
    id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
    dni INTEGER,
    nombre TEXT,
    apellido TEXT,
    telefono TEXT,
    email TEXT,
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS categoria(
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuario(
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    contrasenia TEXT,
    id_empleado FOREIGN KEY REFERENCES empleado(id_empleado)
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuario(
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    contrasenia TEXT,
    id_empleado FOREIGN KEY REFERENCES empleado(id_empleado)
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS habitacion(
    id_habitacion INTEGER PRIMARY KEY AUTOINCREMENT,
    numero INTEGER,
    capacidad INTEGER,
    precio REAL,
    imagen TEXT,
    tipo_habitacion FOREIGN KEY REFERENCES tipo_habitacion(id_tipo_habitacion),
    estado FOREIGN KEY REFERENCES estado(id_estado)
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS estado(
    id_estado INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT,
    fin_de_servicio DATE,
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS tipo_habitacion(
    id_tipo_habitacion INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS reserva(
    id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_entrada DATE,
    fecha_salida DATE,
    id_cliente FOREIGN KEY REFERENCES cliente(id_cliente),
    id_habitacion FOREIGN KEY REFERENCES habitacion(id_habitacion)
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS cliente(
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    dni INTEGER,
    nombre TEXT,
    apellido TEXT,
    telefono INTEGER,
    email TEXT
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS factura(
    id_factura INTEGER PRIMARY KEY AUTOINCREMENT,
    precio_total REAL,
    fecha DATE,
    metodo_pago FOREIGN KEY REFERENCES metodo_pago(id_metodo_pago),
    id_cliente FOREIGN KEY REFERENCES cliente(id_cliente),
    id_reserva FOREIGN KEY REFERENCES reserva(id_reserva)
    )''')

    self.conexion.commit()

  def agregarEmpleado(self, empleado):
    self.cursor.execute(
        '''INSERT INTO empleado(dni,nombre,apellido,telefono,email,id_categoria) VALUES(?,?,?,?,?))''',
        (empleado.getDni(), empleado.getNombre(), empleado.getApellido(),
         empleado.getTelefono(), empleado.getEmail(), empleado.getCategoria()))
    self.conexion.commit()

  def modificarEmpleado(self, empleado):
    self.cursor.execute(
        '''UPDATE empleado SET dni=?, nombre=?, apellido=?, telefono=?, email=?, id_categoria=? WHERE id_empleado=?''',
        (empleado.getDni(), empleado.getNombre(), empleado.getApellido(),
         empleado.getTelefono(), empleado.getEmail(), empleado.getCategoria(),
         empleado.getId()))
    self.conexion.commit()

  def eliminarEmpleado(self, empleado):
    self.cursor.execute('''DELETE FROM empleado WHERE id_empleado=?''',
                        (empleado.getId()))
    self.conexion.commit()

  def listarEmpleados(self):
    self.cursor.execute('''SELECT * FROM empleado''')
    empleados = self.cursor.fetchall()
    return empleados


#CIERRO LA CONEXION DE LA BD

  def cerrarConexion(self):
    self.cursor.close()
    self.conexion.close()
