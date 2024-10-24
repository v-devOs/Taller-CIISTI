import pg8000
import datetime


class Database:

  def __init__(self):
    try:
      self.connection = pg8000.connect(
        host="localhost", 
        database="tareas", 
        user="admin_tareas", 
        password="postgres",
        port=5436
      )
    except Exception as e:
      print('Error al conectar con la base de datos', e)

  def get_all(self):
    sql = self.connection.cursor()

    try:
      sql.execute('SELECT * FROM tarea;')

      registros = sql.fetchall()

      
      for registro in registros:
        registro[3] = registro[3].strftime("%Y-%m-%d")

      return registros
    
    
    except Exception as e:
      print('Error al realizar consulta', e)

  def get_by_id( self, id ):
    sql = self.connection.cursor()

    try:
      sql.execute(f'SELECT * FROM tarea WHERE id = {id}')


      registro = sql.fetchone()

      registro[3] = registro[3].strftime("%Y-%m-%d")

      return registro
    except Exception as e:
      print('Error al realizar consulta', e)
  
  def create( self, data ):

    sql = self.connection.cursor()

    try:
      sql.execute('INSERT INTO tarea (titulo, contenido, fecha_fin) VALUES (%s, %s, %s)', (data['titulo'], data['contenido'], data['fecha_fin']))
      
      return True
    
    except Exception as e:
      print('Error al realizar inserción', e)
      return False

  def update( self, data):
    sql = self.connection.cursor()

    try: 

      sql.execute('''
          UPDATE tarea 
          SET titulo = %s, contenido = %s, fecha_fin = %s , terminado = %s
          WHERE id = %s
      ''', (data['titulo'], data['contenido'], data['fecha_fin'], data['id']))

      return True

    except Exception as e:
      print('Error al actualizar datos', e)
      return False
    
  def mark_as_complete( self, id ):
    sql = self.connection.cursor()

    try: 

      sql.execute('''
          UPDATE tarea 
          SET terminado = %s
          WHERE id = %s
      ''', (True, id ))

      return True
    except Exception as e:
      print('Error al actualizar tarea', e)
      return False
    

  def close_connection(self):
    self.connection.close()