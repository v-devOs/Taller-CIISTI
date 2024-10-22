import xlwings


class ExcelWings:

  def __init__(self, file ):
    self.work_book = xlwings.Book(file)
    self.work_sheet = self.work_book.sheets('Tareas')

  def insert_data( self, tupla_datos  ):
    
    for index, datos in enumerate( tupla_datos ):
      self.work_sheet.range(f'A{2 + index }').value = datos

  def save_and_close(self):
    self.work_book.save()
    self.work_book.close()