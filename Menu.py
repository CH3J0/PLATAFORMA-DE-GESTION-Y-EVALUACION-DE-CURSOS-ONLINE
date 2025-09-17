# MENU
def menu_principal(plataforma):
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar nuevo usuario")
        print("2. Acceder como usuario existente")
        print("3. Crear curso")
        print("4. Inscribir estudiante en curso")
        print("5. Crear evaluación")
        print("6. Mostrar información de curso")
        print("7. Mostrar todos los usuarios")
        print("8. Salir")
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
            else:
                print("Usuario no encontrado. Regístrese primero.")

        elif opcion == "3":
            codigo = pedir_codigo()
            nombre = pedir_nombre_curso()
            id_instructor = pedir_id()
            try:
                plataforma.crear_curso(codigo, nombre, id_instructor)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            id_estudiante = pedir_id()
            codigo_curso = pedir_codigo()
            plataforma.inscribir_estudiante_en_curso(id_estudiante, codigo_curso)

        elif opcion == "5":
            codigo_curso = pedir_codigo()
            curso = plataforma.obtener_info_curso(codigo_curso)
            if curso:
                nombre_eval = pedir_nombre_evaluacion()
                tipo_eval = pedir_tipo_evaluacion()
                evaluacion = Evaluacion(nombre_eval, tipo_eval)
                curso.crear_evaluacion(evaluacion)
            else:
                print("Curso no encontrado.")

        elif opcion == "6":
            codigo_curso = pedir_codigo()
            curso = plataforma.obtener_info_curso(codigo_curso)
            if curso:
                curso.mostrar_info_completa()
            else:
                print("Curso no encontrado.")

        elif opcion == "7":
            print("\n--- LISTA DE USUARIOS REGISTRADOS ---")
            for u in plataforma.usuarios.values():
                print(u)
                print("-" * 40)

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")

# INSTANCIA GENERAL
plataforma = Plataforma()
menu_principal(plataforma)
