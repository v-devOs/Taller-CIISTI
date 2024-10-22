import eel

from utils.database.db import Database 


db = Database()
class ExposerDB:

  @eel.expose
  @staticmethod
  def get_all_registers():
    return db.get_all()

  @eel.expose
  @staticmethod
  def get_one_by_id( id ):
    return db.get_by_id(id)
  
  @eel.expose
  @staticmethod
  def create_register( data ):
    return db.create(data)
  

  @eel.expose
  @staticmethod
  def update_register( data, complete = False ):
    return db.update( data, complete )

