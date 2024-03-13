"Ejercicio b"

# Importa la clase Palindromo del archivo palindromo_clase
from palindromo_clase import Palindromo

# Define una clase PalindromoHeredado que hereda de la clase Palindromo
class PalindromoHeredado(Palindromo):
    def __init__(self, cadena):
        self.cadena = cadena  # Inicializa la cadena que se va a evaluar

    def test(self):
        result = self.esPalindromo(self.cadena)  # Llama al método esPalindromo de la clase base
        if not result:
            print(self.cadena.upper())  # Imprime la cadena en mayúsculas si no es un palíndromo
        return result  # Devuelve el resultado de la comprobación

    def __del__(self):
        print(self.cadena.upper())  # Imprime la cadena en mayúsculas cuando se destruye la instancia

# Ejemplo de uso
# Crea una instancia de PalindromoHeredado con la cadena "radar" y prueba si es un palíndromo
p = PalindromoHeredado("radar")
print(p.test())  # Imprime True si es un palíndromo, False si no lo es

# Crea otra instancia de PalindromoHeredado con la cadena "sonar" y prueba si es un palíndromo
p = PalindromoHeredado("sonar")
print(p.test())  # Imprime True si es un palíndromo, False si no lo es
