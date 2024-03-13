"Ejercicio a"

# Define una clase Palindromo que contiene un método de clase para verificar si una cadena es un palíndromo
class Palindromo:
    @classmethod
    def esPalindromo(cls, cadena):
        # Elimina los caracteres no alfanuméricos y convierte a minúsculas
        cadena = ''.join(caracter.lower() for caracter in cadena if caracter.isalnum())
        # Comprueba si la cadena es igual a su inversa (es decir, si es un palíndromo)
        return cadena == cadena[::-1]

# Ejecuta el código de prueba solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    # Prueba el método esPalindromo con varias cadenas
    print(Palindromo.esPalindromo('radar'))  # Debería imprimir True
    print(Palindromo.esPalindromo('sonar'))  # Debería imprimir False
    print(Palindromo.esPalindromo('Arde ya la yedra'))  # Debería imprimir True
    print(Palindromo.esPalindromo('Ardeyalayedra'))  # Debería imprimir True
    print(Palindromo.esPalindromo('!@#$% %$#@!'))  # Debería imprimir True (ya que no hay caracteres alfanuméricos)
    print(Palindromo.esPalindromo('L O L'))  # Debería imprimir True
