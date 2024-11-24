import sympy as sp

class MatrizSimbolica:
    def __init__(self, num_generadores, num_horas, letra):
        """
        Inicializa la clase para crear una matriz simbólica con el formato `letra_i_t`.
        
        :param num_generadores: Número de generadores (filas).
        :param num_horas: Número de horas (columnas).
        :param letra: Letra base para las variables simbólicas.
        """
        self.num_generadores = num_generadores
        self.num_horas = num_horas
        self.letra = letra
        self.matriz = self.crear_matriz()  # Genera la matriz simbólica al inicializar

    def crear_matriz(self):
        """
        Crea la matriz simbólica de tamaño (num_generadores x num_horas) con el formato `letra_i_t`.
        
        :return: Matriz simbólica como una lista de listas.
        """
        matriz = []
        for i in range(1, self.num_generadores + 1):  # Itera sobre los generadores
            fila = []
            for t in range(1, self.num_horas + 1):  # Itera sobre las horas
                # Genera una variable simbólica en formato letra_i_t
                simbolo = sp.Symbol(f"{self.letra}_{i}_{t}")
                fila.append(simbolo)
            matriz.append(fila)
        return sp.Matrix(matriz)  # Retorna como una matriz de SymPy

    def __str__(self):
        """
        Representación en texto de la matriz simbólica.
        """
        return str(self.matriz)

