
import math
import numpy as np
import matplotlib.pyplot as plt

class Polinomio():
    
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes
    
    #Mostrar el polinomio
    def __str__(self):
        if (self.coeficientes[0] != 0):
            resultado = str(self.coeficientes[0])+'+'
        else:
            resultado = ''

        #Por estetica escribimos el coeficiente de grado 1 sin el ^1

        if (self.coeficientes[1] != 1):
            resultado += str(self.coeficientes[1])+'*x+'
        else:
            resultado +='x+'


        for i in range(2, len(self.coeficientes)):
            if (self.coeficientes[i] != 0):
                if (self.coeficientes[i] != 1):
                    resultado += str(self.coeficientes[i])+'*x^'+str(i)+'+'
                else:
                    resultado +='x^'+str(i)+'+'
        resultado = resultado[:-1]
        return(resultado)

    #Sobrecarga del operador suma
    def __add__(self, otro):
        if (len(self.coeficientes) == len(otro.coeficientes)):
            nuevos_coef = []
            for i in range(0,len(self.coeficientes)):
                nuevos_coef += [self.coeficientes[i]+otro.coeficientes[i]]
            return(Polinomio(nuevos_coef))
        else:
            if  (len(self.coeficientes) > len(otro.coeficientes)):
                nuevos_coef = []
                for i in range(0,len(otro.coeficientes)):
                    nuevos_coef += [self.coeficientes[i]+otro.coeficientes[i]]
                for i in range(len(otro.coeficientes), len(self.coeficientes)):
                    nuevos_coef +=[self.coeficientes[i]]
            else:
                nuevos_coef = []
                for i in range(0,len(self.coeficientes)):
                    nuevos_coef += [self.coeficientes[i]+otro.coeficientes[i]]
                for i in range(len(self.coeficientes), len(otro.coeficientes)):
                    nuevos_coef +=[otro.coeficientes[i]]
            return(Polinomio(nuevos_coef))  

    #Sobrecarga del operador diferencia
    def __sub__(self, otro):
        nuevos_coef = []
        for i in otro.coeficientes:
            nuevos_coef += [-i] 
        return Polinomio(self.coeficientes) + Polinomio(nuevos_coef)
    
    #Sobrecarga del operador multiplicacion(falta acabarlo)
    def __mul__(self,b):
        if (type(b) == float or type(b) == int):
            nuevos_coef = []
            for i in self.coeficientes:
                nuevos_coef += [b * i]
            return Polinomio(nuevos_coef)
        if type(b) == Polinomio:
            nuevos_coef = [0]*(len(self.coeficientes)+len(b.coeficientes)-1)
            for indice_1, coeficiente_1 in enumerate(self.coeficientes):
                for indice_2, coeficiente_2 in enumerate(b.coeficientes):
                    nuevos_coef[indice_1+indice_2] += coeficiente_1 * coeficiente_2
            return(Polinomio(nuevos_coef))  
    
    #Sobrecargamos el operador == para ver cuando dos polinomios son iguales
    def __eq__(self,b):
        if (self.grado() != b.grado()):
            return False
        else:
            iguales = True
            for i in range(0,len(self.coeficientes)):
                if (self.coeficientes[i]!=b.coeficientes[i]):
                    iguales = False
                    break
                else:
                    iguales = True
            return(iguales)

    def __ne__(self, b):
        if self == b:
            return False
        else: 
            return True

    #Metodo que devuelce el grado del polinomio
    def grado(self):
        return len(self.coeficientes)-1

    #Metodo que devuelce las raices del polinomio (solo grados uno y dos, otro grados pfff)
    def raices(self):
        factores = []
        if self.grado() == 1:
             factores += [(-self.coeficientes[1])/(self.coeficientes[0]*1.0)]
        
        if self.grado() == 2:
            discriminante = self.coeficientes[1]**2 - 4 * self.coeficientes[2] * self.coeficientes[0]
            if discriminante < 0:
                print('No existen soluciones reales de la ecuación')
            elif discriminante == 0:
                raiz = -self.coeficientes[1]/(2.0*self.coeficientes[2])
                factores += [raiz]
            else:
                raiz_1 =(-self.coeficientes[1]+math.sqrt(discriminante))/(2.0*self.coeficientes[2])
                raiz_2 =(-self.coeficientes[1]-math.sqrt(discriminante))/(2.0*self.coeficientes[2])
                factores += [raiz_1, raiz_2]
        return factores        

        if self.grado >=3:
            print('Resolver esto ya puede ser complicado')

    #Metodo que imprime la factorizacion del polinomio por pantalla
    def factorizacion(self):
        raices_polinomio = self.raices()
        print(raices_polinomio)
        factor=''
        for i in raices_polinomio:
            if (i>0):
                factor += '(x-' + str(i) +')*'
            if i==0:
                factor += 'x*'
            if i<0:
                factor += '(x' + str(i) +')*'
        factor = factor[:-1]
        return(factor)

    #Metodo que evalua un polinomio en un punto
    def eval(self, num):
        #Implementaremos el algoritmo de Horner
        resultado = 0
        for i in reversed(self.coeficientes):
            resultado *= num
            resultado += i
        return(resultado)

    def derivada(self):
        coef_derivada = []
        for i in range(1, len(self.coeficientes)):
            coef_derivada += [(i)*self.coeficientes[i]]
        return(Polinomio(coef_derivada))

    def grafica(self, inicio_intervalo, final_intervalo):
        x = np.linspace(inicio_intervalo, final_intervalo, 100) 
        plt.plot(x, self.eval(x))
        plt.grid()
        plt.show()

#Funcion para introducir un polinomio
def get_polinimio():
    print('Introduce los coefientes del polinomio empezando por el de grado cero (f para terminar): ')
    seguir = True
    coeficientes = []
    while seguir:
        siguiente = input()
        if siguiente == 'f':
            seguir = False
        else:
            coeficientes += siguiente
    return(Polinomio(coeficientes))