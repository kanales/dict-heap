# -*- coding: utf-8 -*-
#
# Autor: Iván Canales
# Version: 2.5
##
from collections import MutableMapping
import itertools

class dict_heap(MutableMapping):
    __slots__ = ['_heap', '_last']
    """ CONSTRUCTOR """
    def __init__(self, iterable = None, default = None, key = None):
        """
        Este heap incluye un diccionario en el que se guardan los valores de los
        nodos para acceder a su posicion.  Esto permite que el acceso al nodo
        'decrease_key' sea constante~ i por lo tanto el coste total sea log(n).

        Cabe tener en cuenta que en este heap los elementos 'data' deben ser
        únicos, pues perteneceran a un diccionario' :param set_max: Permite
        establecer un tamaño inicial para el heap.
        """
        if iterable:
            if default != None:
                self._heap = [[default, i] for i in iterable]
            elif default != None:
                self._heap = [[key(i),i] for i in iterable]
            else:
                self._heap = [[i,i] for i in iterable]
            self._last = len(self._heap) - 1
        else:
            self._heap = [None]
            self._last = -1;
        self.__dict__ = {self._heap[i][1]:i for i in xrange(len(self))}
        if self: self._build_heap()

    """ METODOS PRINCIPALES """

    def peek(self):
        """
        Devuelve el valor mínimo del heap sin modificarlo
        :return: lista [key, data]
        """
        if self._last > -1:
            return self._heap[0]
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
            self.__dict__.pop(tmp[1], None)
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
        if item in self.__dict__:
            raise Exception("El elemento " + item + " ya pertenece al heap")
        else:
            self.__dict__[item] = self._next()
            n = [key,item]
            if len(self._heap) < self._next() + 1: 
                self._heap.append(n) # si arribem al final fem append
            else: 
                self._heap[self._next()] = n # si no simplement asociem
            self._last += 1
            self._upheap()

    """ METODOS DE AYUDA """
    def _swap(self, a, b):
        """
        Intercambia los nodos en posiciones 'a' y 'b'
        """
        self.__dict__[self._heap[a][1]] = b
        self.__dict__[self._heap[b][1]] = a

        self._heap[a], self._heap[b] = self._heap[b], self._heap[a],

    def _decrease_key(self, data, new_key, i):
        self._heap[i][0] = new_key
        self._swap(self._last, i)
        self._upheap()

    def _increase_key(self, data, new_key, i):
        self._heap[i][0] = new_key
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
        return (i * 2) + 1, (i * 2) + 2

    def _upheap(self):
        i = self._last
        while i > 0:
            p = self._parent(i)
            if self._heap[i][0] < self._heap[p][0]:
                self._swap(i, p)
                i = p
            else: i = 0

    def _downheap(self, i = 0):
        l, r = self._children(i)
        min_ = i

        if l <= self._last and self._heap[l][0] < self._heap[min_][0]:
            min_ = l
        if r <= self._last and self._heap[r][0] < self._heap[min_][0]:
            min_ = r

        if min_ != i:
            self._swap(i, min_)
            self._downheap(min_)

    def _modify_key(self, data, new_key):
        """
        En el momento de modificar la key de un elemento del heap se deberia
        llamar esta función 
        """
        if data in self:
            idx  = self.__dict__[data]
            if self._heap[idx][0] > new_key:
                self._decrease_key(data, new_key, idx)
            elif self._heap[idx][0] <  new_key:
                self._increase_key(data, new_key, idx)
        else:
            raise Exception('Item does not exist.')

    """ SOBRECARGA DE METODOS """
    def values(self):
        return self.__dict__.keys()

    def keys(self):
        return (x[0] for x in self._heap)

    def items(self):
        return itertools.izip(self.keys(), self.values())

    def __cmp__(self, dict):
        return cmp(self.__dict__, dict)

    def __contains__(self, item):
        """
        Devuelve 'True' si el item item esta contenido en el heap
        """
        return item in self.__dict__

    def __delitem__(self, key):
        idx = self._dict__.pop(key, None)
        del self._heap[idx]

    def __getitem__(self, data):
        """
        Devuelve la llave del elemento 'data'
        """
        return self._heap[self.__dict__[data]][0]

    def __setitem__(self, data, new_key):
        self._modify_key(data, new_key)

    def __str__(self):
        return ''.join("[", ", ".join(str(self._heap[i][1]) for i in
            range(self._last +1))"]")

    def __len__(self):
        return self._last + 1

    def __nonzero__(self):
        return self._last != -1

    def __iter__(self):
        return iter(self.items())

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
