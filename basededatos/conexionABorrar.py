import sqlite3
from flask_sqlalchemy import SQLAlchemy
from basededatos.models import Habitacion, TipoHabitacion, Estado
# from entidades.Categoria import Categoria
# from entidades.Cliente import Cliente
# from entidades.Empleado import Empleado
# from entidades.Estado import Estado
# from entidades.Factura import Factura
# from entidades.Habitacion import Habitacion
# from entidades.MetodoPago import MetodoPago
# from entidades.Reserva import Reserva
# from entidades.TipoHabitacion import TipoHabitacion
# from entidades.Usuario import Usuario


db = SQLAlchemy()

#id_categoria FOREIGN KEY REFERENCES categoria(id_categoria)
class Conexion:

  def __init__(self, nombreBaseDatos, app):
    self.conexion = sqlite3.connect(nombreBaseDatos)
    self.app = app
    self.db = db 
    # self.cursor = self.conexion.cursor()


  def crearTablas(self):
    with self.app.app_context():
        db.create_all()
    #CREO LAS TABLAS DE LA BD

  # def crearTablas(self):
  #   self.cursor.execute('''CREATE TABLE IF NOT EXISTS empleado(
  #       id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
  #       dni INTEGER,
  #       nombre TEXT,
  #       apellido TEXT,
  #       telefono TEXT,
  #       email TEXT
  #   )''')

  #   self.cursor.execute('''CREATE TABLE IF NOT EXISTS categoria(
  #       id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
  #       nombre TEXT
  #   )''')

  #   self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuario(
  #       id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
  #       usuario TEXT,
  #       contrasenia TEXT,
  #       id_empleado INTEGER,
  #       FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado)
  #   )''')

  #   self.cursor.execute('''CREATE TABLE IF NOT EXISTS habitacion(
  #       id_habitacion INTEGER PRIMARY KEY AUTOINCREMENT,
  #       numero INTEGER,
  #       capacidad INTEGER,
  #       precio REAL,
  #       imagen TEXT,
  #       id_tipo_habitacion INTEGER,
  #       id_estado INTEGER,
  #       FOREIGN KEY (id_tipo_habitacion) REFERENCES tipo_habitacion(id_tipo_habitacion),
  #       FOREIGN KEY (id_estado) REFERENCES estado(id_estado)
  #   )''')

  #   self.cursor.execute('''CREATE TABLE IF NOT EXISTS estado(
  #       id_estado INTEGER PRIMARY KEY AUTOINCREMENT,
  #       descripcion TEXT
  #   )''')

  #   self.cursor.execute('''CREATE TABLE IF NOT EXISTS tipo_habitacion(
  #       id_tipo_habitacion INTEGER PRIMARY KEY AUTOINCREMENT,
  #       nombre TEXT
  #   )''')

  #   self.cursor.execute('''CREATE TABLE IF NOT EXISTS reserva(
  #       id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
  #       fecha_entrada DATE,
  #       fecha_salida DATE,
  #       id_cliente INTEGER,
  #       id_habitacion INTEGER,
  #       FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
  #       FOREIGN KEY (id_habitacion) REFERENCES habitacion(id_habitacion)
  #   )''')

  #   self.cursor.execute('''CREATE TABLE IF NOT EXISTS cliente(
  #       id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
  #       dni INTEGER,
  #       nombre TEXT,
  #       apellido TEXT,
  #       telefono INTEGER,
  #       email TEXT
  #   )''')

  #   self.cursor.execute('''CREATE TABLE IF NOT EXISTS factura(
  #       id_factura INTEGER PRIMARY KEY AUTOINCREMENT,
  #       precio_total REAL,
  #       fecha DATE,
  #       id_metodo_pago INTEGER,
  #       id_cliente INTEGER,
  #       id_reserva INTEGER,
  #       FOREIGN KEY (id_metodo_pago) REFERENCES metodo_pago(id_metodo_pago),
  #       FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
  #       FOREIGN KEY (id_reserva) REFERENCES reserva(id_reserva)
  #   )''')

  #   self.cursor.execute('''CREATE TABLE IF NOT EXISTS metodo_pago(
  #       id_metodo_pago INTEGER PRIMARY KEY AUTOINCREMENT,
  #       nombre TEXT
  #   )''')

  #   self.conexion.commit()


  def listarHabitaciones(self):
    return Habitacion.query.all()

  def getCantHabitaciones(self):
    return Habitacion.query.count()

  def listarTiposHabitacion(self):
    return TipoHabitacion.query.all()

  def listarEstados(self):
    return Estado.query.all()

  #CRUD EMPLEADO
  # def agregarEmpleado(self, empleado):
  #   self.cursor.execute(
  #       '''INSERT INTO empleado(dni, nombre, apellido, telefono, email, id_categoria) VALUES(?,?,?,?,?)''',
  #       (empleado.getDni(), empleado.getNombre(), empleado.getApellido(),
  #        empleado.getTelefono(), empleado.getEmail(),
  #        empleado.getCategoria().getId()))
  #   self.conexion.commit()

  # def modificarEmpleado(self, empleado):
  #   self.cursor.execute(
  #       '''UPDATE empleado SET dni=?, nombre=?, apellido=?, telefono=?, email=?, id_categoria=? WHERE id_empleado=?''',
  #       (empleado.getDni(), empleado.getNombre(), empleado.getApellido(),
  #        empleado.getTelefono(), empleado.getEmail(),
  #        empleado.getCategoria().getId(), empleado.getId()))
  #   self.conexion.commit()

  # def eliminarEmpleado(self, empleado):
  #   self.cursor.execute('''DELETE FROM empleado WHERE id_empleado=?''',
  #                       (empleado.getId()))
  #   self.conexion.commit()

  # def listarEmpleados(self):
  #   self.cursor.execute('''SELECT * FROM empleado''')
  #   empleados = self.cursor.fetchall()
  #   return empleados

  # #CRUD CATEGORIA
  # def agregarCategoria(self, categoria):
  #   self.cursor.execute('''INSERT INTO categoria(nombre) VALUES(?))''',
  #                       (categoria.getNombre()))
  #   self.conexion.commit()

  # def modificarCategoria(self, categoria):
  #   self.cursor.execute(
  #       '''UPDATE categoria SET nombre=? WHERE id_categoria=?''',
  #       (categoria.getNombre(), categoria.getId()))
  #   self.conexion.commit()

  # def eliminarCategoria(self, categoria):
  #   self.cursor.execute('''DELETE FROM categoria WHERE id_categoria=?''',
  #                       (categoria.getId()))
  #   self.conexion.commit()

  # def listarCategorias(self):
  #   self.cursor.execute('''SELECT * FROM categoria''')
  #   categorias = self.cursor.fetchall()
  #   return categorias

  # #CRUD USUARIO
  # def agregarUsuario(self, usuario):
  #   self.cursor.execute(
  #       '''INSERT INTO usuario(usuario,contrasenia,id_empleado) VALUES(?,?,?))''',
  #       (usuario.getUsername(), usuario.getPassword(),
  #        usuario.getEmpleado().getId()))
  #   self.conexion.commit()

  # def modificarUsuario(self, usuario):
  #   self.cursor.execute(
  #       '''UPDATE usuario SET usuario=?,contrasenia=?,id_empleado=? WHERE id_usuario=?''',
  #       (usuario.getUsername(), usuario.getPassword(),
  #        usuario.getEmpleado().getId(), usuario.getId()))
  #   self.conexion.commit()

  # def eliminarUsuario(self, usuario):
  #   self.cursor.execute('''DELETE FROM usuario WHERE id_usuario=?''',
  #                       (usuario.getId()))
  #   self.conexion.commit()

  # def listarUsuarios(self):
  #   self.cursor.execute('''SELECT * FROM usuario''')
  #   usuarios = self.cursor.fetchall()
  #   return usuarios

  # #CRUD HABITACION
  # def agregarHabitacion(self, habitacion):
  #   self.cursor.execute(
  #       '''INSERT INTO habitacion(numero,capacidad,precio,imagen,id_tipo_habitacion,id_estado) VALUES(?,?,?,?,?,?)''',
  #       (habitacion.getNumero(), habitacion.getCapacidad(),
  #        habitacion.getPrecio(), habitacion.getImagen(),
  #        habitacion.getTipo().getId(), habitacion.getEstado().getId()))
  #   self.conexion.commit()

  # def modificarHabitacion(self, habitacion):
  #   self.cursor.execute(
  #       '''UPDATE habitacion SET numero=?, capacidad=?, precio=?, imagen=?, id_tipo_habitacion=?, id_estado=? WHERE id_habitacion=?''',
  #       (habitacion.getNumero(), habitacion.getCapacidad(),
  #        habitacion.getPrecio(), habitacion.getImagen(),
  #        habitacion.getTipo().getId(), habitacion.getEstado().getId(),
  #        habitacion.getId()))
  #   self.conexion.commit()

  # def eliminarHabitacion(self, habitacion):
  #   self.cursor.execute('''DELETE FROM habitacion WHERE id_habitacion=?''',
  #                       (habitacion.getId()))
  #   self.conexion.commit()

  # def listarHabitacion(self):
  #   self.cursor.execute('''SELECT * FROM habitacion''')
  #   habitaciones = self.cursor.fetchall()
  #   return habitaciones

  # #CRUD TIPO HABITACION
  # def agregarTipoHabitacion(self, tipohabitacion):
  #   self.cursor.execute('''INSERT INTO tipo_habitacion (nombre) VALUES(?)''',
  #                       (tipohabitacion.getNombre(), ))
  #   self.conexion.commit()

  # def modificarTipoHabitacion(self, tipohabitacion):
  #   self.cursor.execute(
  #       '''UPDATE tipo_habitacion SET nombre=? WHERE id_tipo_habitacion=?''',
  #       (tipohabitacion.getNombre(), ))
  #   self.conexion.commit()

  # def eliminarTipoHabitacion(self, tipohabitacion):
  #   self.cursor.execute(
  #       '''DELETE FROM tipo_habitacion WHERE id_tipo_habitacion=?''',
  #       (tipohabitacion.getId(), ))
  #   self.conexion.commit()

  # def listarTipoHabitacion(self):
  #   self.cursor.execute('''SELECT * FROM tipo_habitacion''')
  #   tipo_habitaciones = self.cursor.fetchall()
  #   return tipo_habitaciones

  # #CRUD ESTADO
  # #CORRECTO
  # def agregarEstado(self, estado):
  #   self.cursor.execute('''INSERT INTO estado (descripcion) VALUES(?)''',
  #                       (estado.getDescripcion(), ))
  #   self.conexion.commit()

  # def modificarEstado(self, estado):
  #   self.cursor.execute(
  #       '''UPDATE estado SET descripcion=? WHERE id_estado=?''', (
  #           estado.getDescripcion(),
  #           estado.getId(),
  #       ))
  #   self.conexion.commit()

  # def eliminarEstado(self, estado):
  #   self.cursor.execute('''DELETE FROM estado WHERE id_estado=?''',
  #                       (estado.getId(), ))
  #   self.conexion.commit()

  # def listarEstados(self):
  #   self.cursor.execute('''SELECT * FROM estado''')
  #   estados = self.cursor.fetchall()
  #   return estados

  # #CRUD RESERVA
  # def agregarReserva(self, reserva):
  #   self.cursor.execute(
  #       '''INSERT INTO reserva(fecha_entrada,fecha_salida,id_cliente,id_habitacion) VALUES (?,?,?,?))''',
  #       (
  #           reserva.getFechaEntrada(),
  #           reserva.getFechaSalida(),
  #           reserva.getCliente().getId(),
  #           reserva.getHabitacion().getId(),
  #       ))
  #   self.conexion.commit()

  # def modificarReserva(self, reserva):
  #   self.cursor.execute(
  #       '''UPDATE reserva SET fecha_entrada=?, fecha_salida=?, id_cliente=?, id_habitacion=? WHERE id_reserva=?''',
  #       (
  #           reserva.getFechaEntrada(),
  #           reserva.getFechaSalida(),
  #           reserva.getCliente().getId(),
  #           reserva.getHabitacion().getId(),
  #       ))
  #   self.conexion.commit()

  # def eliminarReserva(self, reserva):
  #   self.cursor.execute('''DELETE FROM reserva WHERE id_reserva=?''',
  #                       (reserva.getId(), ))
  #   self.conexion.commit()

  # def listarReservas(self):
  #   self.cursor.execute('''SELECT * FROM reserva''')
  #   reservas = self.cursor.fetchall()
  #   return reservas

  # #COMPLETARLO
  # def listarReservasActivas(self):
  #   self.cursor.execute('''SELECT * FROM reserva WHERE tu_condicion_aqui''')
  #   habitaciones = self.cursor.fetchall()
  #   return habitaciones

  # #CRUD CLIENTE
  # def agregarCliente(self, cliente):
  #   self.cursor.execute(
  #       '''INSERT INTO cliente(dni,nombre,apellido,telefono,email) VALUES (?,?,?,?,?))''',
  #       (
  #           cliente.getDni(),
  #           cliente.getNombre(),
  #           cliente.getApellido(),
  #           cliente.getTelefono(),
  #           cliente.getEmail(),
  #       ))
  #   self.conexion.commit()

  # def modificarCliente(self, cliente):
  #   self.cursor.execute(
  #       '''UPDATE cliente SET dni=?,nombre=?,apellido=?,telefono=?,email=? WHERE id_cliente=?''',
  #       (
  #           cliente.getDni(),
  #           cliente.getNombre(),
  #           cliente.getApellido(),
  #           cliente.getTelefono(),
  #           cliente.getEmail(),
  #           cliente.getId(),
  #       ))
  #   self.conexion.commit()

  # def eliminarCliente(self, cliente):
  #   self.cursor.execute('''DELETE FROM cliente WHERE id_cliente=?''',
  #                       (cliente.getId(), ))
  #   self.conexion.commit()

  # def listarClientes(self):
  #   self.cursor.execute('''SELECT * FROM cliente''')
  #   clientes = self.cursor.fetchall()
  #   return clientes

  # #CRUD FACTURA
  # def agregarFactura(self, factura):
  #   self.cursor.execute(
  #       '''INSERT INTO factura(precio_total,fecha,id_metodo_pago,id_cliente,id_reserva) VALUES (?,?,?,?,?))''',
  #       (
  #           factura.getPrecioTotal(),
  #           factura.getFecha(),
  #           factura.getMetodoPago().getId(),
  #           factura.getCliente().getId(),
  #           factura.getReserva().getId(),
  #       ))
  #   self.conexion.commit()

  # def modificarFactura(self, factura):
  #   self.cursor.execute(
  #       '''UPDATE factura SET precio_total=?,fecha=?,id_metodo_pago=?,id_cliente=?, id_reserva=? WHERE id_factura=?''',
  #       (
  #           factura.getPrecioTotal(),
  #           factura.getFecha(),
  #           factura.getMetodoPago().getId(),
  #           factura.getCliente().getId(),
  #           factura.getReserva().getId(),
  #           factura.getId(),
  #       ))
  #   self.conexion.commit()

  # def eliminarFactura(self, factura):
  #   self.cursor.execute('''DELETE FROM factura WHERE id_factura=?''',
  #                       (factura.getId(), ))
  #   self.conexion.commit()

  # def listarFacturas(self):
  #   self.cursor.execute('''SELECT * FROM factura''')
  #   facturas = self.cursor.fetchall()
  #   return facturas

  # #CRUD METODOPAGO
  # def agregarMetodoPago(self, metodopago):
  #   self.cursor.execute('''INSERT INTO metodo_pago (nombre) VALUES(?))''',
  #                       (metodopago.getNombre(), ))
  #   self.conexion.commit()

  # def modificarMetodoPago(self, metodopago):
  #   self.cursor.execute(
  #       '''UPDATE metodo_pago SET nombre=? WHERE id_metodo_pago=?''', (
  #           metodopago.getNombre(),
  #           metodopago.getId(),
  #       ))
  #   self.conexion.commit()

  # def eliminarMetodoPago(self, metodopago):
  #   self.cursor.execute('''DELETE FROM metodo_pago WHERE id_metodo_pago=?''',
  #                       (metodopago.getId(), ))
  #   self.conexion.commit()

  # def listarMetodosPagos(self):
  #   self.cursor.execute('''SELECT * FROM metodo_pago''')
  #   metodos_pagos = self.cursor.fetchall()
  #   return metodos_pagos


#CIERRO LA CONEXION DE LA BD

  def cerrarConexion(self):
    self.conexion.close()
  # def cerrarConexion(self):
  #   self.cursor.close()
  #   self.conexion.close()
