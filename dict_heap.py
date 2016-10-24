# -*- coding: utf-8 -*-
#
# Autor: Iván Canales
# Version: 2.5
##

class dict_heap:
    """ CONSTRUCTOR """
    def __init__(self, iterable = None, set_max = 0, key = None):
        """
        Este heap incluye un diccionario en el que se guardan los valores de los nodos para acceder a su posicion.
        Esto permite que el acceso al nodo 'decrease_key' sea constante~ i por lo tanto el coste total sea log(n).

        Cabe tener en cuenta que en este heap los elementos 'data' deben ser únicos, pues perteneceran a un diccionario'
        :param set_max: Permite establecer un tamaño inicial para el heap.
        """
        if set_max < 0: raise Exception("set_max must be 0 or positive")

        if iterable:
            key = (lambda x: x) if key==None else key
            self._vec = [[key(i),i] for i in iterable]
            self._last = len(self._vec) - 1
        else:
            self._vec = [None] * set_max
            self._last = -1;
        self._items = {self._vec[i][1]:i for i in xrange(len(self) )}
        if self: self._build_heap()

    """ METODOS PRINCIPALES """

    def peek(self):
        """
        Devuelve el valor mínimo del heap sin modificarlo
        :return: lista [key, data]
        """
        if self._last > -1:
            return self._vec[0]
        else:
            raise Exception('Heap is empty')

    def pop(self):
        """
        Elimina y devuelve el elemento más pequeño por llave del heap
        :return:
        """
        tmp = self.peek()
        if self._last > -1:
            self._swap(0, self._last)
            self._last -= 1
            self._downheap()
            self._items.pop(tmp[1], None)
            return tmp
        else:
            raise Exception('Heap is empty')

    def insert(self,key, item = None):
        """
        Inserta un nuevo elemento en el heap
        :param key:
        :param item:
        :return:
        """
        item = item if item else key
        if item in self._items:
            raise Exception("El elemento " + item + " ya pertenece al heap")
        else:
            self._items[item] = self._next()
            n = [key,item]
            if len(self._vec) < self._next() + 1: self._vec.append(n) # si arribem al final fem append
            else: self._vec[self._next()] = n # si no simplement asociem
            self._last += 1
            self._upheap()

    """ METODOS DE AYUDA """
    def _swap(self, a, b):
        """
        Intercambia los nodos en posiciones 'a' y 'b'
        """
        temp = self._vec[a]
        self._items[self._vec[a][1]] = b
        self._items[self._vec[b][1]] = a

        self._vec[a] = self._vec[b]
        self._vec[b] = temp

    def _decrease_key(self, data, new_key, i):
        self._vec[i][0] = new_key
        self._swap(self._last, i)
        self._upheap()

    def _increase_key(self, data, new_key, i):
        self._vec[i][0] = new_key
        self._swap(i, 0)
        self._downheap()

    def _build_heap(self):
        for i in range(len(self)//2, -1, -1):
            self._downheap(i)

    def _next(self):
        """
        Devuelve la posicion del nodo immediatamente posterior al nodo final.
        Determina el punto de insercion de un nuevo nodo.
        :return:
        """
        return self._last + 1

    @staticmethod
    def _parent(i):
        """
        Devuelve el padre de un nodo.
        :param i: Posicion del nodo
        :return:
        """
        return (i - 1) >> 1

    @staticmethod
    def _children(i):
        """
        Devuelve las posiciones del los dos hijos asociados a un nodo
        :param i: posicion del nodo 'padre'
        :return:
        """
        return (i << 1) + 1, (i << 1) + 2

    def _upheap(self):
        i = self._last
        while i > 0:
            p = self._parent(i)
            if self._vec[i][0] < self._vec[p][0]:
                self._swap(i, p)
                i = p
            else: i = 0

    def _downheap(self, i = 0):
        l, r = self._children(i)
        min_ = i

        if l <= self._last and self._vec[l][0] < self._vec[min_][0]:
            min_ = l
        if r <= self._last and self._vec[r][0] < self._vec[min_][0]:
            min_ = r

        if min_ != i:
            self._swap(i, min_)
            self._downheap(min_)

    def _modify_key(self, data, new_key):
        """
        En el momento de modificar la key de un elemento del heap se deberia llamar esta función
        """
        if data in self:
            idx  = self._items[data]
            if self._vec[idx][0] > new_key:
                self._decrease_key(data, new_key, idx)
            elif self._vec[idx][0] <  new_key:
                self._increase_key(data, new_key, idx)
        else:
            raise Exception('Item does not exist.')

    """ SOBRECARGA DE METODOS """

    def __contains__(self, item):
        """
        Devuelve 'True' si el item item esta contenido en el heap
        """
        return item in self._items

    def __getitem__(self, data):
        """
        Devuelve la llave del elemento 'data'
        """
        return self._vec[self._items[data]][0]

    def __setitem__(self, data, new_key):
        self._modify_key(data, new_key)

    def __str__(self):
        return "[" + ", ".join(str(self._vec[i][1]) for i in range(self._last +1)) + "]"

    def __len__(self):
        return self._last + 1

    def __nonzero__(self):
        return self._last != -1

    def __iter__(self):
       return iter(self.d)

if __name__=='__main__':
    """ sanity check """
    l1 = [5, 4, 1, 2, 3, 8]
    l1_sorted = [1, 2, 3, 4, 5, 8]
    l1_ = []

    l2 = [(5,'a'), (4,'b'), (1,'c'), (2,'d'), (3,'e'), (8,'f')]
    l2_final = ['c', 'd', 'e', 'b', 'f', 'a']
    l2_ = []

    h2 = dict_heap()
    h1 = dict_heap(iter(l1))

    for key, val in l2: h2.insert(key, val)

    #cambio de llave
    h2['a'] = 10
    while h1:
        l1_.append(h1.pop()[1])

    while h2:
        print h2.peek()
        l2_.append(h2.pop()[1])

    print l1_
    print l2_
    print l1_ == l1_sorted and l2_ == l2_final
