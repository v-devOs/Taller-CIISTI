import pg8000

class Database:

  def __init__(self):
    try:
      self.connection = pg8000.connect(
        host="localhost", 
        database="postgres", 
        user="postrges", 
        password="postgres",
        port=5435
      )
    except Exception as e:
      print('Error al conectar con la base de datos', e)

  def get_all(self):
    sql = self.connection.cursor()

    try:
      sql.execute('SELECT * FROM tareas;')

      registros = sql.fetchall()

      return registros
    
    except Exception as e:
      print('Error al realizar consulta', e)

  def close_connection(self):
    self.connection.close()

