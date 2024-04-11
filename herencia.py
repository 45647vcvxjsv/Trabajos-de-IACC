class persona:
  def __init__(self, Nombre, Apellido, Direccion):
    self.Nombre = Nombre
    self.Apellido = Apellido
    self.Direccion = Direccion
  
  def get_Nombre(self):
    return self.Nombre
  def set_Nombre(self, Nombre):
    self.Nombre = Nombre
  def get_Apellido(self):
    return self.Apellido
  def set_Apellido(self, Apellido):
    self.Apellido = Apellido
  def get_Direccion(self):
    return self.Direccion
  def set_Direccion(self, Direccion):
    self.Direccion = Direccion
  
class Medico(persona):
  def __init__(self, Nombre, Apellido, Direccion, Especialidad):
    super().__init__(Nombre, Apellido, Direccion)
    self.Especialidad = Especialidad

  def get_Especialidad(self):
    return self.Especialidad
  
  def set_Especialidad(self, Especialidad):
    self.Especialidad = Especialidad

class producto:
  def __init__(self, Nombre, Precio, Descripcion, Medico=None):
    self.Nombre = Nombre
    self.Precio = Precio
    self.Descripcion = Descripcion
    self.Medico = Medico
  
  def get_Nombre(self):
    return self.Nombre
  def set_Nombre(self, Nombre):
    self.Nombre = Nombre
  def get_Precio(self):
    return self.Precio
  def set_Precio(self, Precio):
    self.Precio = Precio
  def get_Descripcion(self):
    return self.Descripcion
  def set_Descripcion(self, Descripcion):
    self.Descripcion = Descripcion
  def get_Medico(self):
    return self.Medico
  def set_Medico(self, Medico):
    self.Medico = Medico

class Cliente(persona):
  def __init__(self, Nombre, Apellido, Direccion, Historial_Medico):
    super().__init__(Nombre, Apellido, Direccion)
    self.Historial_Medico = Historial_Medico
  
  def get_Historial_Medico(self):
    return self.Historial_Medico
  def set_Historial_Medico(self, Historial_Medico):
    self.Historial_Medico = Historial_Medico

  


