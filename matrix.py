from functools import reduce


def process_matrix(matrix):
  if matrix == []: # caso trivial
    return []
  elif is_numerical_matrix(matrix): # caso correcto
    return _process_matrix(matrix)
  else:
    #error
    raise ValueError('Only works on numerical matrices')


def is_numerical_matrix(matrix):
    for i, column in enumerate(matrix):
        for j, value  in enumerate(column):
            if type(value) != int:
                return False
            else: 
                return True    



def _process_matrix(matrix):
    """
    Recibe una matrix de listas y devuelve una nueva, con los elementos cambiados.
    Cada elemento de la nueva sera el promedio del valor antiguo y de sus vecinos
    """
    new_matrix = []
    
    for i, column in enumerate(matrix):
        new_column = []
        for j, value  in enumerate(column):
            new_value = process_element(i, j, matrix)
            new_column.append(new_value)

        new_matrix.append(new_column)  

    return new_matrix


def process_element(i, j, matrix):   # matriz o elements
    """
    Recibe el indice de un elemento y la matriz en la que esta, 
    calcula su promedio con sus vecinos
    y devuelve dicho promedio
    """
    # obtengo la lista de vecinos
    #indices = get_neighbours_indices(i, j, matrix)
    indices = get_indices(i, j, matrix)

    indices_filtrado = get_indices_filtrado(indices, 0, len(matrix))

    #values = get_neighbours_values(indices, matrix)
    values = get_values(indices_filtrado, matrix)

    # calculo su promedio
    average = get_average(values)

    # devuelvo el valor final
    return average    


def get_indices(i, j, matrix):
    """
    Devuelve la lista de indices de los vecinos.
    Se incluye al propio elemento
    """
    indices = [] 

    indices.append([i + 1, j])
    indices.append([i - 1, j])
    indices.append([i, j + 1])
    indices.append([i, j - 1])
    indices.append([i, j])

    return indices

def is_in_range(point, min_value, max_value):
    if point[0] < max_value and point[0] >= min_value and point[1] < max_value and point[1] >= min_value:
        return True

def get_indices_filtrado(indices, min_value, max_value):
    indices_filtrado = []
    for point in indices:  
        if is_in_range(point, min_value, max_value):
            indices_filtrado.append(point)
    return indices_filtrado


def first_coord(point):
   return point[0]


def second_coord(point):
  return point[1]


def get_value(point, matrix):
    return matrix[first_coord(point)][second_coord(point)]
    
     
def get_values(indices_filtrado, matrix):
    values = []
    for point in indices_filtrado:
        value = get_value(point, matrix)
        values.append(value)
    return values    


def get_average(values):
    """
    Recibe una lista de numeros(get_values()) y devuelve su promedio
    """    
    return reduce(lambda accum, b: accum + b, values, 0)  /  len(values)



print(process_matrix([[1, 10], [2, 3]]))