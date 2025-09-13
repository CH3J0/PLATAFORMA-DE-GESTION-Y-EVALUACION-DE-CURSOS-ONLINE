# VALIDACIONES
def pedir_id():
    while True:
        id_usuario = input("Ingrese el ID (solo números): ")
        if id_usuario.isdigit():
            return int(id_usuario)
        print("Error: El ID debe contener solo números.")

def pedir_nombre():
    while True:
        nombre = input("Ingrese el nombre (sin números): ")
        if nombre.replace(" ", "").isalpha():
            return nombre
        print("Error: El nombre no debe contener números ni símbolos.")

def pedir_email():
    while True:
        email = input("Ingrese el correo electrónico: ")
        if "@" in email and "." in email:
            return email
        print("Error: El correo debe contener '@' y '.'")

def pedir_codigo():
    while True:
        codigo = input("Ingrese el código del curso (solo números): ")
        if codigo.isdigit():
            return int(codigo)
        print("Error: El código debe contener solo números.")

def pedir_nombre_curso():
    while True:
        nombre = input("Ingrese el nombre del curso (sin números): ")
        if nombre.replace(" ", "").isalpha():
            return nombre
        print("Error: El nombre no debe contener números ni símbolos.")

def pedir_nombre_evaluacion():
    while True:
        nombre = input("Ingrese el nombre de la evaluación: ")
        if nombre.strip():
            return nombre
        print("Error: El nombre no puede estar vacío.")

def pedir_tipo_evaluacion():
    while True:
        tipo = input("Ingrese el tipo de evaluación (Ej: Examen, Proyecto, Tarea): ")
        if tipo.replace(" ", "").isalpha():
            return tipo
        print("Error: El tipo debe contener solo letras.")
