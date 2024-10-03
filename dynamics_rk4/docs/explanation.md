# Explanation

Para la resolución del problema, se utiliza el Método de Runge-Kutta de orden 4 (RK4). En forma general, el método de 'orden s' tiene la forma:

$$y_{n+1} = y_n +h\sum_{i=1}^s b_i k_i$$

donde $y_n$ es la función solución para el valor t=n, $y_{n+1}$ es la función solución para el valor t=n+1, $h$ es el paso de iteración (el incremento del tiempo entre puntos sucesivos) y los coeficientes k_i son términos de aproximación medios, con coeficientes propios del esquema numérico escogido. En este caso, el Método de Runge-Kutta de orden 4 tiene la siguiente forma:

$$ y_{n+1}=y_n+\frac{1}{6}\cdot(k_1+2k_2+2k_3+k_4)$$


$$k_1=h\cdot f(t_n,y_n)$$


$$k_2=h\cdot f(t_n,y_n+\frac{k_1}{2})$$


$$k_3=h\cdot f(t_n,y_n+\frac{k_2}{2})$$


$$k_4=h\cdot f(t_n,y_n+k_3)$$

En general, las imágenes para $k>1$ suelen estar evaluadas en el punto $t_n+\frac{h}{2}$, sin embargo, el segundo término de la suma desaparece debido a que la función no depende explícitamente del tiempo.

