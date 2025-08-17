

class Cliente:
    def __init__(self, id, nombre, telefono, correo):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        
        
        
class Mascota:
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        
    def __str__(self):
        return f"{self.nombre} ({self.tipo}, {self.edad} años)"   
        
        
class Hotel_mascota:
    def __init__(self):
        self.mascotas_alojadas = []
        self.cargar_alojamientos()

    def alojar_mascota(self, mascota, cliente):
        for c, m in self.mascotas_alojadas:
            if c.id == cliente.id and m.nombre.lower() == mascota.nombre.lower():
                print(f"Ya existe una mascota llamada '{mascota.nombre}' alojada por el cliente con ID {cliente.id}.")
                return False
        self.mascotas_alojadas.append((cliente, mascota))
        self.guardar_alojamientos()
        print(f"{mascota.nombre} ha sido alojada por {cliente.nombre}.")
        return True



    def retirar_mascota(self, nombre_mascota):
        for i, (cliente, mascota) in enumerate(self.mascotas_alojadas):
            if mascota.nombre.lower() == nombre_mascota.lower():
                del self.mascotas_alojadas[i]
                self.guardar_alojamientos()
                print(f"{mascota.nombre} ha sido retirada.")
                return True
        print(f"No se encontró la mascota '{nombre_mascota}'.")
        return False

    def guardar_alojamientos(self):
        try:
            with open("alojamiento.txt", "w", encoding="utf-8") as f:
                for cliente, mascota in self.mascotas_alojadas:
                    f.write(f"{cliente.id},{cliente.nombre},{cliente.telefono},{cliente.correo},{mascota.nombre},{mascota.tipo},{mascota.edad}\n")
        except Exception as e:
            print(f"Error al guardar alojamientos: {e}")

    def cargar_alojamientos(self):
        try:
            with open("alojamiento.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 7:
                        id_str, nombre_cliente, telefono, correo, nombre_mascota, tipo, edad_str = datos
                        try:
                            cliente = Cliente(int(id_str), nombre_cliente, telefono, correo)
                            mascota = Mascota(nombre_mascota, tipo, int(edad_str))
                            self.mascotas_alojadas.append((cliente, mascota))
                        except ValueError:
                            print(f"Error de formato en línea: {linea.strip()}")
        except FileNotFoundError:
            print("Archivo 'alojamiento.txt' no encontrado. Se creará al guardar.")
        except Exception as e:
            print(f"Error al cargar alojamientos: {e}")


    def listar_mascotas(self):
        if not self.mascotas_alojadas:
            print("No hay mascotas alojadas.")
        else:
            for cliente, mascota in self.mascotas_alojadas:
                print(f"{mascota} - Cliente: {cliente.nombre} (ID: {cliente.id}), telefono{cliente.telefono}, e-mail{cliente.correo}")

            