"Ejercicio d"

import os  # Importa la biblioteca os para trabajar con rutas de archivo y directorio

class Logger:
    def __init__(self):
        self.count = 0  # Inicializa el contador de registros
        # Obtiene la ruta del directorio del script actual y concatena el nombre del archivo de registro
        script_dir = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(script_dir, "log.txt")
        # Abre el archivo de registro en modo escritura
        self.log_file = open(log_path, "w")
        # Escribe un mensaje de inicio en el archivo de registro
        self.log_file.write("--Start log--\n")
    
    def __del__(self):
        # Escribe un mensaje de finalización en el archivo de registro con el recuento de registros
        self.log_file.write("--End log: {} log(s)--".format(self.count))
        # Cierra el archivo de registro
        self.log_file.close()

    def log(self, message):
        self.count += 1  # Incrementa el contador de registros
        # Escribe el mensaje de registro en una nueva línea en el archivo de registro
        self.log_file.write(message + "\n")


class Test:
    def __init__(self):
        # Inicializa una instancia de la clase Logger para el registro
        self.logger = Logger()

    def llamada(self, mensaje):
        # Llama al método log del Logger para registrar un mensaje
        self.logger.log(mensaje)

test = Test()
# Realiza algunas llamadas para registrar mensajes
for i in range(1, 6):
    if i == 1:
        test.llamada("Primera llamada")
    else:
        test.llamada("{}ª llamada".format(i))
