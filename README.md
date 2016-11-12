
# dict\_heap
## ATENCIÓN: LA DOCUMENTACIÓN NO ESTA AL DÍA
**dict\_heap** es una estructura de datos diseñada a partir de un diccionario. A diferencia de un diccionario tradicional los elementos estan ordenados siguiendo una estructura de heap binario, de manera que actua como una cola prioritaria con acceso constante a los elementos.

## Funciones

* `min_heap([iterable[, key[,default]]])`: devuelve un objeto de tipo dict\_heap. Si se proporciona un iterador lo genera a partir del iterador con coste lineal. Con `key` se puede definir una funcion de comparacion.
* `peek()`: permite ver (sin eliminar) el elemento con la llave más pequeña del heap.
* `pop()`: permite ver y eliminar el elememto con la llave más pequeña del heap.
* `insert(key[, item])`: permite insertar un elemento en el heap. Para usar el item como llave se puede usar el constructor con un elemento.

### Funciones heredadas de MutableMapping
* `values()`: devuelve todos los valores del *dict\_heap*, i.e. los valores de la cola prioritaria.

* `keys()`: devuelve todsa las llaves de los elementos de la cola prioritaria.

* `items()`: devuelve todos los pares (llave, valor) de la cola prioritaria.

* `__cmp__(dict)`:

* `__contains__(item)`:

* `__delitem__(key)`:

* `__getitem__(data)`:

* `__setitem__(data, new_key)`:

* `__str__()`:

* `__len__()`:

* `__nonzero__()`:

* `__iter__()`:
