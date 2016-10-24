# ESTRUCTURAS DE DATOS

## Heap
En este modulo se incluyen dos versiones de la cola prioritaria tipo 'heap'.

### dict\_heap

#### Funciones
* `min_heap(iterable, set_max, key)`: devuelve un objeto de tipo dict\_heap. Si se proporciona un iterador lo genera a partir del iterador con coste lineal. Con `key` se puede definir una funcion de comparacion.
* `peek()`: permite ver (sin eliminar) el elemento con la llave más pequeña del heap.
* `pop()`: permite ver y eliminar el elememto con la llave más pequeña del heap.
* `insert(key, item)`: permite insertar un elemento en el heap. Para usar el item como llave se puede usar el constructor con un elemento.
