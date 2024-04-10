class producto:
  def __init__(self, Nombre, Precio,Descripcion, Medico):
    self.Nombre = Nombre
    self.Precio = Precio
    self.Descripcion = Descripcion
    self.Medico = Medico
  

  
  def get_Nombre(self):
    return self.Nombre
  def set_Nombre(self,Nombre):
    self.Nombre = Nombre
  def get_Precio(self):
    return self.Precio
  def set_Precio(self, Precio):
    return self.Precio
  def get_Descripcion(self):
    return self.Descripcion
  def set_Descripcion(self, Descripcion):
    self.Descripcion
  def get_Medico(self):
    return self.Medico
  def set_Medico(self, Medico):
    self.Medico


lente = producto("Marco Vision", 100, "De Sol", "Juan")



    