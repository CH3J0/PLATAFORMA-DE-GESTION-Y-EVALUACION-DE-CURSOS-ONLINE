# clase usuario, para conocer la información del usuario
class Usuario:
    def __init__(self, id_usuario, nombre, email):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        
    def __str__(self):
        return (
            f"--- BIENVENIDO USUARIO ---\n"             # Presentamos al usuario 
            f" - Nombre de usuario: {self.nombre}\n"
            f" - Id de usuario: {self.id_usuario}\n"
            f" - Correo electrónico de usuario: {self.email}"
        )
