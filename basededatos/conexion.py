import sqlite3

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
    id_categoria FOREIGN KEY REFERENCES categoria(id_categoria)
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
    id_tipoHabitacion FOREIGN KEY REFERENCES tipo_habitacion(id_tipo_habitacion),
    id_estado FOREIGN KEY REFERENCES estado(id_estado)
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS estado(
    id_estado INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
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
    id_metodo_pago FOREIGN KEY REFERENCES metodo_pago(id_metodo_pago),
    id_cliente FOREIGN KEY REFERENCES habitacion(id_habitacion),
    id_reserva FOREIGN KEY REFERENCES reserva(id_reserva)
    )''')

    self.conexion.commit()

  def agregarEmpleado(self):
    dni = input("Ingrese el DNI del empleado: ")
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    telefono = input("Ingrese el telefono del empleado: ")
    email = input("Ingrese el email del empleado: ")
    empleado = Empleado(dni,nombre,apellido,telefono,email)
    self.cursor.execute('''INSERT INTO empleado(dni,nombre,apellido,telefono,email) VALUES(?,?,?,?,?))''''',(dni,nombre,apellido)


#CIERRO LA CONEXION DE LA BD

  def cerrarConexion(self):
    self.cursor.close()
    self.conexion.close()
