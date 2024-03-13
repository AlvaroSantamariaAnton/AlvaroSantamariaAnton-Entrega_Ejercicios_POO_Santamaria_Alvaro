"Ejercicio c"

class A:
    def z(self):
        return self

    def y(self, t):
        return len(t)

# Creamos una instancia de la clase A
objeto_A = A()

# Imprime la instancia de la clase A
print(objeto_A)

# Compara si la instancia objeto_A es igual a una nueva instancia de A
print(objeto_A is A())

# Llama al método y de la instancia objeto_A con una tupla vacía como argumento
print(objeto_A.y(()))

# Llama al método y de la clase A con una tupla que contiene la clase A como argumento
print(A().y((A,)))

# Llama al método y de la instancia objeto_A con una tupla que contiene la clase A y el método z
print(objeto_A.y((A, objeto_A.z)))

# Llama al método y de la instancia objeto_A con una tupla que contiene el método z, un entero y una cadena
print(objeto_A.y((objeto_A.z, 1, 'z')))
