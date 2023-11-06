# import unittest
# from basededatos.conexion import Conexion  # Asegúrate de importar la clase y módulo adecuados

# class TestConexion(unittest.TestCase):

#     def test_getCantHabitaciones(self):
#         # Crea una instancia de la clase Conexion o utiliza una existente si es necesario
#         conexion = Conexion("basededatos/mi_bd.db", app)

#         # Llama a la función getCantHabitaciones
#         cantidad_habitaciones = conexion.getCantHabitaciones()

#         # Realiza una aserción para verificar si la cantidad de habitaciones es un entero positivo
#         self.assertIsInstance(cantidad_habitaciones, int)
#         self.assertGreaterEqual(cantidad_habitaciones, 0)

# if __name__ == '__main__':
#     unittest.main()



# # import unittest
# # from unittest.mock import Mock
# # from tu_modulo import Conexion  # Importa tu clase de conexión

# # class TestConexion(unittest.TestCase):

# #     def test_getCantHabitaciones(self):
# #         # Crea un objeto Mock que simule la conexión a la base de datos
# #         conexion_mock = Mock()

# #         # Configura el valor que debe devolver el método getCantHabitaciones simulado
# #         conexion_mock.getCantHabitaciones.return_value = 10

# #         # Crea una instancia de la clase Conexion con el objeto Mock
# #         conn = Conexion(conexion_mock)

# #         # Llama a la función que quieres probar
# #         resultado = conn.getCantHabitaciones()

# #         # Verifica si el resultado es igual a lo que esperas
# #         self.assertEqual(resultado, 10)

# # if __name__ == '__main__':
# #     unittest.main()

