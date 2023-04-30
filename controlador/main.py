class produccion:
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def __repr__(self):
        return f"{self.izquierda} -> {' '.join(self.derecha)}"

def factorizar_gramatica(producciones):
        # Creamos un diccionario para almacenar los prefijos comunes
        prefijos = {}
        # Recorremos todas las producciones
        for produccion in producciones:
            # Recorremos los símbolos del lado derecho de la producción
            for i in range(1, len(produccion.derecha)):
                # Tomamos el prefijo desde el inicio hasta el índice actual
                prefijo = tuple(produccion.derecha[:i])
                # Si el prefijo ya está en el diccionario, actualizamos la producción
                if prefijo in prefijos:
                    new_nonterminal = prefijos[prefijo]
                    new_produccion = produccion(new_nonterminal, list(prefijo) + ['X'])
                    produccion.derecha = produccion.derecha[i:]
                    producciones.append(new_produccion)
                    break
            # Si no encontramos prefijos comunes, añadimos el prefijo al diccionario
            else:
                prefijo = tuple(produccion.derecha)
                prefijos[prefijo] = produccion.izquierda
        return producciones

producciones = [
    produccion('S', ['E']),
    produccion('S', ['T']),
    produccion('E', ['S', '+', 'T']),
    produccion('E', ['S', '-', 'T']),
    produccion('T', ['F']),
    produccion('T', ['T1', '*', 'F']),
    produccion('T', ['T1', '/', 'F']),
    produccion('T1', ['T']),
    produccion('T1', ['S']),
    produccion('F', ['(', 'E', ')']),
    produccion('F', ['num']),
]

factorizar_gramatica(producciones)
