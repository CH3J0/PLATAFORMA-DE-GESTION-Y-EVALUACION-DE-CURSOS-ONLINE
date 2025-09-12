def menu_principal(plataforma):
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar nuevo usuario")
        print("2. Acceder como usuario existente")
        print("3. Mostrar todos los usuarios")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("¿Es Estudiante (E) o Instructor (I)? ").strip().upper()
            id_usuario = pedir_id()
            if id_usuario in plataforma.usuarios:
                print("Ya existe un usuario con ese ID. Use la opción 2 para acceder.")
                continue
            nombre = pedir_nombre()
            email = pedir_email()

            if tipo == "E":
                usuario = Estudiante(id_usuario, nombre, email)
            elif tipo == "I":
                usuario = Instructor(id_usuario, nombre, email)
            else:
                print("Tipo no válido.")
                continue

            plataforma.registrar_usuario(usuario)

        elif opcion == "2":
            id_usuario = pedir_id()
            usuario = plataforma.usuarios.get(id_usuario)
            if usuario:
                print("\n--- USUARIO ENCONTRADO ---")
                print(usuario)
                # Aquí podrías agregar submenús según el tipo de usuario
            else:
                print("Usuario no encontrado. Regístrese primero.")

        elif opcion == "3":
            print("\n--- LISTA DE USUARIOS REGISTRADOS ---")
            for u in plataforma.usuarios.values():
                print(u)
                print("-" * 40)

        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
