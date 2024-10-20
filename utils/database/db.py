import pg8000

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

      return registros
    
    except Exception as e:
      print('Error al realizar consulta', e)

  def get_by_id( self, id ):
    sql = self.connection.cursor()

    try:
      sql.execute(f'SELECT * FROM tarea WHERE id = {id}')


      registro = sql.fetchone()

      return registro
    except Exception as e:
      print('Error al realizar consulta', e)
  
  def create( self, data ):

    sql = self.connection.cursor()

    try:
      # Asumiendo que 'sql' es tu cursor
        sql.execute('INSERT INTO tarea (titulo, contenido, fecha_fin) VALUES (%s, %s, %s)', (data['titulo'], data['contenido'], data['fecha_fin']))
    except Exception as e:
      print('Error al realizar inserción', e)
      

  def close_connection(self):
    self.connection.close()

