class Medico:
  def __init__(self, Nombre, Apellido, Direccion, Especialidad):
    self.Nombre = Nombre
    self.Apellido = Apellido
    self.Direccion = Direccion
    self.Especialidad = Especialidad
    
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
  def get_Especialidad(self):
    return self.Especialidad
  def set_Especialidad(self, Especialidad):
    self.Especialidad = Especialidad
  
medico = Medico("Juan", "Perez", "Antonio Rojas 23","Oftalmologo")


    
