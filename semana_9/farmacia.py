class paciente:
  def __init__(self, Nombre, Apellido, Rut, Edad, Direccion):
    self.nombre = Nombre
    self.Apellido = Apellido
    self.Rut = Rut
    self.Edad = Edad
    self.Direccion = Direccion

  def actualizarDatos(self,Nombre, Apellido, Edad, Direccion):
    self.nombre = Nombre
    self.Apellido = Apellido
    self.Edad = Edad
    self:Direccion = Direccion

  def mostrarDatos(self):
    return f"Paciente: Nombre{self.nombre}, Apellido: {self.Apellido}, Direccion: {self.Direccion}"


class Medico:
  def __init__(self, Nombre, Apellido, Direccion, Especialidad):
    self.Nombre = Nombre
    self.Apellido = Apellido
    self.Direccion = Direccion
    self.Especialidad = Especialidad

  def mostrarInfoMedico(self):
    return f"Medico: Nombre: {self.Nombre}, Apellido: {self.Apellido}, Especialidad: {self.Especialidad}"

  
class Persona:
  def __init__(self, Nombre, Apellido, Direccion):
    self.nombre = Nombre
    self.Apellido = Apellido
    self.Direccion = Direccion

  def actualizarDatos(self,Nombre, Apellido, Edad, Direccion):
    self.nombre = Nombre
    self.Apellido = Apellido
    self:Direccion = Direccion

  def datosPersona(self):
    return f"Cliente: {self.nombre}, Apellido: {self.Apellido}, Direccion: {self.Direccion}"

class Paciente(Persona):
  def __init__(self, Nombre, Apellido, Rut, Edad, Direccion):
    super().__init__(Nombre, Apellido, Direccion)
    self.Rut = Rut
    self.Edad = Edad

  def actualizarDatos(self, Nombre, Apellido, Edad, Direccion):
    super().actualizarDatos(Nombre, Apellido, Direccion)
    self.Edad = Edad

  def mostrarDatos(self):
    return f"Paciente: Nombre: {self.Nombre}, Apellido: {self.Apellido}, Edad: {self.Edad}, Direccion: {self.Direccion}, RUT: {self.Rut}"

class recetaMedica:
  def __init__(self, NombreMedico, Diagnostico, FechaEmision):
    self.NombreMedico = NombreMedico
    self.Diagnostico = Diagnostico
    self.FechaEmision = FechaEmision

  def mostrarReceta(self):
    return f"Receta: NombreMedico: {self.NombreMedico}, Diagnostico: {self.Diagnostico}, FechaEmision: {self.FechaEmision}"