#!/usr/bin/env python

import numpy as np

def dyn_generator(oper, state):
    """Multiplica el negativo de la constante compleja por el valor del 'permutador' ([A,B]=AB-BA) entre dos matrices, correspondientes a un operador y un estado inicial, respectivamente.

    Examples:
        >>> dyn_generator(np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]))
        [[0.0-0.0j 0.0+1.0j]
         [0.0-1.0j 0.0-0.0j]]

    Args:
        oper (array): Operador
        state (array): Estado inicial

    Returns:
        (array): Devuelve el resultado del permutador entre el operador `oper` y el estado inicial `state`, multiplicado por el negativo de la constante compleja.

    """
    return -1.0j*(np.dot(oper,state)-np.dot(state,oper))

def rk4(func, oper, state, h):
    """Determina la funcion solucion para el valor t=n+1 mediante el metodo de Rugen-Kutta de orden 4, dado un estado inicial 'state' correspondiente a la funcion solucion para el valor t=n, un intervalo de tiempo 'h', un operador 'oper' y una funcion 'func' que genera la dinamica temporal a estudiar.

    Examples:
        >>> rk4(dyn_generator, np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]), 0.20408163)
        [[0.95892891+0.0j 0.0+0.19841506j]
         [0.0-0.19841506j 0.04107109+0.0j]]

    Args:
        func (function): Funcion que genera la dinamica del problema
        oper (array): Operador de la funcion
        state (array): Estado inicial
        h (float): Representa el intervalo de tiempo transcurrido entre dos estados consecutivos

    Returns:
        (array): Devuelve la solucion de la dinamica temporal ingresada, a partir del estado inicial, mediante el Metodo Runge-Kutta de orden 4.

    """
    k1=func(oper,state)
    k2=func(oper,state+k1/2)
    k3=func(oper,state+k2/2)
    k4=func(oper,state+k3)
    return state + (h/6)*(k1+2*k2+2*k3+k4)
