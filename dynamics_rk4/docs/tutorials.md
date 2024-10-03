# Tutorials

Para desarrollar un ejemplo de uso del programa, escogeremos el siguiente operador:

    oOper = np.array([[0, 1], [1, 0]])

$oOper = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$

donde dicho operador puede tener distintos significados físicos dependiendo del problema dinámico en cuestión, desde un mapa algebráico, un generador dinámico de un sistema caótico, un Hamiltoniano, etc.

Lo siguiente es definir una condición inicial para el estado $y(t)$, en este caso:

    yInit = np.array([[1, 0], [0, 0]])

$yInit = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$

Con las funciones del programa a nuestra disposición, podemos evaluar la dinámica temporal en una grilla temporal unidimensional. Utilizaremos la función numpy.linspace para crear un arreglo de valores temporales homogéneos.

    times = np.linspace(0,10)

$times = [0.00000000\text{    }0.20408163\text{    }0.40816327\text{    }0.6122490\text{    }0.81632653\text{    }1.02040816 ...]$

Recordando que la función rk4() depende de un valor h, correspondiente al intervalo entre dos valores temporales consecutivos y sabiendo que el arreglo seleccionado es homogéneo, es posible calcularlo como la diferencia de dos valores consecutivos cualesquiera.

    h = (times[1]-times[0])

$h = 0.20408163$

Ahora, para crear una rutina que realice la evolución temporal, se establece una copia del operador que representa el estado inicial, debido a que el objetivo es ir registrando cómo varía su valor sin perder registro del 'original'. La función copy() de numpy permite este procedimiento:

    yCopy = yInit.copy()
    
$yCopy = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$

Llamaremos la rutina rk4() de manera iterativa, calculando el operador del estado del sistema $y(t)$ a través del tiempo, donde iremos guardando la entrada (0,0) y (1,1) de la matriz $y(t)$. Considere que sólo es necesario guardar estas dos entradas debido a que tanto el valor inicial como el operador $O$ son diagonales. Para esto, se generan dos arreglos con valores iniciales cero, utiliznado el mismo tamaño del arreglo que contiene los valores de la variable independiente temporal.

    stateQuant00 = np.zeros(times.size)
    stateQuant11 = np.zeros(times.size)

$stateQuant00 = [0.0\text{    }0.0\text{    }0.0\text{    }0.0 ...]$
$stateQuant11 = [0.0\text{    }0.0\text{    }0.0\text{    }0.0 ...]$

Finalmente, la rutina principal estará dada por un ciclo for loop:

    for tt in range(times.size):
        
        stateQuant00[tt]=yInit[0][0].real
        stateQuant11[tt]=yInit[1][1].real
        yN = rk4(dyn_generator,oOper,yInit,h)
        yInit = yN


