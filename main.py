from Clases import Cliente, Mascota, Hotel_mascota

def menu_hotel():
    hotel = Hotel_mascota()
    try:

        while True:
            print("\n--- Gestor de Hotel de Mascotas ---")
            print("1. Ingresar mascota")
            print("2. Retirar mascota")
            print("3. Listar mascotas alojadas")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                try:
                    id_cliente = int(input("ID del cliente: "))
                    nombre_cliente = input("Nombre del cliente: ")
                    nombre_mascota = input("Nombre de la mascota: ")
                    telefono_cliente = input("Ingrese el teléfono del cliente: ")
                    correo_cliente = input("Ingrese el correo del cliente: ")

                    tipo_mascota = input("Tipo de mascota (Perro, Gato, etc.): ")
                    edad_mascota = int(input("Edad de la mascota: "))

                    cliente = Cliente(id_cliente, nombre_cliente,telefono_cliente,correo_cliente)
                    mascota = Mascota(nombre_mascota, tipo_mascota, edad_mascota)
                    hotel.alojar_mascota(mascota, cliente)
                except ValueError:
                    print("Error: Ingrese datos válidos.")

            elif opcion == "2":
                hotel.listar_mascotas()
                nombre_mascota = input("Nombre de la mascota a retirar: ")
                hotel.retirar_mascota(nombre_mascota)

            elif opcion == "3":
                hotel.listar_mascotas()

            elif opcion == "4":
                print("Gracias por usar el gestor. ¡Hasta luego!")
                break

            else:
                print("Opción inválida. Intente nuevamente.")
    except KeyboardInterrupt:
        print("\n\nProceso interrumpido por el usuario (Ctrl+C).")

if __name__ == "__main__":
    menu_hotel()
