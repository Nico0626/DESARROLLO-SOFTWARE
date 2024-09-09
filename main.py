from Maquina_coser import MaquinaDeCoser

def mostrar_menu():
    print("\n--- Menú de la Máquina de Coser ---")
    print("1. Encender máquina")
    print("2. Apagar máquina")
    print("3. Empezar a coser")
    print("4. Parar de coser")
    print("5. Cambiar color de hilo")
    print("6. Ajustar velocidad")
    print("7. Mostrar estado de la máquina")
    print("8. Salir")

def main():
    # Crear una instancia de la máquina de coser
    maquina = MaquinaDeCoser(modelo="ModeloX", color_hilo="blanco", velocidad=500)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-8): ")
        
        if opcion == '1':
            try:
                print(maquina.encender())
            except ValueError as e:
                print(e)
        
        elif opcion == '2':
            try:
                print(maquina.apagar())
            except ValueError as e:
                print(e)
        
        elif opcion == '3':
            try:
                cantidad = int(input("¿Cuántas puntadas vas a realizar?: "))
                print(maquina.empezar_cocer())
                maquina.puntadas_realizadas(cantidad)
                print(f"la maquina {maquina.modelo} hizo {cantidad} de puntadas")
                
            except ValueError as e:
                print(e)
        
        elif opcion == '4':
            try:
                print(maquina.parar_cocer())
            except ValueError as e:
                print(e)
        
        elif opcion == '5':
            nuevo_color = input("Ingresa el nuevo color de hilo: ")
            print(maquina.cambiar_hilo(nuevo_color))
            maquina.centimetros_hilo=1000
        
        elif opcion == '6':
            tipo_ajuste = input("¿Quieres aumentar o disminuir la velocidad? (a/d): ")
            cantidad = int(input("¿Cuánto ajustar? (en rpm): "))
            if tipo_ajuste == 'a':
                try:
                    print(maquina.aumentar_velocidad(cantidad))
                except ValueError as e:
                    print(e)
            elif tipo_ajuste == 'd':
                try:
                    print(maquina.disminuir_velocidad(cantidad))
                except ValueError as e:
                    print(e)
            else:
                print("Opción no válida")
        
        elif opcion == '7':
            print(maquina.estado_maquina())
        
        elif opcion == '8':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 9.")

if __name__ == '__main__':
    main()
