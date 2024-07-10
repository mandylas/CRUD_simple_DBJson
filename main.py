import os
import json

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER + '/DB/' 'db.json')
with open (my_file, "r") as f:
    datos = json.load(f)
datos_personas = datos['Personas']
f.close()

class Persona:
    def __init__(self, cedula, nombre, apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
    
    # Método genérico pero con implementación particular
    
    def mostrar(self):
        lista_personas = {}
        
        for persona in datos["Personas"]:
            if self.cedula == None:
                print(persona)
            else:
                if persona['cedula'] == self.cedula:
                    #indice = datos["Personas"].index(persona)
                    lista_personas = persona
                    return(lista_personas)
            
    def agregar(self):
        nueva_persona = Persona(
            self.cedula,
            self.nombre,
            self.apellido,
        ).__dict__
        with open (my_file, "w") as fr:
            datos["Personas"].append(nueva_persona)
            json.dump(datos, fr, indent=4)
            fr.close()
            print("Persona agregada correctamente")
    def modificar(self):
        for persona in datos["Personas"]:
            if persona['cedula'] == self.cedula:
                persona['cedula'] = self.cedula
                persona['nombre'] = self.nombre
                persona['apellido'] = self.apellido
                with open (my_file, "w") as fw:
                    json.dump(datos, fw, indent=4)
                    fw.close()
                print("Persona modificada correctamente")
        
    
    def eliminar(self):
        for persona in datos["Personas"]:
            if persona['cedula'] == self.cedula:
                indice = datos["Personas"].index(persona)
                datos["Personas"].remove(persona)
                with open (my_file, "w") as fx:
                    json.dump(datos, fx, indent=4)
                    fx.close()
                print("Persona eliminada correctamente")
        

    def Accion(self):
        print(
              "Accion: ", type(self).__name__,
              "\nCedula: ", self.cedula,
              "\nNombre: ", self.nombre,
              "\nApellido: ", self.apellido
              
              )


cedula = None
nombre = None
apellido = None
mostrar_todos = Persona(cedula,nombre,apellido)
mostrar_todos.mostrar()

accion = input("""
            Seleccione accion: 1. Mostrar, 2. Agregar, 3. Editar, 4. Eliminar
      """
)

if accion == "1":
    cedula = input("ingrese cedula ")
    buscar_persona = Persona(cedula, nombre, apellido)
    print(buscar_persona.mostrar())

elif accion == "2":
    cedula = input("ingrese cedula ")
    nombre = input("ingrese nombre ")
    apellido = input("ingrese apellido ")
    persona_agregar = Persona(cedula, nombre, apellido)
    persona_agregar.agregar()

elif accion == "3":
    cedula = input("ingrese cedula ")
    buscar_persona = Persona(cedula, nombre, apellido)
    buscar_persona.mostrar()
    if buscar_persona == None:
        print("Persona no encontrada")
    else:
        cedula = input("ingrese cedula ")
        nombre = input("ingrese nuevo nombre ")
        apellido = input("ingrese nuevo apellido ")
        persona_modificar = Persona(cedula, nombre, apellido)
        persona_modificar.modificar()

elif accion == "4":
    cedula = input("ingrese cedula ")
    buscar_persona = Persona(cedula, nombre, apellido)
    buscar_persona.mostrar()
    if buscar_persona == None:
        print("Persona no encontrada")
    else:
        persona_eliminar = Persona(cedula, nombre, apellido)
        persona_eliminar.eliminar()


