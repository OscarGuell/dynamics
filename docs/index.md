# Welcome to Dynamics Module!

En general, un modelo dinámico busca resolver la trayectoria temporal de una cantidad física como función de algún generador dinámico. En algunos casos, podemos modelar la dinámica de un estado genérico $y$ mediante la ecuación dinámica

$$\frac{dy}{dt} = f(t,y)$$

sujeta a la condición inicial

$$y(t_0)=y_0$$

Este programa estudia la evolución temporal de un estado $y(t)$, representado mediante una matriz 2x2 que corresponde a un operador lineal. La función que genera la dinámica del problema es

$$f(t,y) = -i[O,y(t)]$$

donde $O$ es otro operador lineal, $i$ es la constante compleja y $[A,B]$ $=$ $AB$ $-$ $BA$ es una operación de conmutación. Note que la función f(t,y) no depende explícitamente del tiempo, lo que simplificará la resolución del problema.

El proyecto se encuentra en [github.com](github.com/OscarGuell/dynamics)
